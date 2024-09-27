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
    driver.get('https://humanbenchmark.com/tests/number-memory')
    driver.maximize_window()
    time.sleep(15) # Let the user actually see something!
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Start']")
    # Get the location and size of the element
    
    center_x, center_y = screen_position(element)
    
    mouse = Controller()
    mouse.position = (center_x, center_y)
    mouse.click(Button.left, 1)
    
    time.sleep(1)
    
    NUMBER_element = driver.find_element(By.XPATH, "//div[@class='big-number ']")
    print(NUMBER_element.text)
    
    TIMER_element = driver.find_element(By.XPATH, "//div[@class='number-timer-bar']")
    print (TIMER_element.text)
    
        
except KeyboardInterrupt:
    print("\nProgram exited.")
    driver.quit()