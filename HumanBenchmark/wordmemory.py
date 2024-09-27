import time
import pyautogui
from pynput.mouse import Button, Controller
from selenium import webdriver
from selenium.webdriver.common.by import By

def screen_position(element):
    location = element.location
    size = element.size
    
    center_x = location['x'] + size['width'] / 2
    center_y = location['y'] + size['height'] / 2
    center_y += 120
    return center_x, center_y

try:
    driver = webdriver.Chrome()
    driver.get('https://humanbenchmark.com/tests/verbal-memory')
    driver.maximize_window()
    time.sleep(15) # Let the user actually see something!
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Start']")
    # Get the location and size of the element
    
    center_x, center_y = screen_position(element)
    
    mouse = Controller()
    mouse.position = (center_x, center_y)
    mouse.click(Button.left, 1)
    
    SEEN_element = driver.find_element(By.XPATH, "//button[normalize-space()='SEEN']")
    SEEN_location = screen_position(SEEN_element)
    
    NEW_element = driver.find_element(By.XPATH, "//button[normalize-space()='NEW']")
    NEW_location = screen_position(NEW_element)
    
    time.sleep(5)
    words = {"word1", "word2"}
    while True:
        try:
            WORD_element = driver.find_element(By.XPATH, "//div[@class='word']")
            current = WORD_element.text
            if current not in words:
                words.add(current)
                mouse.position = (NEW_location)
                mouse.click(Button.left, 1)
            else:
                mouse.position = (SEEN_location)
                mouse.click(Button.left, 1)
            time.sleep(0.01)
        except:  # noqa: E722
            time.sleep(1)
        
except KeyboardInterrupt:
    print("\nProgram exited.")
    driver.quit()