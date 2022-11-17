import PySimpleGUI as sg
def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def dv(a,b):
  return a/b

layout=[[sg.Text("Enter 1st Number"),sg.Input(key="a")],
         [sg.Text("Enter 2nd Number"),sg.Input(key="b")],
        [sg.Listbox(values=["Addition","Subtraction","Multiplication","Division"],s=30,key='c')],
        [sg.Exit(),sg.Button("Calculate",s=15,button_color="tomato")]]

window=sg.Window("Calculator", layout)


while True:
    event,values=window.read()
    print(event,values)
    if event in (sg.WINDOW_CLOSED,"Exit"):
        break
    if event=="Calculate":
        for i in values['c']:
            if i=='Addition':
                output=(add(int(values['a']),int(values['b'])))
                sg.popup_no_titlebar(output)
            elif i=='Subtraction':
                output=(sub(int(values['a']),int(values['b'])))
                sg.popup_no_titlebar(output)
            elif i=='Multiplication':
                output=(mul(int(values['a']),int(values['b'])))
                sg.popup_no_titlebar(output)
            elif i=='Division':
                output=(dv(int(values['a']),int(values['b'])))
                sg.popup_no_titlebar(output)

window.close()
