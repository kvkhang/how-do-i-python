import pyautogui
import time
from PIL import ImageGrab

def get_color_at_mouse(x, y):
    # Get the current mouse position
    

    # Take a screenshot of the screen
    screenshot = ImageGrab.grab()

    # Get the color at the mouse position
    color = screenshot.getpixel((x, y))

    return color

try:
    while True:
        x, y = pyautogui.position()
        color = get_color_at_mouse(x, y)
        
        # Clear the console line (optional)
        print(f"\rMouse position: ({x}, {y}), ({color})", end='')
        
        # Wait for a short period before updating
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nProgram exited.")
    
