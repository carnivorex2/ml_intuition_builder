import torch
import torch.nn as nn
import os
import argparse

def build_dataset():
    DATA_DIR = "data"
    TRAIN_X_PATH = os.path.join(DATA_DIR, "train_x.pt")
    TRAIN_Y_PATH = os.path.join(DATA_DIR, "train_y.pt")
    VAL_X_PATH = os.path.join(DATA_DIR, "val_x.pt")
    VAL_Y_PATH = os.path.join(DATA_DIR, "val_y.pt")

    # Check if data files exist
    if all(os.path.exists(p) for p in [TRAIN_X_PATH, TRAIN_Y_PATH, VAL_X_PATH, VAL_Y_PATH]):
        print("Loading data from files...")
        train_x = torch.load(TRAIN_X_PATH)
        train_y = torch.load(TRAIN_Y_PATH)
        val_x = torch.load(VAL_X_PATH)
        val_y = torch.load(VAL_Y_PATH)
    else:
        print("Generating new dataset...")
        # Create a "slightly larger" dataset of 1000 samples for Part 4
        total_samples = 1000
        dataset_x = torch.arange(total_samples, dtype=torch.float32).unsqueeze(1)
        dataset_y = torch.zeros((total_samples, 2))
        # Simple decision boundary
        for i in range(dataset_y.shape[0]):
            if i < 350:
                dataset_y[i] = torch.tensor([1.0, 0.0])
            else:
                dataset_y[i] = torch.tensor([0.0, 1.0])
        
        # Randomly sample for train/validation split
        indices = torch.randperm(total_samples)
        train_size = int(0.8 * total_samples)
        
        train_indices = indices[:train_size]
        val_indices = indices[train_size:]
        
        train_x = dataset_x[train_indices]
        train_y = dataset_y[train_indices]
        val_x = dataset_x[val_indices]
        val_y = dataset_y[val_indices]

        # Save the dataset to files
        os.makedirs(DATA_DIR, exist_ok=True)
        torch.save(train_x, TRAIN_X_PATH)
        torch.save(train_y, TRAIN_Y_PATH)
        torch.save(val_x, VAL_X_PATH)
        torch.save(val_y, VAL_Y_PATH)
        print("Dataset saved to data/ directory.")

    return train_x, train_y, val_x, val_y

def create_model():
    layer1 = nn.Linear(1,500)
    layer2 = nn.ReLU()
    layer3 = nn.Linear(500,500)
    layer4 =nn.ReLU()
    layer5 = nn.Linear(500,2)
    model = nn.Sequential(layer1,layer2,layer3,layer4,layer5)
    return model

def main(mode='train'):
    train_x, train_y, val_x, val_y = build_dataset()
    # print(dataset_x.shape)
    # print(dataset_x)
    # print(dataset_y.shape)
    print("Train Y shape:", train_y.shape)
    print("Val Y shape:", val_y.shape)
    model = create_model()
    
    CHECKPOINT_PATH = "models/checkpoint.pth"

    if mode=='use':
        output = model(train_x)
        print(nn.Softmax(1)(output))
    elif mode=='train':
        for i in range(2000):
            output = model(train_x)
            loss_fn = nn.CrossEntropyLoss()
            loss=loss_fn(output,train_y)
            if i%100==0:
                print(loss.data)
            loss.backward()
            for p in model.parameters():
                p.data-=p.grad*.1
            for p in model.parameters():
                p.grad.zero_()
        
        # Save the trained model
        os.makedirs("models", exist_ok=True)
        torch.save(model.state_dict(), CHECKPOINT_PATH)
        print(f"\nModel state saved to {CHECKPOINT_PATH}")

        output = model(train_x)
        for i in range(len(train_x)):
            print(train_x[i])
            print(nn.Softmax(1)(output)[i])
        # print(train_x, "->" nn.Softmax(1)(output))
    elif mode=='val':
        # Load the trained model
        if os.path.exists(CHECKPOINT_PATH):
            model.load_state_dict(torch.load(CHECKPOINT_PATH))
            print(f"Model state loaded from {CHECKPOINT_PATH}")
        else:
            print("\nWARNING: Checkpoint not found. Running validation on an untrained model.")

        print("\n--- Starting Validation ---")
        model.eval() # Set model to evaluation mode
        loss_fn = nn.CrossEntropyLoss()

        with torch.no_grad(): # Disable gradient calculation
            val_output = model(val_x)
            val_loss = loss_fn(val_output, val_y)
            
            # Calculate accuracy
            _, predicted_classes = torch.max(val_output, 1)
            _, true_classes = torch.max(val_y, 1) 
            
            correct_predictions = (predicted_classes == true_classes).sum().item()
            accuracy = correct_predictions / len(val_y)

            print(f"Validation Loss: {val_loss.item():.4f}")
            print(f"Validation Accuracy: {accuracy * 100:.2f}%")
        print("--- Validation Finished ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run training, validation, or inference modes.")
    parser.add_argument("--mode", type=str, default="train", choices=["train", "val", "use"],
                        help="Mode to run: 'train', 'val', or 'use'.")
    args = parser.parse_args()

    print(torch.cuda.is_available())
    main(mode=args.mode)