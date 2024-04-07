from fastai.vision.all import *
import time

def label_func(x):
    """
    Label function to extract the category of the image based on its parent directory name.
    """
    return x.parent.name

def run():
    """
    Main function to train a model to classify images into directional movements.
    """
    # Define the path to your dataset
    path = Path("dataset_gta")
    
    # Get image file paths from the dataset
    fnames = get_image_files(path)
    print(f"Total Images: {len(fnames)}")

    # Create ImageDataLoaders
    dls = ImageDataLoaders.from_path_func(path, fnames, label_func, item_tfms=Resize(224), bs=40, num_workers=0)
    
    # Create a CNN learner with ResNet18 architecture
    learn = cnn_learner(dls, resnet18, metrics=error_rate)
    
    # Train the model
    print("Training started")
    learn.fine_tune(4, base_lr=1.0e-02)
    print("Training completed")

    # Export the trained model for later use
    learn.export()

if __name__ == '__main__':
    run()
