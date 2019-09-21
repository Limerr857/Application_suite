from tkinter import *
from tkinter.ttk import *
import random

  # Variables:
global temp
temp = ""
global temp2
temp2 = []


def begin():
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "What sort of names do you want to generate?").pack(side = TOP)
    btn2 = Button(root, text = "Company names", command = Company).pack(fill=X)
    #btn3 = Button(root, text = "Human names", command = Boring).pack(fill=X)
    btn4 = Button(root, text = "Robot names", command = Robot).pack(fill=X)
    #btn5 = Button(root, text = "Country names", command = Bank).pack(fill=X)


def Company():
    for widget in root.winfo_children():
        widget.destroy()
    btn1 = Button(root, text = "Generate!", command = Company1).pack()
    btn2 = Button(root, text = "Generate 10!", command = Company2).pack()
    txt1 = Text(root, height = 10, wrap = WORD)
    txt1.insert(1.0, temp2)
    txt1.pack()
    txt1.configure(bg=root.cget('bg'), relief=FLAT)  # These two might be useless, but I can't be bothered to check
    btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)
def Companycalc():
    # TODO: Add more names
    # Setup
    listA = ["United", "Wholesome", "Micro", "Giant"]
    listB = ["Foods", "Industries", "Engineering", "Technology", "Games"]
    listC = ["Ltd.", "Corp.", "Inc.", ""]

    listAlen = len(listA)
    listBlen = len(listB)
    listClen = len(listC)

    for i in range(times):
        # Generation
        tempA = listA[random.randint(0, listAlen-1)]
        tempB = listB[random.randint(0, listBlen-1)]
        tempC = listC[random.randint(0, listClen-1)]

        global temp2
        temp = tempA + " " + tempB + " " + tempC
        temp2.append(temp)
    temp2 = "\n".join(temp2)
    Company()
def Company1():
    global temp2
    temp2 = []
    global times
    times = 1
    Companycalc()
def Company2():
    global temp2
    temp2 = []
    global times
    times = 10
    Companycalc()


def Robot():
    for widget in root.winfo_children():
        widget.destroy()
    btn1 = Button(root, text = "Generate!", command = Robot1).pack()
    btn2 = Button(root, text = "Generate 10!", command = Robot2).pack()
    txt1 = Text(root, height = 10, wrap = WORD)
    txt1.insert(1.0, temp2)
    txt1.pack()
    txt1.configure(bg=root.cget('bg'), relief=FLAT)  # These two might be useless, but I can't be bothered to check
    btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)
def Robot1():
    global temp2
    temp2 = []
    global times
    times = 1
    Robotcalc()
def Robot2():
    global temp2
    temp2 = []
    global times
    times = 10
    Robotcalc()
def Robotcalc():
    # TODO: Add more names
    # Setup
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = str.upper(alphabet_lower)

    for i in range(times):
        # Generation
        rand = random.randint(0, 2)
        if rand == 0:
            tempA = str(random.randint(1000, 9999))
            tempB = alphabet_lower[random.randint(0, len(alphabet_lower)-1)]
            tempC = str(random.randint(1, 1000))

            temp = tempA + tempB + tempC
        elif rand == 1:
            tempA = alphabet_lower[random.randint(0, len(alphabet_lower)-1)]
            tempB = alphabet_upper[random.randint(0, len(alphabet_upper)-1)]
            tempC = str(random.randint(1000, 9999))
            tempD = alphabet_upper[random.randint(0, len(alphabet_upper)-1)]
            tempE = str(random.randint(1, 1000))

            temp = tempA + tempB + tempC + tempD + tempE
        elif rand == 2:
            tempA = alphabet_upper[random.randint(0, len(alphabet_upper)-1)]
            tempB = str(random.randint(0, 9))
            tempC = alphabet_upper[random.randint(0, len(alphabet_upper)-1)]
            tempD = str(random.randint(0, 9))

            temp = tempA + tempB + tempC + tempD
        else:
            print("error! 108")

        global temp2
        temp2.append(temp)
    temp2 = "\n".join(temp2)
    Robot()

root = Toplevel()
root.geometry("400x300")
root.title("NameGenerator")
btn1 = Button(root, text = "Generate me some names!", command = begin)
btn1.pack()
root.mainloop()