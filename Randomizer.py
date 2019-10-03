
from tkinter import *
from tkinter.ttk import *
import random

temp = ""
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ.,/_-+=():'*?!1234567890&$€#@^~;"
alen = len(alphabet)
sylen = len(symbols)

def begin():
    global temp
    temp = ""
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "What do you want to do?").pack(side = TOP)
    btn2 = Button(root, text = "Random numbers!", command = Num).pack(fill=X)
    btn3 = Button(root, text = "Random letters!", command = Let).pack(fill=X)
    btn4 = Button(root, text = "Random symbols!", command = Sym).pack(fill=X)
    btn5 = Button(root, text = "Random numbers and symbols!", command = NumSym).pack(fill=X)
    #btn6 = Button(root, text = "Randomize order!", command = RanOrd).pack(fill=X)
    btn7 = Button(root, text = "Shuffle string!", command = ShuStr).pack(fill=X)

def Num():
    global ent1
    for widget in root.winfo_children():
        widget.destroy()
    txt1 = Text(root, height = 8, wrap = WORD) 
    txt1.insert(1.0, temp)
    btn1 = Button(root, text="Give me those numbers!", command=Num2)
    btn2 = Button(root, text="Go back", command=begin)
    lbl2 = Label(root, text="length:")
    ent1 = Entry(root)
    txt1.pack(side=TOP)
    btn2.pack(side=BOTTOM)
    btn1.pack(side=BOTTOM)
    lbl2.pack()
    ent1.pack()
def Num2():
    global temp
    temp2 = ent1.get()
    try:
        temp2 = int(temp2)
        temp2 -= 1
        failed = False
    except:
        temp = "Only integers"
        failed = True
    if failed == False:
        if temp2 > 10000:
            temp = "Only numbers below 10000"
        else:
            temp = random.randint((10 ** temp2), (10**(temp2+1))-1)
    Num()

def Let():
    global ent1
    for widget in root.winfo_children():
        widget.destroy()
    txt1 = Text(root, height = 8, wrap = WORD) 
    txt1.insert(1.0, temp)
    btn1 = Button(root, text="Give me those letters!", command=Let2)
    btn2 = Button(root, text="Go back", command=begin)
    lbl2 = Label(root, text="length:")
    ent1 = Entry(root)
    txt1.pack(side=TOP)
    btn2.pack(side=BOTTOM)
    btn1.pack(side=BOTTOM)
    lbl2.pack()
    ent1.pack()
def Let2():
    global temp
    temp2 = ent1.get()
    try:
        temp2 = int(temp2)
        failed = False
    except:
        temp = "Only integers"
        failed = True
    if failed == False:
        if temp2 > 10000:
            temp = "Only numbers below 10000"
        else:
            temp = []
            for i in range(temp2):
                temp3 = random.randint(0, alen)
                temp3 = alphabet[temp3-1]
                temp.append(temp3)
            temp = "".join(temp)
    Let()

def Sym():
    global ent1
    for widget in root.winfo_children():
        widget.destroy()
    txt1 = Text(root, height = 8, wrap = WORD) 
    txt1.insert(1.0, temp)
    btn1 = Button(root, text="Give me those symbols!", command=Sym2)
    btn2 = Button(root, text="Go back", command=begin)
    lbl2 = Label(root, text="length:")
    ent1 = Entry(root)
    txt1.pack(side=TOP)
    btn2.pack(side=BOTTOM)
    btn1.pack(side=BOTTOM)
    lbl2.pack()
    ent1.pack()
def Sym2():
    global temp
    temp2 = ent1.get()
    try:
        temp2 = int(temp2)
        failed = False
    except:
        temp = "Only integers"
        failed = True
    if failed == False:
        if temp2 > 10000:
            temp = "Only numbers below 10000"
        else:
            temp = []
            for i in range(temp2):
                temp3 = random.randint(0, sylen)
                temp3 = symbols[temp3-1]
                temp.append(temp3)
            temp = "".join(temp)
    Sym()

def NumSym():
    global ent1
    for widget in root.winfo_children():
        widget.destroy()
    txt1 = Text(root, height = 8, wrap = WORD) 
    txt1.insert(1.0, temp)
    btn1 = Button(root, text="Give me those numbers and symbols!", command=NumSym2)
    btn2 = Button(root, text="Go back", command=begin)
    lbl2 = Label(root, text="length:")
    ent1 = Entry(root)
    txt1.pack(side=TOP)
    btn2.pack(side=BOTTOM)
    btn1.pack(side=BOTTOM)
    lbl2.pack()
    ent1.pack()
def NumSym2():
    global temp
    temp2 = ent1.get()
    try:
        temp2 = int(temp2)
        failed = False
    except:
        temp = "Only integers"
        failed = True
    if failed == False:
        if temp2 > 10000:
            temp = "Only numbers below 10000"
        else:
            temp = []
            for i in range(temp2):
                temp3 = random.randint(0, 1)
                if temp3 == 0:
                    temp3 = random.randint(0, sylen)
                    temp3 = symbols[temp3-1]
                    temp.append(temp3)
                else:
                    temp3 = str(random.randint(0, 9))
                    temp.append(temp3)
            temp = "".join(temp)
    NumSym()

def ShuStr():
    global ent1
    global temp
    for widget in root.winfo_children():
        widget.destroy()
    txt1 = Text(root, height = 8, wrap = WORD) 
    txt1.insert(1.0, temp)
    btn1 = Button(root, text="Shuffle letters!", command=ShuStr2)
    btn2 = Button(root, text="Go back", command=begin)
    lbl2 = Label(root, text="Shuffle this:")
    ent1 = Entry(root)
    txt1.pack(side=TOP)
    btn2.pack(side=BOTTOM)
    btn1.pack(side=BOTTOM)
    lbl2.pack()
    ent1.pack()
def ShuStr2():
    global ent1
    global temp
    temp2 = ent1.get()
    temp2 = list(temp2)
    random.shuffle(temp2)
    temp = "".join(str(e) for e in temp2)
    ShuStr()


root = Toplevel()
root.geometry("400x300")
root.title("NameGenerator")
btn1 = Button(root, text = "Randomize me something!", command = begin)
btn1.pack()
root.mainloop()