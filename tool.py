import pyautogui
import time
import cv2 as cv
import numpy as np

def find_image(name, screenshot, threshold=0.9):
    store_image = cv.imread(name)
    if store_image is None:
        raise ValueError(f"Could not load image '{name}'")
    
    store_image = store_image[:,:,:3]
    
    screenshot_array = np.array(screenshot)[:, :, ::-1].copy()
    
    result = cv.matchTemplate(screenshot_array, store_image, cv.TM_CCOEFF_NORMED)
    max_val = np.max(result)
    
    if max_val >= threshold:
        return True
    return False

screenshot = pyautogui.screenshot()

def main():
    result = find_image("images\\windows-icon.png", screenshot)
    if (result):
        {
            print("Image finded")
        }
    else:
        {
            print("Image not finded")
        }

if __name__ == "__main__":
    main()
