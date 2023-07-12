import PySimpleGUI as sg
import random
from PIL import Image 

sg.theme("DarkBrown3")

image_path="2.png"
img=Image.open(image_path)
img.thumbnail((300,300))

layout=[[sg.T("let's omikuji")],
    [sg.Image(data=img.tobytes())],
    [sg.T(k="txt")],
    [sg.B("do omikuji",k="btn")]]

win=sg.Window("omikuji game",layout,font=(None,14))

def omikuji():
    kuji=["daikiti","tyukiti","syokiti","kyo"]
    result=random.choice(kuji)
    txt=f"result is {result}"
    win["txt"].update(txt)

while True:
    e,v=win.read()
    if e=="btn":
        omikuji()
    if e==None:
        break

win.close()
