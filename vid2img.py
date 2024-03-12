import cv2
import os

# Define the path to the video file and the output folder
video_path = 'Pipeline dataset.mov'
output_folder = 'images'

# Make sure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video file")
else:
    frame_count = 0
    while True:
        # Read a new frame
        ret, frame = cap.read()
        if ret:
            # Save the frame as an image file
            frame_path = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
            cv2.imwrite(frame_path, frame)
            print(f'Saved {frame_path}')
            frame_count += 1
        else:
            # Break the loop if there are no more frames
            break

    # Release the VideoCapture object
    cap.release()
    print("Done extracting frames.")

