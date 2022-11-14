from pyautogui import *
import time as tm


keyDown('alt')
press('tab')
keyUp('alt')
tm.sleep(2)
print(position())