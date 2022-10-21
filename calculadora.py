import PySimpleGUI as sg

def criarjanela(theme):
    sg.theme(theme)
    sg.set_options(font='Arial 14', button_element_size = (6,3))

    tamanhobotao = (6,3)

    layout = [
    [sg.Text(0,
    font = 'Arial 28',
    justification = 'right',
    expand_x = True,
    pad = (10, 20),
    right_click_menu = temamenu,
    key = 'texto')
    ],
    

    [sg.Button('Limpar',
    expand_x = True),
    sg.Button('**',
    expand_x =True)],

    [sg.Button(7, size = tamanhobotao),
    sg.Button(8, size = tamanhobotao),
    sg.Button(9, size = tamanhobotao),
    sg.Button('*', size = tamanhobotao)],

    [sg.Button(4, size = tamanhobotao),
    sg.Button(5, size = tamanhobotao),
    sg.Button(6, size = tamanhobotao),
    sg.Button('/', size = tamanhobotao)],

    [sg.Button(1, size = tamanhobotao),
    sg.Button(2, size = tamanhobotao),
    sg.Button(3, size = tamanhobotao),
    sg.Button('-', size = tamanhobotao)],

    [sg.Button(0, expand_x = True),
    sg.Button('.', size = tamanhobotao),
    sg.Button('+', size = tamanhobotao),
    sg.Button('=', size = tamanhobotao)]
]
    return sg.Window('Calculadora', layout)

temamenu = ['menu', ['LightGrey1', 'dark', 'DarkGray8', 'random']]

window = criarjanela('LightGrey1')

numeroatual = []
fulloperacao = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in temamenu[1]:
        window.close()
        window = criarjanela(event)
        

    if event in ['0', '1', '2', '3', '4','5', '6', '7', '8', '9', '.']:
        numeroatual.append(event)
        numstring = ''.join(numeroatual)
        window['texto'].update(numstring)

    if event in ['+', '-', '*', '/', '**']:
        fulloperacao.append(''.join(numeroatual))
        numeroatual = []
        fulloperacao.append(event)
        window['texto'].update('')

    if event == '=':
        fulloperacao.append(''.join(numeroatual))
        resultado = eval(' '.join(fulloperacao))
        window['texto'].update(resultado)
        fulloperacao = []

    if event == 'Limpar':
        numeroatual = []
        fulloperacao = []
        window['texto'].update('')




window.close()    
