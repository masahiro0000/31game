import PySimpleGUI as sg

layout=[[sg.I("hutaba",k="in")],
        [sg.B("execute",k="btn")],
        [sg.T(k="txt")]]
win=sg.Window("test",layout)

def execute():
    txt="hello,"+v["in"]
    win["txt"].update(txt)

while True:
    e,v=win.read()
    if e=="btn":
        execute()
    if e==None:
        break
win.close()