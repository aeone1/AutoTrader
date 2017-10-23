'''new close script does not take close.png coordinates
but uses a manual pixel move. And there is a One(1)
scratch that Two(2) second delay ouch...
But this depends on the hardware and network speed.
This allows MT4 to close a trade, re-arrange orders and
allows time before the next for loop runs.
This slows the program but it'll do for now.
wow!!! On the contrary, since there's only one image search for every for loop
this makes the program faster!
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
        print '\ng_slell = ', j
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
        print '\nh_slell = ', j
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
