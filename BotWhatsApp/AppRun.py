from pyautogui import *
import time as tm
import main
from PySimpleGUI import PySimpleGUI as sg



def AppRun():
        c=0
        press("win")
        write("whatsapp")
        press("enter")
        tm.sleep(2.5)
        click(x = 111, y = 111)
        write(main.valores['nome'])
        click(x = 239, y = 200)
        click(x = 146, y = 178)
        click(x = 722, y = 743)
        tm.sleep(1.4)
        while c < int(main.valores['vezes']):
            write(main.valores['msg'])
            press('enter')
            c = c + 1
        write("©bySorriso")
        press('enter')
        print("©bySorriso")