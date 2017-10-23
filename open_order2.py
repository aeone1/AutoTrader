'''refined open orders, but works best if only one order and thats ok for me.'''
import pyautogui

no_orders = int(raw_input('How many orders do you want to open? '))
order = raw_input('buy or sell? ')

def buy():
    '''buy order'''
    while True:
        buy_button_region = (334, 116, 51, 30)
        pos_buy = pyautogui.locateCenterOnScreen('blue_buy.png', region = buy_button_region)
        if pos_buy is not None:
            break
    pyautogui.click(pos_buy)
    print 'Clicked on buy.'

def sell():
    '''sell order'''
    while True:
        sell_button_region = (193, 116, 51, 30)
        pos_sell = pyautogui.locateCenterOnScreen('red_sell.png', region = sell_button_region)
        if pos_sell is not None:
            break
    pyautogui.click(pos_sell)
    print 'Clicked on sell.'

for i in range(0, no_orders):
    if order == 'buy':
        buy()
    elif order == 'sell':
        sell()
    else:
        print 'Didn\'t specify order, please specify order type.'
