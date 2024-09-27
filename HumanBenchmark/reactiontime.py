import pyautogui
from pynput.mouse import Button, Controller
import time

def get_color_at_pixel(x, y):
    # Capture only the specific pixel to reduce overhead
    screenshot = pyautogui.screenshot(region=(x, y, 1, 1))
    # Get the color at the pixel (x, y) which is the top-left of the region
    color = screenshot.getpixel((0, 0))
    return color

mouse = Controller()
green = (75, 219, 106)

try:
    while True:
        color = get_color_at_pixel(200, 200)
        if color == green:
            mouse.click(Button.left, 1)
        
        # Wait for a short period before updating
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nProgram exited.")