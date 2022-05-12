import pyautogui
import time
import cv2 as cv
import numpy as np

def find_image(name, screenshot):
    store_image = cv.imread(name)
    store_image = store_image[:,:,:3]
    screenshot_array = np.array(screenshot)
    screenshot_array = screenshot_array[:, :, ::-1].copy()
    result = cv.matchTemplate(screenshot_array, store_image, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    threshold = 0.9
    locations = np.where(result >= threshold)
    if max_val > .9:
        return True
    return False  

time.sleep(2)
screen = pyautogui.screenshot()
windowsicon = find_image('images/windows-icon.png', screen)

if windowsicon == True:
    print('Windows icon found')
else:
    print('Windows icon not found')

# print(pyautogui.position())
# print("pyautogui is working")