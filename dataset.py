import matplotlib.pyplot as plt
import os
import shutil

# Set the path to the directory containing your images
image_folder_path = 'images'
# Set the path to the base directory where the "up", "down", "left", "right" folders exist
base_folder_path = 'Dataset'

# Get a list of image file names
image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]

# Function to move image to designated folder
def move_image(image_path, direction):
    target_folder_path = os.path.join(base_folder_path, direction)
    shutil.move(image_path, target_folder_path)
    print(f"Moved {os.path.basename(image_path)} to {direction} folder")

# Function to delete the current image
def delete_image(image_path):
    os.remove(image_path)
    print(f"Deleted {os.path.basename(image_path)}")

# Function to handle key presses
def on_key(event):
    global current_image_index
    if event.key in ['up', 'down', 'left', 'right']:
        move_image(os.path.join(image_folder_path, image_files[current_image_index]), event.key)
    elif event.key == 'space':
        delete_image(os.path.join(image_folder_path, image_files[current_image_index]))
    
    # Move to the next image or close if at the end
    current_image_index += 1
    if current_image_index < len(image_files):
        update_figure(current_image_index)
    else:
        plt.close()

    if event.key == 'escape':
        plt.close()

# Function to update figure with the next image
def update_figure(index):
    # Clear the current figure to load a new image
    plt.clf()
    img = plt.imread(os.path.join(image_folder_path, image_files[index]))
    plt.imshow(img)
    plt.draw()

# Setup the plot
fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', on_key)
current_image_index = 0

if image_files:
    update_figure(current_image_index)
    plt.show()
else:
    print("No images found in the specified folder.")
