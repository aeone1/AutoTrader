'Close \'interval\' numbers of trades'
import pyautogui

interval = int(raw_input('How many trades to close? '))

def w_close():
    'white close button'
    x, y = pyautogui.locateCenterOnScreen('w_close.png')
    print x, y
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
    pyautogui.moveTo(1234, 56)

def g_close():
    'grey close button'
    x, y = pyautogui.locateCenterOnScreen('g_close.png')
    print x, y
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
    pyautogui.moveTo(1234, 56)

def h_close():
    'hilighted close button or Blue close button'
    x, y = pyautogui.locateCenterOnScreen('h_close.png')
    print x, y
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
    pyautogui.moveTo(1234, 56)


for i in range(0, interval):
    if list(pyautogui.locateAllOnScreen('w_close.png')) != []:
        print 'w_close'
        w_close()
    elif list(pyautogui.locateAllOnScreen('g_close.png')) != []:
        print 'g_close'
        g_close()
    elif list(pyautogui.locateAllOnScreen('h_close.png')) != []:
        print 'h_close'
        h_close()
    else:
        print 'nothing to close...'
    