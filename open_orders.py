'CLick on sell and close after some seconds'
import pyautogui

interval = int(raw_input('How many orders do you want to open? '))
order_type = raw_input('buy or sell? ')

for i in range(0, interval):
    if order_type == 'sell' and list(pyautogui.locateAllOnScreen('red_sell.png')) != []:
        print 'selling red'
        x, y = pyautogui.locateCenterOnScreen('red_sell.png')
        print x, y
        pyautogui.moveTo(x, y, 0.1)
        pyautogui.click(x, y)
    elif order_type == 'sell' and list(pyautogui.locateAllOnScreen('blue_sell.png')) != []:
        print 'selling blue'
        x, y = pyautogui.locateCenterOnScreen('blue_sell.png')
        print x, y
        pyautogui.moveTo(x, y, 0.1)
        pyautogui.click(x, y)
    elif order_type == 'buy' and list(pyautogui.locateAllOnScreen('red_buy.png')) != []:
        print 'buying red'
        x, y = pyautogui.locateCenterOnScreen('red_buy.png')
        print x, y
        pyautogui.moveTo(x, y, 0.1)
        pyautogui.click(x, y)
    elif order_type == 'buy' and list(pyautogui.locateAllOnScreen('blue_buy.png')) != []:
        print 'buying blue'
        x, y = pyautogui.locateCenterOnScreen('blue_buy.png')#bug - it can change at any moment
        print x, y
        pyautogui.moveTo(x, y, 0.1)
        pyautogui.click(x, y)
    else:
        print 'Please specify Order type. '
    