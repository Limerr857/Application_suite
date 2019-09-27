
from tkinter import *
from tkinter.ttk import *
import random

temp = ""

def begin():
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "What do you want to do?").pack(side = TOP)
    btn2 = Button(root, text = "Random numbers!", command = Num).pack(fill=X)
    #btn3 = Button(root, text = "Random letters!, command = Human).pack(fill=X)
    #btn4 = Button(root, text = "Random numbers and letters", command = Robot).pack(fill=X)
    #btn5 = Button(root, text = "Country names", command = Country).pack(fill=X)

def Num():
    global ent1
    for widget in root.winfo_children():
        widget.destroy()
    txt1 = Text(root, height = 8, wrap = WORD) 
    txt1.insert(1.0, temp)
    btn1 = Button(root, text="Give me those numbers!", command=Num2)
    lbl2 = Label(root, text="length:")
    ent1 = Entry(root)
    txt1.pack(side=TOP)
    btn1.pack(side=BOTTOM)
    lbl2.pack()
    ent1.pack()

def Num2():
    global temp
    temp2 = ent1.get()
    try:
        temp2 = int(temp2)
        temp2 -= 1
        if temp2 > 10000:
            badtemp = temp2
            temp = "Only numbers below 10000"
            Num()
    except:
        temp = "Only integers"
        Num()
    temp = random.randint((10 ** temp2), (10**(temp2+1))-1)
    Num()

root = Toplevel()
root.geometry("400x300")
root.title("NameGenerator")
btn1 = Button(root, text = "Randomize me something!", command = begin)
btn1.pack()
root.mainloop()