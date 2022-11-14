from pyautogui import *
import time as tm
from PySimpleGUI import PySimpleGUI as sg
import AppRun


sg.theme('Reddit')
layout = [
    [sg.Text('Digite o nome do contato em que deseja mandar mensagem: '),sg.Input(key = 'nome')],
    [sg.Text('Mensage que deseja enviar: '),sg.Input(key = 'msg')],
    [sg.Text('Quantidade de vezes que deseja mandar: '),sg.Input(key = "vezes")],
    [sg.Button('Enviar')]
]

janela = sg.Window('Tela de login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enviar':
        AppRun.AppRun()


