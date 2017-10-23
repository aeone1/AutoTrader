'''checks the screen and prints buy or sell
whenever price is on thier respective levels
'''
import pyautogui

chart_region = (2, 97, 1680, 300)

def buy_signal():
    '''All buy signals'''
    bt = pyautogui.locateOnScreen('bt.png', region=chart_region)
    #bt_blue = pyautogui.locateOnScreen('bt_blue.png', region=chart_region)
    #bt_green = pyautogui.locateOnScreen('bt_green.png')

    #buy_s = (bt)
    return bt

def sell_signal():
    '''All sell signals'''
    st = pyautogui.locateOnScreen('st.png', region=chart_region)
    #st_blue = pyautogui.locateOnScreen('st_blue.png')
    #st_green = pyautogui.locateOnScreen('st_green.png', region=chart_region)

    #sell_s = (st)
    return st

def in_level():
    '''if in level'''
    in_lev = pyautogui.locateOnScreen('in_level.png', region=chart_region)

    return in_lev

def sup():
    '''supply level'''
    supply = pyautogui.locateOnScreen('sup.png', region=chart_region)
    return supply

def dem():
    '''Demand level'''
    demand = pyautogui.locateOnScreen('dem.png', region=chart_region)
    return demand

count = 0

while True:
    b = buy_signal()
    print 'buy_signal ', b
    s = sell_signal()
    print 'sell_signal ', s
    i = in_level()
    print 'in_level ', i
    su = sup()
    print 'supply ', su
    de = dem()
    print 'demand ', de
    if b != (None) and b < i and su is (None):
        print 'buy_signal ', buy_signal(), in_level()
        print '\nbt\n'
    elif s != (None) and s < i and de is (None):
        print 'sell_signal ', sell_signal(), in_level()
        print '\nst\n'
    elif i != (None) and b is (None) and s is (None):
        print 'in_level', in_level()
        print '\nNothing to do.\n'
    elif i != (None) and i < b:
        print 'in_level < buy_signal', in_level(), buy_signal()
        print '\nst\n'
    elif i != (None) and i < s:
        print 'in_level < sell_signal', in_level(), sell_signal()
        print '\nbt\n'
    elif b != (None) and su is (None):
        print 'buy_signal ', buy_signal()
        print '\nbt\n'
    elif s != (None) and de is (None):
        print 'sell_signal', sell_signal()
        print '\nst\n'
    elif b != (None) and su != (None):
        print '\nClosing all Sell.'
        print '\nall_sell\n'
    elif s != (None) and de != (None):
        print '\nClosing all Buy.'
        print '\nall_buy\n'
    else:
        print '.........'
        print count
        count += 1
