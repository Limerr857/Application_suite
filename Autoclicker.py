from tkinter import *
from tkinter.ttk import *
import pyautogui
from pynput.keyboard import Key, Listener

pyautogui.PAUSE = 0

global activation_key
global activate
global key
activation_key = "enter"
activate = False
key = None

def begin():
    for widget in root.winfo_children(): 
        widget.destroy()
    lbl1 = Label(root, text="NOTE: PRESS ESC AT ANY TIME TO ABORT").pack(side=TOP)
    #btn1 = Button(root, text="Apply").pack(side=BOTTOM)
    lbl2 = Label(root, text="activation key: Enter").pack()


def on_press(key):
    global activate
    global activation_key
    if key == Key.esc:
        # Stop listener
        return False
    else:
        if key == Key.enter:
            (x, y) = pyautogui.position()
            pyautogui.click(x, y)
            key == None

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

listener = Listener(on_press=on_press,on_release=on_release)
listener.start()


root = Toplevel()
root.geometry("304x300")
root.title("Autoclicker")
btn1 = Button(root, text = "Click for me!", command = begin)
btn1.pack()
root.mainloop()