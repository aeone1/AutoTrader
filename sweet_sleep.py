'''Nisi Dominsus frustra.'''
import time
import pyautogui

type_region = (324, 3, 111, 692)
chart_region = (2, 97, 1680, 300)

def close_sell():
    '''closes all orders of type sell'''
    def all_sell():
        '''list all sells'''
        w_sell = list(pyautogui.locateAllOnScreen('w_sell.png', region=type_region))
        g_sell = list(pyautogui.locateAllOnScreen('g_sell.png', region=type_region))
        h_sell = list(pyautogui.locateAllOnScreen('h_sell.png', region=type_region))

        all_sells = list(w_sell + g_sell + h_sell)
        return all_sells

    while all_sell() != []:
        print 'all sell', all_sell()
        for j in list(pyautogui.locateAllOnScreen('w_sell.png', region=type_region)):
            print '\nw_sell = ', j
            xt, yt, w, l = j
            pyautogui.moveTo(xt, yt, duration=0.02)
            print 'moved to %r, %r' % (xt, yt)
            pyautogui.moveRel(957, None, duration=0.02)
            print 'moved to %r, %r' % (xt+957, yt)
            pyautogui.click(duration=0.02)
            print 'clicked on', pyautogui.position()
            time.sleep(2)
            print 'slept for 2 seconds'
            break

        for j in list(pyautogui.locateAllOnScreen('g_sell.png', region=type_region)):
            print '\ng_sell = ', j
            xt, yt, w, l = j
            pyautogui.moveTo(xt, yt, duration=0.02)
            print 'moved to %r, %r' % (xt, yt)
            pyautogui.moveRel(957, None, duration=0.02)
            print 'moved to %r, %r' % (xt+957, yt)
            pyautogui.click(duration=0.02)
            print 'clicked on', pyautogui.position()
            time.sleep(2)
            print 'slept for 2 seconds'
            break

        for j in list(pyautogui.locateAllOnScreen('h_sell.png', region=type_region)):
            print '\nh_sell = ', j
            xt, yt, w, l = j
            pyautogui.moveTo(xt, yt, duration=0.02)
            print 'moved to %r, %r' % (xt, yt)
            pyautogui.moveRel(950, 1, duration=0.02)
            print 'moved to %r, %r' % (xt+950, yt+1)
            pyautogui.click(duration=0.02)
            print 'clicked on', pyautogui.position()
            time.sleep(2)
            print 'slept for 2 seconds'
            break

        continue

    print 'all sell = ', all_sell()
    print 'no more sell orders'

def close_buy():
    '''closes all orders of type buy'''
    def all_buy():
        '''creates a list of all buy orders'''
        w_buy = list(pyautogui.locateAllOnScreen('w_buy.png', region=type_region))
        g_buy = list(pyautogui.locateAllOnScreen('g_buy.png', region=type_region))
        h_buy = list(pyautogui.locateAllOnScreen('h_buy.png', region=type_region))

        all_sells = list(w_buy + g_buy + h_buy)
        return all_sells

    while all_buy() != []:
        print 'all buy', all_buy()
        for j in list(pyautogui.locateAllOnScreen('w_buy.png', region=type_region)):
            print '\nw_buy = ', j
            xt, yt, w, l = j
            pyautogui.moveTo(xt, yt, duration=0.02)
            print 'moved to %r, %r' % (xt, yt)
            pyautogui.moveRel(957, None, duration=0.02)
            print 'moved to %r, %r' % (xt+957, yt)
            pyautogui.click(duration=0.02)
            print 'clicked on', pyautogui.position()
            time.sleep(2)
            print 'slept for 2 seconds'
            break

        for j in list(pyautogui.locateAllOnScreen('g_buy.png', region=type_region)):
            print '\ng_buy = ', j
            xt, yt, w, l = j
            pyautogui.moveTo(xt, yt, duration=0.02)
            print 'moved to %r, %r' % (xt, yt)
            pyautogui.moveRel(957, None, duration=0.02)
            print 'moved to %r, %r' % (xt+957, yt)
            pyautogui.click(duration=0.02)
            print 'clicked on', pyautogui.position()
            time.sleep(2)
            print 'slept for 2 seconds'
            break

        for j in list(pyautogui.locateAllOnScreen('h_buy.png', region=type_region)):
            print '\nh_buy = ', j
            xt, yt, w, l = j
            pyautogui.moveTo(xt, yt, duration=0.02)
            print 'moved to %r, %r' % (xt, yt)
            pyautogui.moveRel(950, 1, duration=0.02)
            print 'moved to %r, %r' % (xt+950, yt+1)
            pyautogui.click(duration=0.02)
            print 'clicked on', pyautogui.position()
            time.sleep(2)
            print 'slept for 2 seconds'
            break

        continue

    print 'all buys = ', all_buy()
    print 'no more buy orders'

