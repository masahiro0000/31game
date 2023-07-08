import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout=[[sg.T("abc",size=(30,1),justification="left")],
        [sg.T("abc",size=(30,1),justification="center")],
        [sg.T("abc",size=(30,1),justification="right")]]
win=sg.Window("文字レイアウトテスト",layout,font=(None,14),size=(300,120))

e,v=win.read()
win.close()