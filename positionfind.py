import pyautogui
import time
from PIL import ImageGrab

def get_color_at_mouse():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Take a screenshot of the screen
    screenshot = ImageGrab.grab()

    # Get the color at the mouse position
    color = screenshot.getpixel((x, y))

    return color

try:
    while True:
        color = get_color_at_mouse()
        
        # Clear the console line (optional)
        print(f"\rMouse position: ({color})", end='')
        
        # Wait for a short period before updating
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nProgram exited.")
    
