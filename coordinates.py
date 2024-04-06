import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()  # Get the current mouse position.
        print(f"Cursor Position: X: {x} Y: {y}", end='\r')
        time.sleep(0.1)  # Pause for a short moment to make the output readable.
except KeyboardInterrupt:
    print("\nExited by user")
