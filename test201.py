import PySimpleGUI as sg

layout=[[sg.Input("hutaba",key="in")],
        [sg.Button("execute",key="btn")],
        [sg.Text(key="txt")]]
window=sg.Window("test",layout)

def execute():
    txt="hello,"+values["in"]
    window["txt"].update(txt)

while True:
    event,values=window.read()
    if event=="btn":
        execute()
    if event==None:
        break
window.close()