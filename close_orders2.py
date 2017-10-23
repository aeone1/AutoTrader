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

# doing this has saved me roughly 6 seconds on every loop.
# Although it adds 2 seconds to the start of the loop though. 
w_close_button = pyautogui.locateOnScreen('w_close.png')
g_close_button = pyautogui.locateOnScreen('g_close.png')
h_close_button = pyautogui.locateOnScreen('h_close.png')


for i in range(0, interval):
    if w_close_button != None:
        print 'w_close button'
        w_close()
    elif g_close_button != None:
        print 'g_close button'
        g_close()
    elif h_close_button != None:
        print 'h_close button'
        h_close()
    else:
        print 'Nothing to close...'
    