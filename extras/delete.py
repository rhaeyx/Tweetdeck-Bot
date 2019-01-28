# Delete all scheduled tweets.

from pyautogui import locateOnScreen, click, center
from time import sleep

try:
    while True:
        click(center(locateOnScreen('../images/delete-icon.png')))
        sleep(1)
        click(center(locateOnScreen('../images/ok-btn.png')))
except:
    print('Done.')
