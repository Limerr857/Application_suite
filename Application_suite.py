
  # Yes, somehow these are all necessary
from tkinter import *
from tkinter.ttk import *
import random
from os import listdir
from os.path import isfile, join, dirname
import os
from PIL import ImageTk, Image
import time


def begin():
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "Choose an app to run.").pack(side = TOP)
    btn1 = Button(root, text = "Encrypt0r", command = Encrypt0r).pack(fill=X)
    btn2 = Button(root, text = "Calculat0r", command = Calculat0r).pack(fill=X)
    btn3 = Button(root, text = "Image Of The Day", command = IOTD).pack(fill=X)
    btn4 = Button(root, text = "Gambler", command = Gambler).pack(fill=X)

def Encrypt0r():
    exec(open("Encrypt0r.py", encoding="utf-8").read(), globals())

def Calculat0r():
    exec(open("Calculat0r.py", encoding="utf-8").read(),globals())

def IOTD():
    exec(open("IOTD.py", encoding="utf-8").read(),globals())

def Gambler():
    exec(open("Gambler.py", encoding="utf-8").read(),globals())

root = Tk()
root.geometry("550x300")
root.title("GE:APPS v.0.4")
btn1 = Button(root, text = "Start browsing", command = begin)
btn1.pack()
root.mainloop()