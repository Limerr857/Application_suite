
from tkinter import *
from tkinter.ttk import *
import time

unitlist = ["Meters", "Feet", "Kilometers", "Miles"]

def begin():
    global lst1
    global lst2
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "What do you want to convert?").pack(side = TOP)
    btn1 = Button(root, text = "Convert!", command = convert0).pack(fill=X, side=BOTTOM)

    lst1 = Listbox(root)
    for item in unitlist:
        lst1.insert(END, item)

    lst1.pack(side=LEFT, fill=X)

    lst2 = Listbox(root)
    for item in unitlist:
        lst2.insert(END, item)

    lst2.pack(side=RIGHT, fill=X)

def convert0():
    global lst1
    global lst2
    global unit1
    global unit2
    global ent1
    global result

    try:
        i = lst1.curselection()[0]
        unit1 = lst1.get(i)
        unit2 = lst2.get(ACTIVE)
    except:
        unit1 = lst1.get(ACTIVE)
        i = lst2.curselection()[0]
        unit2 = lst2.get(i)

    result = ""
    convert15()

def convert15():
    convert1()

def convert1():
    for widget in root.winfo_children():
        widget.destroy()
    print("Convert1")
    global lst1
    global lst2
    global unit1
    global unit2
    global ent1
    global result

    lbl1 = Label(root, text=unit1).pack()
    ent1 = Entry(root)
    ent1.pack()

    btn2 = Button(root, text="Go back", command=begin).pack(side=BOTTOM)
    btn1 = Button(root, text="Apply", command=convert2)
    btn1.pack(side=BOTTOM)

       # Stupidity
    if unit1 == unit2:
        result = "Converting a unit to itself is pointless."
        btn1.config(state="disabled")

    txt1 = Text(root)
    txt1.insert(1.0, "{}: {}".format((''.join(str(e) for e in unit2)), result))
    txt1.pack()

def convert2():
    global unit1
    global unit2
    global result
    global ent1
    time.sleep(0.04)

    ent1_input = ent1.get()
    
    try:
        ent1_input = float(ent1_input)
    except:
        result = "Not a float."
        print("Not a float")
        convert15()

    # Welcome to elif hell.


    # Meters
    if "Meters" in unit1 and "Feet" in unit2:
        result = round((ent1_input * 3.28084), 3)
        convert1()
    elif "Meters" in unit1 and "Kilometers" in unit2:
        result = round((ent1_input / 1000), 3)
        convert1()
    elif "Meters" in unit1 and "Miles" in unit2:
        result = round((ent1_input / 1609.344), 3)
        convert1()

    # Feet    
    elif "Feet" in unit1 and "Meters" in unit2:
        result = round((ent1_input / 3.28084), 3)
        convert1()
    elif "Feet" in unit1 and "Miles" in unit2:
        result = round((ent1_input / 5280), 3)
        convert1()
    elif "Feet" in unit1 and "Kilometers" in unit2:
        result = round((ent1_input / 3280.84), 3)
        convert1()

    # Kilometers
    elif "Kilometers" in unit1 and "Meters" in unit2:
        result = round((ent1_input * 1000), 3)
        convert1()
    elif "Kilometers" in unit1 and "Feet" in unit2:
        result = round((ent1_input * 3280.84), 3)
        convert1()
    elif "Kilometers" in unit1 and "Miles" in unit2:
        result = round((ent1_input / 1.609344), 3)
        convert1()

    # Miles
    elif "Miles" in unit1 and "Meters" in unit2:
        result = round((ent1_input * 1609.344), 3)
        convert1()
    elif "Miles" in unit1 and "Feet" in unit2:
        result = round((ent1_input * 5280), 3)
        convert1()
    elif "Miles" in unit1 and "Kilometers" in unit2:
        result = round((ent1_input * 1.609344), 3)
        convert1()
    
    

    else:
        result = "Something went wrong."
        print(result)
        convert15()



root = Toplevel()
root.geometry("300x300")
root.title("Converter")
btn1 = Button(root, text = "Convert units!", command = begin)
btn1.pack()
root.mainloop()