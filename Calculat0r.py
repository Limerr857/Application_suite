
from tkinter import *
from tkinter.ttk import *
import random

global counter
counter = []

def begin():
    for widget in root.winfo_children():  # Destroys all widgets in root
        widget.destroy()
    global txt1
    txt1 = Text(root, height = 3)
    txt1.configure(state='disabled', height = 3, width = 30)
    lbl1 = Label(root, text = 'Calculator. Might crash at too large of a calculation.').grid(row = 0, columnspan = 10)
    
    txt1.grid(row = 1, columnspan = 10)

      # Numbers
    btn0 = Button(root, text = "0", command = _btn0).grid(row = 6, column = 5)
    btn1 = Button(root, text = "1", command = _btn1).grid(row = 5, column = 4)
    btn2 = Button(root, text = "2", command = _btn2).grid(row = 5, column = 5)
    btn3 = Button(root, text = "3", command = _btn3).grid(row = 5, column = 6)
    btn4 = Button(root, text = "4", command = _btn4).grid(row = 4, column = 4)
    btn5 = Button(root, text = "5", command = _btn5).grid(row = 4, column = 5)
    btn6 = Button(root, text = "6", command = _btn6).grid(row = 4, column = 6)
    btn7 = Button(root, text = "7", command = _btn7).grid(row = 3, column = 4)
    btn8 = Button(root, text = "8", command = _btn8).grid(row = 3, column = 5)
    btn9 = Button(root, text = "9", command = _btn9).grid(row = 3, column = 6)

      # Operators
    btnplus = Button(root, text = "+", command = _btnplus).grid(row = 3, column = 7)
    btnminus = Button(root, text = "-", command = _btnminus).grid(row = 4, column = 7)
    btnmult = Button(root, text = "*", command = _btnmult).grid(row = 5, column = 7)
    btndiv = Button(root, text = "/", command = _btndiv).grid(row = 6, column = 7)
    btnparl = Button(root, text = "(", command = _btnparl).grid(row = 6, column = 4)  # Parethesis left
    btnparr = Button(root, text = ")", command = _btnparr).grid(row = 6, column = 6)  # Parenthesis right
    btnpwr = Button(root, text = "^", command = _btnpwr).grid(row = 7, column = 7)

      # Meta
    btnequals = Button(root, text = "=", command = count).grid(row = 8, column = 5)
    btndel = Button(root, text = "DELETE", command = _btndel).grid(row = 8, column = 4)
    btnclr = Button(root, text = "CLEAR", command = _btnclr).grid(row = 8, column = 6)

      # Constants
    btnpi = Button(root, text = "π", command = _btnpi).grid(row = 7, column = 4)
    btne = Button(root, text = "e", command = _btne).grid(row = 7, column = 5)
    btnphi = Button(root, text = "Φ", command = _btnphi).grid(row = 7, column = 6)

def main():
    txt1.configure(state='normal')
    txt1.delete("1.0", END)      # Clears txt1 and inserts counter[]
    txt1.insert("1.0", counter)
    txt1.configure(state='disabled')

  # Too many def's :-(
def _btn0():
    counter.append(0)
    main()
def _btn1():
    counter.append(1)
    main()
def _btn2():
    counter.append(2)
    main()
def _btn3():
    counter.append(3)
    main()
def _btn4():
    counter.append(4)
    main()
def _btn5():
    counter.append(5)
    main()
def _btn6():
    counter.append(6)
    main()
def _btn7():
    counter.append(7)
    main()
def _btn8():
    counter.append(8)
    main()
def _btn9():
    counter.append(9)
    main()
def _btnplus():
    counter.append("+")
    main()
def _btnminus():
    counter.append("-")
    main()
def _btnmult():
    counter.append("*")
    main()
def _btndiv():
    counter.append("/")
    main()
def _btnparl():
    counter.append("(")
    main()
def _btnparr():
    counter.append(")")
    main()
def _btnpwr():
    counter.append("**")
    main()
def _btndel():
    global counter
    counter = counter[:-1]  # Delete last character from counter
    main()
def _btnclr():
      # Clears txt1
    global counter
    counter = []
    main()
def _btnpi():
    counter.append("3.1415926535")
    main()
def _btne():
    counter.append("2.7182818284")
    main()
def _btnphi():
    counter.append("1.6180339887")
    main()

def count():
    global counter
    counter = ''.join(str(e) for e in counter)
    try:
        result = eval(counter)  # Evaluates = runs it like it were python code.
        counter = list(counter)
        counter.append("=")
        counter.append(str(result))
        main()
    except:
        counter = list(counter)
        counter.append("ERROR")
        main()

root = Tk()
root.geometry("304x300")
root.title("Calculat0r v.0.2")
btn1 = Button(root, text = "Start calculating", command = begin)
btn1.pack()
root.mainloop()
