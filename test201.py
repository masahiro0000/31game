import PySimpleGUI as sg
sg.theme("BrightColors")

layout=[[sg.I("hutaba",k="in")],
        [sg.B("execute",k="btn")],
        [sg.T(k="txt")]]
win=sg.Window("test",layout,
            font=(None,14),size=(250,120))

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