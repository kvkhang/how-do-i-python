import pyautogui
import time
from pynput.keyboard import Controller

keyboard = Controller()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Done")