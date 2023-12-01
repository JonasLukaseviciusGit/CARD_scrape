from selenium import webdriver      # for opening webpage
from PIL import Image, ImageGrab    # for taking screenshots and handling images
import pyautogui                    # for moving mouse and clicking
import pyperclip                    # for copying and pasting (using clipboard)
import random                       # for generating random number in file name uniquification
import time                         # for delays
import os                           # for deleting screenshots


def manual_downloading(folder_path=r'C:\Users\HP\Desktop\CARD\google_scholar\articles',
                       mouse_movement_duration=1,
                       initial_wait_duration=2,
                       click_wait=0.5,
                       url='https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/lim2.13'):
    filename = None

    # Initializing the browser and opening the window in full screen
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(initial_wait_duration)

    # Screenshot screen place where download button is supposed to be
    x1, y1, x2, y2 = 1770, 175, 1785, 195
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screenshot.save("screenshot-button.jpg")

    # Compare pixel values screenshot and saved download button
    download_button = Image.open("download_button.jpg")
    screenshot = Image.open("screenshot-button.jpg")
    screenshot = list(screenshot.getdata())
    download_button = list(download_button.getdata())

    # If download button is there, continue normally
    if screenshot == download_button:

        # Move to download button and click it
        pyautogui.moveTo(1778, 174, duration=mouse_movement_duration)
        pyautogui.click()
        time.sleep(click_wait)

        # Move to location field and replace Desktop location with folder_path
        pyautogui.moveTo(362, 70, duration=mouse_movement_duration)
        pyautogui.doubleClick()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        pyautogui.write(folder_path)
        pyautogui.press('enter')

        # Move to save button and click it
        pyautogui.moveTo(1714, 976, duration=mouse_movement_duration)
        pyautogui.click()
        time.sleep(click_wait)

        # Screenshot screen place where message may appear (message that file already exists)
        ImageGrab.grab(bbox=(1000, 510, 1190, 550)).save("screenshot-message.jpg")
        message = list(Image.open("message.jpg").getdata())
        screenshot = list(Image.open("screenshot-message.jpg").getdata())

        # If message ('file already exists') appears, rename the file
        if screenshot == message:
            pyautogui.moveTo(1140, 537, duration=mouse_movement_duration)   # Drag mouse to 'NO' button on the message
            pyautogui.click()                                               # Click 'NO' button (replace file → NO)
            time.sleep(click_wait)
            pyautogui.moveTo(1203, 885, duration=mouse_movement_duration)   # Drag mouse to file name field
            pyautogui.click()                                               # Put cursor in file name field
            pyautogui.hotkey('ctrl', 'c')                                   # Copy file name
            filename = pyperclip.paste()
            index = random.randint(100, 999)
            filename = f'{filename}-{index}'                                # Add index to change file name
            pyperclip.copy(filename)                                        # Copy new file name
            pyautogui.press('delete')                                       # Delete old file name
            pyautogui.hotkey('ctrl', 'v')                                   # Paste new file name
            pyautogui.moveTo(1714, 976, duration=mouse_movement_duration)   # Drag mouse to save button
            pyautogui.click()                                               # Click save button
            time.sleep(click_wait)
            filename = index
        else:
            pass

        # Delete screenshots
        absolute_path = os.path.abspath("screenshot-button.jpg")
        os.remove(absolute_path)
        absolute_path = os.path.abspath("screenshot-message.jpg")
        os.remove(absolute_path)
    # If download button is not there, don't do anything
    else:
        pass

    # Close the browser window
    pyautogui.moveTo(1891, 21, duration=mouse_movement_duration)
    pyautogui.click()
    time.sleep(click_wait)

    # Closing browser window and returning index or None
    driver.quit()
    return filename
