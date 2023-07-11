import PySimpleGUI as sg
from PIL import Image
import io
sg.theme("DarkBrown3")

layout=[[sg.B("open file",k="btn1"),sg.T(k="txt")],
        [sg.B("save file",k="btn2")],
        [sg.Im(k="img")]]

win=sg.Window("change to monoimage",layout,size=(320,400))

def loadimage():
    global Image
    loadname=sg.popup_get_file("select image file")
    if not loadname:
        return
    try:
        img=Image.open(loadname).convert("L")
        img2=img.copy()
        img2.thumbnail((300,300))
        bio=io.BytesIO()
        img2.save(bio,format="PNG")
        win["img"].update(data=bio.getvalue())
        win["txt"].update(loadname)
    except:
        win["img"].update()
        win["txt"].update("lose")
    
    img=None

    def saveimage():
        if img==None:
            return
        savename=sg.popup_get_file("save as png",
                                   save_as=True)
        if not savename:
            sg.PopupTimed("enter png image name")
            return
        if savename.endswith(".png")==False:
            savename=savename+".png"
        try:
            img.save(savename)
            win["txt"].update(savename+"save")
        except:
            win["txt"].update("lose")

while True:
    e,v=win.read()
    if e=="btn1":
        loadimage()
    if e=="btn2":
        saveimage()
    if e==None:
        break
win.close()