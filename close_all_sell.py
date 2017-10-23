'''closes all sell trades'''
import pyautogui

type_region = (324, 3, 111, 692)

w_sell = pyautogui.locateCenterOnScreen('w_sell.png', region=type_region)
g_sell = pyautogui.locateCenterOnScreen('g_sell.png', region=type_region)
h_sell = pyautogui.locateCenterOnScreen('h_sell.png', region=type_region)

while True:
    w_sell = list(pyautogui.locateAllOnScreen('w_sell.png', region=type_region))
    g_sell = list(pyautogui.locateAllOnScreen('g_sell.png', region=type_region))
    h_sell = list(pyautogui.locateAllOnScreen('h_sell.png', region=type_region))

    all_sell = list(w_sell + g_sell + h_sell)

    print all_sell

    while all_sell is not []:

        while True:

            if pyautogui.locateCenterOnScreen('w_sell.png', region=type_region) is not None:
                xt, yt = pyautogui.locateCenterOnScreen('w_sell.png', region=type_region)
                xc, yc = pyautogui.locateCenterOnScreen('w_close.png')
                pyautogui.moveTo(xt, yt)
                pyautogui.moveTo(xc, None)
                pyautogui.click()
                print 'closed w_sell'
            else:
                print 'No more w_sell'

                if pyautogui.locateCenterOnScreen('g_sell.png', region=type_region) is not None:
                    xt, yt = pyautogui.locateCenterOnScreen('g_sell.png', region=type_region)
                    xc, yc = pyautogui.locateCenterOnScreen('g_close.png')
                    pyautogui.moveTo(xt, yt)
                    pyautogui.moveTo(xc, None)
                    pyautogui.click()
                    print 'closed g_sell'
                else:
                    print 'No more g_sell'    
                    
                    if pyautogui.locateCenterOnScreen('h_sell.png', region=type_region) is not None:
                        xt, yt = pyautogui.locateCenterOnScreen('h_sell.png', region=type_region)
                        xc, yc = pyautogui.locateCenterOnScreen('h_close.png')
                        pyautogui.moveTo(xt, yt)
                        pyautogui.moveTo(xc, None)
                        pyautogui.click()
                        print 'closed h_sell'
                        break


    print 'all sell orders closed.'


    break
