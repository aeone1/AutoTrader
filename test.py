'Testbed for all tests'
from sys import argv
import pyautogui

#using argv to get name of file
# dont forget to specify/add file type
#----------------------------------
#script, picname = argv

#pyautogui.screenshot(picname)
#using a png file i saved to search the screen
print pyautogui.locateOnScreen('red_sell.png')
print pyautogui.locateOnScreen('blue_sell.png')
