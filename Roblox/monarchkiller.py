import pyautogui
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as Kontroller
from PIL import ImageGrab

def get_color_at_mouse(x, y):
    # Get the current mouse position
    

    # Take a screenshot of the screen
    screenshot = ImageGrab.grab()

    # Get the color at the mouse position
    color = screenshot.getpixel((x, y))

    return color

mouse = Controller()
keyboard = Kontroller()
color = get_color_at_mouse(1050, 160)
try:
    while(1):
        color = get_color_at_mouse(781, 160)
        if (color[0] > 210 and color[1] < 70 and color[2] < 70):
            keyboard.tap("2")
        else:
            mouse.click(Button.left, 1)
        time.sleep(1)
except KeyboardInterrupt:
    print("Program Exited")