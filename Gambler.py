

from tkinter import *
from tkinter.ttk import *
import time
import random
global money
money = 100
global dept
dept = random.randint(0, 1000000)

def begin():
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "So, how do you want to waste your money today?").pack(side = TOP)
    lbl2 = Label(root, text = "You have {} shmeckles.".format(money)).pack(side = TOP)
    #btn1 = Button(root, text = "Wheel of fortune!", command = Wheel).pack(fill=X)
    btn2 = Button(root, text = "Guesser", command = Guesser).pack(fill=X)
    #btn3 = Button(root, text = "Boring", command = IOTD).pack(fill=X)
    btn4 = Button(root, text = "Waster", command = Waster).pack(fill=X)
    btn5 = Button(root, text = "Bank", command = Bank).pack(fill=X)

def Wheel():
    for widget in root.winfo_children():
        widget.destroy()
    print("hellu")
    btn1 = Button(root, text = "Spin the wheel!", command = Wheel1).pack()
    print("ok")
def Wheel1():
    for widget in root.winfo_children():
        widget.destroy()
    print("yes")
    result = random.randint(0, 99)
    x = 0
    y = 0
    btn1 = Button(root, text = str(result-2)).pack()
    btn2 = Button(root, text = str(result-1)).pack()
    btn3 = Button(root, text = str(result)).pack()
    btn4 = Button(root, text = str(result+1)).pack()
    btn5 = Button(root, text = str(result+2)).pack()
    while x!=3:
        if y==result:
            x += 1
        if y== 100:
            y = 0
        print("1st", y)
        time.sleep(0.01)
        y += 1
    while y!=result:
        for widget in root.winfo_children():
            widget.destroy()
        btn1 = Button(root, text = str(result-2)).pack()
        btn2 = Button(root, text = str(result-1)).pack()
        btn3 = Button(root, text = str(result)).pack()
        btn4 = Button(root, text = str(result+1)).pack()
        btn5 = Button(root, text = str(result+2)).pack()
        if y== 100:
            y = 0
        print("2nd", y)
        time.sleep(0.1)
        y += 1
    for widget in root.winfo_children():
            widget.destroy()
    lbl1 = Label(root, text = "Congratulations, you win.").pack()
    btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)


def Guesser():
    global lock
    lock = False
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "Choose your difficulty. The harder it is, the more money you can lose!\nCost: 10 shmeckles for Easy, after that add 1 shmeckle for each new level.").pack(side = TOP)
    lbl2 = Label(root, text = "You have {} shmeckles.".format(money)).pack(side = TOP)
    btn1 = Button(root, text = "Easy", command = Guesser1).pack()
    btn2 = Button(root, text = "Medium", command = Guesser2).pack()
    btn3 = Button(root, text = "Hard", command = Guesser3).pack()
    btn4 = Button(root, text = "Extreme", command = Guesser4).pack()
    btn5 = Button(root, text = "Ultra", command = Guesser5).pack()
    global x
    global y

def Guesser1():
    global money
    money -= 10
    global x
    global y
    x = 2
    y = 2
    Guessercalc()
def Guesser2():
    global money
    money -= 11
    global x
    global y
    x = 4
    y = 4
    Guessercalc()
def Guesser3():
    global money
    money -= 12
    global x
    global y
    x = 9
    y = 8
    Guessercalc()
def Guesser4():
    global money
    money -= 13
    global x
    global y
    x = 99
    y = 50
    Guessercalc()
def Guesser5():
    global money
    money -= 14
    global x
    global y
    x = 99999
    y = 100000000000000000
    Guessercalc()

def Guessercalc():
    for widget in root.winfo_children():
        widget.destroy()
    global result
    result = random.randint(0, x)
    lbl1 = Label(root, text = "Guess the number!, from 1 to " + str(x+1)).pack()
    global ent1
    ent1 = Entry(root)
    ent1.pack()
    btn1 = Button(root, text = "Guess!", command = Guessercalc2).pack()
def Guessercalc2():
    guess = ent1.get()
    try:
        guess = int(guess)
        guess -= 1
    except:
        Guessercalc()
    global lock
    if result == guess and lock == False:
        global x
        x = x * y
        text1 = "CONGRATULATIONS YOU WON {} SHMECKLES!".format(x)
        lbl1 = Label(root, text = text1).pack()
        global money
        money += x
        btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)
    elif lock == False:
        lbl1 = Label(root, text = "You lost!").pack()
        lock = True
        btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)
        

def Waster():
    for widget in root.winfo_children():
        widget.destroy()
      # I actually have an iq of 1034 simply because i watch rick and morty.
      # Make a simple story appear when you waste enough money, sortof like Candy box?
    lbl1 = Label(root, text = "You have {} shmeckles.".format(money)).pack()
    btn1 = Button(root, text = "Throw 10 shmeckles in the trash.", command = Waster2).pack()
    btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)
def Waster2():
    global money
    if money - 10 >= 0:
        money -= 10
    Waster()

def Bank():
    for widget in root.winfo_children():
        widget.destroy()
      # Implement better dept system
    global money
    global dept
    lbl1 = Label(root, text = "How much money do you want to borrow?").pack(side=TOP)
    lbl2 = Label(root, text = "Shmeckles:{}, Dept:{}.".format(money, dept)).pack(side=TOP)
    btn1 = Button(root, text = "100 shmeckles", command = bank100).pack()
    btn2 = Button(root, text = "10000 shmeckles", command = bank10000).pack()
    btn3 = Button(root, text = "1000000 shmeckles", command = bank1000000).pack()
    btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)

def bank100():
    global money
    global dept
    money += 100
    dept += 100
    Bank()
def bank10000():
    global money
    global dept
    money += 10000
    dept += 100000
    Bank()
def bank1000000():
    global money
    global dept
    money += 1000000
    dept += 10000000
    Bank()

root = Toplevel()
root.geometry("400x300")
root.title("Gambler")
btn1 = Button(root, text = "Gamble your money away!", command = begin)
btn1.pack()
root.mainloop()