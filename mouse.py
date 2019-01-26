# Mouse locator

import pyautogui
import time
print("Ctrl + C to close")
try:
    while True:
        x, y = pyautogui.position()
        pix = pyautogui.screenshot().getpixel((x,y))
        for_print = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        for_print += ' RGB: (' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(3) + ')'
        print(for_print, end='')
        print('\b' * len(for_print), end='', flush=True)
except KeyboardInterrupt:
    print('\nBye!')
    exit()
