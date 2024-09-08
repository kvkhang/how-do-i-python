import pyautogui
from pynput.keyboard import Controller
import time

def get_color_at_pixel(x, y):
    # Capture only the specific pixel to reduce overhead
    screenshot = pyautogui.screenshot(region=(x, y, 1, 1))
    # Get the color at the pixel (x, y) which is the top-left of the region
    color = screenshot.getpixel((0, 0))
    return color

# Define pixel coordinates for color detection
pixel_xA, pixel_yA = 800, 960
pixel_xS, pixel_yS = 905, 960
pixel_xJ, pixel_yJ = 1010, 960
pixel_xK, pixel_yK = 1115, 960

keyboard = Controller()

# Maintain the state of keys
key_states = {
    'a': False,
    's': False,
    'j': False,
    'k': False
}

def update_key_state(key, should_press):
    if should_press:
        if not key_states[key]:
            keyboard.press(key)
            key_states[key] = True
    else:
        if key_states[key]:
            keyboard.release(key)
            key_states[key] = False

try:
    while True:
        # Get colors at specified pixels
        colorA = get_color_at_pixel(pixel_xA, pixel_yA)
        colorS = get_color_at_pixel(pixel_xS, pixel_yS)
        colorJ = get_color_at_pixel(pixel_xJ, pixel_yJ)
        colorK = get_color_at_pixel(pixel_xK, pixel_yK)
        
        # Calculate color intensities
        intensityA = sum(colorA)
        intensityS = sum(colorS)
        intensityJ = sum(colorJ)
        intensityK = sum(colorK)
        
        # Update key states based on color intensities
        update_key_state('a', intensityA > 430)
        update_key_state('s', intensityS > 430)
        update_key_state('j', intensityJ > 430)
        update_key_state('k', intensityK > 430)

        # Wait for a short period before the next check
        time.sleep(0.001)

except KeyboardInterrupt:
    print("\nProgram exited.")
