import cv2
import numpy as np
from mss import mss

def capture_screen(bbox=(0, 0, 640, 480)):
    """
    Capture the screen within the specified bounding box (bbox).
    The default bbox corresponds to a windowed mode game resolution.
    """
    with mss() as sct:
        monitor = {"top": bbox[1], "left": bbox[0], "width": bbox[2], "height": bbox[3]}
        screenshot = sct.grab(monitor)
        # Convert to an OpenCV image (BGR)
        img = np.array(screenshot)[:, :, :3]
        return img

def process_image(img):
    """
    Convert the image to grayscale and apply Canny edge detection.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def main():
    while True:
        # Capture the screen
        img = capture_screen()

        # Process the image
        processed_img = process_image(img)

        # Display the result
        cv2.imshow("Processed Image", processed_img)

        # Break the loop when the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
