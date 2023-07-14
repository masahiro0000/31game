import PySimpleGUI as sg
import random
sg.theme("DarkBrown3")

layout=[[sg.T("let's 31 game!")],
[sg.Im(k="img1"),sg.T(k="txt1")],
[sg.T("enter number",k="txt2")],
[sg.I("1",k="in1",size=(15)),
 sg.B("enter",k="btn",bind_return_key=True)]]

win=sg.Window("31 game",layout,font=(None,14),finalize=True)

def getnextnums(n):
    global nextnums,choicemsg
    nextnums=list(range(n+1,min(32,n+4)))
    choicemsg=f"enter {nextnums}"
    win["txt2"].update(choicemsg)

def question():
    global playflag
    getnextnums(0)
    win["txt1"].update("let's game")
    win["img1"].update("futaba.png")
    playflag=True

def com_turn(comnum):
    keynums=[2,6,10,14,18,22,26,30]
    getnextnums(comnum)
    for n in nextnums:
        if n in keynums:
            comnum=n
    if random.randint(0,1)>0:
        comnum=nextnums[0]
    win["txt1"].update(f"I'd like {comnum}")
    getnextnums(comnum)

def my_turn():
    global playflag
    if v["in1"].isdecimal()==False:
        win["txt1"].update("enter number")
    else:
        mynum=int(v["in1"])
        if mynum in nextnums:
            if mynum==31:
                win["txt1"].update("you lose")
                win["img1"].update("futaba0.png")
                win["txt2"].update("push enter button, and play")
                playflag=False
            elif mynum==30:
                win["txt1"].update("you win. congratulations")
                win["img1"].update("futaba0.png")
                win["txt2"].update("push enter button, and play")
                playflag=False
            else:
                com_turn(mynum)
        else:
            win["txt1"].update(choicemsg)


question()

while True:
    e,v=win.read()
    if playflag==False:
        question()
    else:
        my_turn()
    if e==None:
        break

win.close()
