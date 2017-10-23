'close a trade by its type'
import pyautogui

type_region = (324, 3, 111, 692)

''' def w_sell():
    'white sell type'
    xt, yt = pyautogui.locateCenterOnScreen('w_sell.png', region=type_region)
    xc, yc = pyautogui.locateCenterOnScreen('w_close.png')
    pyautogui.moveTo(xt, yt)
    pyautogui.moveTo(xc, None)
    pyautogui.click()

def g_sell():
    'grey sell type'
    xt, yt = pyautogui.locateCenterOnScreen('g_sell.png', region=type_region)
    xc, yc = pyautogui.locateCenterOnScreen('g_close.png')
    pyautogui.moveTo(xt, yt)
    pyautogui.moveTo(xc, None)
    pyautogui.click()

def h_sell():
    'hilighted sell type'
    xt, yt = pyautogui.locateCenterOnScreen('h_sell.png', region=type_region)
    xc, yc = pyautogui.locateCenterOnScreen('h_close.png')
    pyautogui.moveTo(xt, yt)
    pyautogui.moveTo(xc, None)
    pyautogui.click()

def w_buy():
    'white buy type'
    xt, yt = pyautogui.locateCenterOnScreen('w_buy.png', region=type_region)
    xc, yc = pyautogui.locateCenterOnScreen('w_close.png')
    pyautogui.moveTo(xt, yt)
    pyautogui.moveTo(xc, None)
    pyautogui.click()

def g_buy():
    'grey buy type'
    xt, yt = pyautogui.locateCenterOnScreen('g_buy.png', region=type_region)
    xc, yc = pyautogui.locateCenterOnScreen('g_close.png')
    pyautogui.moveTo(xt, yt)
    pyautogui.moveTo(xc, None)
    pyautogui.click()

def h_buy():
    'hilighted buy type'
    xt, yt = pyautogui.locateCenterOnScreen('h_buy.png', region=type_region)
    xc, yc = pyautogui.locateCenterOnScreen('h_close.png')
    pyautogui.moveTo(xt, yt)
    pyautogui.moveTo(xc, None)
    pyautogui.click() '''


order_type = raw_input('what type of order do you want to close? ')

next = int(raw_input('How many orders do you want to close? '))

for i in range(0, next):
    if order_type == 'sell' and pyautogui.locateCenterOnScreen('w_sell.png', region=type_region) is not None:
        xt, yt = pyautogui.locateCenterOnScreen('w_sell.png', region=type_region)
        xc, yc = pyautogui.locateCenterOnScreen('w_close.png')
        pyautogui.moveTo(xt, yt)
        pyautogui.moveTo(xc, None)
        pyautogui.click()
        print 'closed w_sell'
    elif order_type == 'sell' and pyautogui.locateCenterOnScreen('g_sell.png', region=type_region) is not None:
        xt, yt = pyautogui.locateCenterOnScreen('g_sell.png', region=type_region)
        xc, yc = pyautogui.locateCenterOnScreen('g_close.png')
        pyautogui.moveTo(xt, yt)
        pyautogui.moveTo(xc, None)
        pyautogui.click()
        print 'closed g_sell'
    elif order_type == 'sell' and pyautogui.locateCenterOnScreen('h_sell.png', region=type_region) is not None:
        xt, yt = pyautogui.locateCenterOnScreen('h_sell.png', region=type_region)
        xc, yc = pyautogui.locateCenterOnScreen('h_close.png')
        pyautogui.moveTo(xt, yt)
        pyautogui.moveTo(xc, None)
        pyautogui.click()
        print 'closed h_sell'
    elif order_type == 'buy' and pyautogui.locateCenterOnScreen('w_buy.png', region=type_region) is not None:
        xt, yt = pyautogui.locateCenterOnScreen('w_buy.png', region=type_region)
        xc, yc = pyautogui.locateCenterOnScreen('w_close.png')
        pyautogui.moveTo(xt, yt)
        pyautogui.moveTo(xc, None)
        pyautogui.click()
        print 'closed w_buy'
    elif order_type == 'buy' and pyautogui.locateCenterOnScreen('g_buy.png', region=type_region) is not None:
        xt, yt = pyautogui.locateCenterOnScreen('g_buy.png', region=type_region)
        xc, yc = pyautogui.locateCenterOnScreen('g_close.png')
        pyautogui.moveTo(xt, yt)
        pyautogui.moveTo(xc, None)
        pyautogui.click()
        print 'closed g_buy'
    elif order_type == 'buy' and pyautogui.locateCenterOnScreen('h_buy.png', region=type_region) is not None:
        xt, yt = pyautogui.locateCenterOnScreen('h_buy.png', region=type_region)
        xc, yc = pyautogui.locateCenterOnScreen('h_close.png')
        pyautogui.moveTo(xt, yt)
        pyautogui.moveTo(xc, None)
        pyautogui.click()
        print 'closed h_buy'
    else:
        print 'please specify a different order type.'

''' if next.isdigit == True:
   n_interval = int(next)
   for i in range(0, n_interval):
       if order_type == 'sell':
           close_sell()
       elif order_type == 'buy':
           close_buy()
       else:
           print 'please specify order type.'
elif next == 'all' or next == 'All' or next == 'ALL':
   sell_list = list(pyautogui.locateAllOnScreen('w_sell.png'))+list(pyautogui.locateAllOnScreen('g_sell.png'))+list(pyautogui.locateAllOnScreen('h_sell.png'))
   buy_list = list(pyautogui.locateAllOnScreen('w_buy.png'))+list(pyautogui.locateAllOnScreen('g_buy.png'))+list(pyautogui.locateAllOnScreen('h_buy.png'))
    for i in sell_list:
        if order_type == 'sell':
            close_sell()
        elif order_type == 'buy':
            close_buy()
        else:
            print 'please specify order type.'

else:
    print 'please enter a number or \'all\' for all orders'
 '''