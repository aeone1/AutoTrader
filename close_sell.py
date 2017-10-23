'''closes all sell trades
This program works but will crash when;
-An already detected sell (j) 'disappears' when xt, yt is called.
-There is no buy
'''
import time
import pyautogui

type_region = (324, 3, 111, 692)

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
        print '\nw_slell = ', j
        xt, yt = pyautogui.locateCenterOnScreen('w_sell.png', region=type_region)
        print 'xt is %r, yt is %r' % (xt, yt)
        xc, yc = pyautogui.locateCenterOnScreen('w_close.png')
        print 'xc is %r, yc is %r' % (xc, yc)
        pyautogui.moveTo(xt, yt, duration=0.02)
        print 'moved to %r, %r' % (xt, yt)
        pyautogui.moveTo(xc, yt, duration=0.02)
        print 'moved to %r, %r' % (xc, yt)
        pyautogui.click(duration=0.02)
        print 'clicked on', pyautogui.position()
        print 'closed w_sell at y = ', yt
        pyautogui.click(1257, 652, duration=0.02)
        print 'clicked away at ', pyautogui.position()
        time.sleep(0.1)
        print 'slept for 0.1 seconds'
        break

    for j in list(pyautogui.locateAllOnScreen('g_sell.png', region=type_region)):
        print '\ng_sell = ', j
        xt, yt = pyautogui.locateCenterOnScreen('g_sell.png', region=type_region)
        print 'xt is %r, yt is %r' % (xt, yt)
        xc, yc = pyautogui.locateCenterOnScreen('g_close.png')
        print 'xc is %r, yc is %r' % (xc, yc)
        pyautogui.moveTo(xt, yt, duration=0.02)
        print 'moved to %r, %r' % (xt, yt)
        pyautogui.moveTo(xc, yt, duration=0.02)
        print 'moved to %r, %r' % (xc, yt)
        pyautogui.click(duration=0.02)
        print 'clicked on', pyautogui.position()
        print 'closed g_sell at y = ', yt
        pyautogui.click(1257, 652, duration=0.02)
        print 'clicked away at ', pyautogui.position()
        time.sleep(0.1)
        print 'slept for 0.1 seconds'
        break

    for j in list(pyautogui.locateAllOnScreen('h_sell.png', region=type_region)):
        print '\nh_sell = ', j
        xt, yt = pyautogui.locateCenterOnScreen('h_sell.png', region=type_region)
        print 'xt is %r, yt is %r' % (xt, yt)
        xc, yc = pyautogui.locateCenterOnScreen('h_close.png')
        print 'xc is %r, yc is %r' % (xc, yc)
        pyautogui.moveTo(xt, yt, duration=0.02)
        print 'moved to %r, %r' % (xt, yt)
        pyautogui.moveTo(xc, yt, duration=0.02)
        print 'moved to %r, %r' % (xc, yt)
        pyautogui.click(duration=0.02)
        print 'clicked on', pyautogui.position()
        print 'closed h_sell at y = ', yt
        pyautogui.click(1257, 652, duration=0.02)
        print 'clicked away at ', pyautogui.position()
        time.sleep(0.1)
        print 'slept for 0.1 seconds'
        break

    continue

print 'all sell = ', all_sell()
print 'no more sell orders'