def buy_signal():
    '''All buy signals'''
    bt = pyautogui.locateOnScreen('bt.png', region=chart_region)
    return bt

def sell_signal():
    '''All sell signals'''
    st = pyautogui.locateOnScreen('st.png', region=chart_region)
    return st

def in_level():
    '''if in level'''
    in_lev = pyautogui.locateOnScreen('in_level.png', region=chart_region)
    return in_lev

def sup():
    '''supply level'''
    supply = pyautogui.locateOnScreen('sup.png')#, region=chart_region)
    return supply

def dem():
    '''Demand level'''
    demand = pyautogui.locateOnScreen('dem.png')#, region=chart_region)
    return demand

def open_buy():
    '''Allocate open buy coordinates'''
    op_buy = pyautogui.locateOnScreen('open_buy.png')#, region=chart_region)
    return op_buy

def open_sell():
    '''Allocate open sell cordinates ie check if there's an order on the level b4 placing a new one'''
    op_sell = pyautogui.locateOnScreen('open_sell.png')#, region=chart_region)
    return op_sell


count = 0

while True:
    i = in_level()
    print 'in_level ', i

    b = buy_signal()
    print 'buy_signal ', b

    s = sell_signal()
    print 'sell_signal ', s

    su = sup()
    print 'supply ', su

    de = dem()
    print 'demand ', de

    o_b = open_buy()
    print 'open_buy ', o_b

    o_s = open_sell()
    print 'open_sell ', o_s

    if b != (None) and b < i and su is (None) and o_b is (None):
        print 'buy_signal ', buy_signal(), in_level()
        print '\nbt\n'
        pyautogui.click(170, 139)
        print 'clicked on buy ', pyautogui.position()
    elif s != (None) and s < i and de is (None) and o_s is (None):
        print 'sell_signal ', sell_signal(), in_level()
        print '\nst\n'
        pyautogui.click(29, 139)
        print 'clicked on sell ', pyautogui.position()
    elif i != (None) and b is (None) and s is (None):
        print 'in_level', in_level()
        print '\nNothing to do.\n'
    elif i != (None) and i < b and o_s is (None):
        print 'in_level < buy_signal', in_level(), buy_signal()
        print '\nst\n'
        pyautogui.click(29, 139)
        print 'clicked on sell ', pyautogui.position()
    elif i != (None) and i < s and o_b is (None):
        print 'in_level < sell_signal', in_level(), sell_signal()
        print '\nbt\n'
        pyautogui.click(170, 139)
        print 'clicked on buy ', pyautogui.position()
    elif b != (None) and su is (None) and o_b is (None):
        print 'buy_signal ', buy_signal()
        print '\nbt\n'
        pyautogui.click(170, 139)
        print 'clicked on buy ', pyautogui.position()
    elif s != (None) and de is (None) and o_s is (None):
        print 'sell_signal', sell_signal()
        print '\nst\n'
        pyautogui.click(29, 139)
        print 'clicked on sell ', pyautogui.position()
    elif b != (None) and su != (None) and s is (None):
        print '\nClosing all Sell.'
        print '\nall_sell\n'
        close_sell()
        print 'closed all sell.'
    elif s != (None) and de != (None) and b is (None):
        print '\nClosing all Buy.'
        print '\nall_buy\n'
        close_buy()
        print 'closed all buy.'
    else:
        print '.........',
        print count
        count += 1
