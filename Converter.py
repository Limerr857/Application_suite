
from tkinter import *
from tkinter.ttk import *
import time

distlist = ["Meters", "Feet", "Kilometers", "Miles", "Centimeters", "Inches"]
templist = ["Kelvin", "Celsius", "Fahrenheit"]

def start():
    for widget in root.winfo_children():
        widget.destroy()
    btn1 = Button(root, text = "Convert distance units!", command = begindist)
    btn1.pack()
    btn2 = Button(root, text = "Convert temperature units!", command = begintemp)
    btn2.pack()
    #btn3 = Button(root, text = "Convert time units!", command = begintime)
    #btn3.pack()


def begindist():
    global lst1
    global lst2
    global distlist
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "What do you want to convert?").pack(side = TOP)
    btn2 = Button(root, text = "Go back", command = start).pack(fill=X, side=BOTTOM)
    btn1 = Button(root, text = "Convert!", command = convertdist0).pack(fill=X, side=BOTTOM)

    lst1 = Listbox(root)
    for item in distlist:
        lst1.insert(END, item)
    lst1.pack(side=LEFT, fill=X)

    lst2 = Listbox(root)
    for item in distlist:
        lst2.insert(END, item)
    lst2.pack(side=RIGHT, fill=X)

def convertdist0():
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
    convertdist15()

def convertdist15():
    convertdist1()

def convertdist1():
    for widget in root.winfo_children():
        widget.destroy()
    global lst1
    global lst2
    global unit1
    global unit2
    global ent1
    global result

    lbl1 = Label(root, text=unit1).pack()
    ent1 = Entry(root)
    ent1.pack()

    btn2 = Button(root, text="Go back", command=begintemp).pack(side=BOTTOM)
    btn1 = Button(root, text="Apply", command=convertdist2)
    btn1.pack(side=BOTTOM)

    # Stupidity
    if unit1 == unit2:
        result = "Converting a unit to itself is pointless."
        btn1.config(state="disabled")

    txt1 = Text(root)
    txt1.insert(1.0, "{}: {}".format((''.join(str(e) for e in unit2)), result))
    txt1.pack()

def convertdist2():
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
        convertdist15()


    # Welcome to elif hell.

    # Meters
    if "Meters" in unit1 and "Feet" in unit2:
        result = round((ent1_input * 3.28084), 3)
        convertdist1()
    elif "Meters" in unit1 and "Kilometers" in unit2:
        result = round((ent1_input / 1000), 3)
        convertdist1()
    elif "Meters" in unit1 and "Miles" in unit2:
        result = round((ent1_input / 1609.344), 3)
        convertdist1()
    elif "Meters" in unit1 and "Centimeters" in unit2:
        result = round((ent1_input * 100), 3)
        convertdist1()
    elif "Meters" in unit1 and "Inches" in unit2:
        result = round((ent1_input * 39.37008), 3)
        convertdist1()

    # Feet    
    elif "Feet" in unit1 and "Meters" in unit2:
        result = round((ent1_input / 3.28084), 3)
        convertdist1()
    elif "Feet" in unit1 and "Miles" in unit2:
        result = round((ent1_input / 5280), 3)
        convertdist1()
    elif "Feet" in unit1 and "Kilometers" in unit2:
        result = round((ent1_input / 3280.84), 3)
        convertdist1()
    elif "Feet" in unit1 and "Centimeters" in unit2:
        result = round((ent1_input / 0.0328084), 3)
        convertdist1()
    elif "Feet" in unit1 and "Inches" in unit2:
        result = round((ent1_input * 12), 3)
        convertdist1()

    # Kilometers
    elif "Kilometers" in unit1 and "Meters" in unit2:
        result = round((ent1_input * 1000), 3)
        convertdist1()
    elif "Kilometers" in unit1 and "Feet" in unit2:
        result = round((ent1_input * 3280.84), 3)
        convertdist1()
    elif "Kilometers" in unit1 and "Miles" in unit2:
        result = round((ent1_input / 1.609344), 3)
        convertdist1()
    elif "Kilometers" in unit1 and "Centimeters" in unit2:
        result = round((ent1_input * 100_000), 3)
        convertdist1()
    elif "Kilometers" in unit1 and "Inches" in unit2:
        result = round((ent1_input * 39370.08), 3)
        convertdist1()

    # Miles
    elif "Miles" in unit1 and "Meters" in unit2:
        result = round((ent1_input * 1609.344), 3)
        convertdist1()
    elif "Miles" in unit1 and "Feet" in unit2:
        result = round((ent1_input * 5280), 3)
        convertdist1()
    elif "Miles" in unit1 and "Kilometers" in unit2:
        result = round((ent1_input * 1.609344), 3)
        convertdist1()
    elif "Miles" in unit1 and "Centimeters" in unit2:
        result = round((ent1_input * 160_934.4), 3)
        convertdist1()
    elif "Miles" in unit1 and "Inches" in unit2:
        result = round((ent1_input * 63360), 3)
        convertdist1()

    # Centimeters
    elif "Centimeters" in unit1 and "Feet" in unit2:
        result = round((ent1_input * 0.0328084), 3)
        convertdist1()
    elif "Centimeters" in unit1 and "Kilometers" in unit2:
        result = round((ent1_input / 100_000), 3)
        convertdist1()
    elif "Centimeters" in unit1 and "Miles" in unit2:
        result = round((ent1_input / 160_934.4), 3)
        convertdist1()
    elif "Centimeters" in unit1 and "Meters" in unit2:
        result = round((ent1_input / 100), 3)
        convertdist1()
    elif "Centimeters" in unit1 and "Inches" in unit2:
        result = round((ent1_input * 0.3937008), 3)
        convertdist1()

    # Inches
    elif "Inches" in unit1 and "Feet" in unit2:
        result = round((ent1_input * 0.08333333), 3)
        convertdist1()
    elif "Inches" in unit1 and "Kilometers" in unit2:
        result = round((ent1_input * 0.0000254), 3)
        convertdist1()
    elif "Inches" in unit1 and "Miles" in unit2:
        result = round((ent1_input * 0.00001578283), 3)
        convertdist1()
    elif "Inches" in unit1 and "Meters" in unit2:
        result = round((ent1_input * 0.0254), 3)
        convertdist1()
    elif "Inches" in unit1 and "Centimeters" in unit2:
        result = round((ent1_input * 2.54), 3)
        convertdist1()
    

    else:
        result = "Something went wrong."
        convertdist15()



def begintemp():
    global lst1
    global lst2
    global templist
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "What do you want to convert?").pack(side = TOP)
    btn2 = Button(root, text = "Go back", command = start).pack(fill=X, side=BOTTOM)
    btn1 = Button(root, text = "Convert!", command = converttemp0).pack(fill=X, side=BOTTOM)

    lst1 = Listbox(root)
    for item in templist:
        lst1.insert(END, item)
    lst1.pack(side=LEFT, fill=X)

    lst2 = Listbox(root)
    for item in templist:
        lst2.insert(END, item)
    lst2.pack(side=RIGHT, fill=X)

def converttemp0():
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
    converttemp15()

def converttemp15():
    converttemp1()

def converttemp1():
    for widget in root.winfo_children():
        widget.destroy()
    global lst1
    global lst2
    global unit1
    global unit2
    global ent1
    global result

    lbl1 = Label(root, text=unit1).pack()
    ent1 = Entry(root)
    ent1.pack()

    btn2 = Button(root, text="Go back", command=begintemp).pack(side=BOTTOM)
    btn1 = Button(root, text="Apply", command=converttemp2)
    btn1.pack(side=BOTTOM)

    # Stupidity
    if unit1 == unit2:
        result = "Converting a unit to itself is pointless."
        btn1.config(state="disabled")

    txt1 = Text(root)
    txt1.insert(1.0, "{}: {}".format((''.join(str(e) for e in unit2)), result))
    txt1.pack()

def converttemp2():
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
        converttemp15()


    # Welcome to elif hell.

    # Kelvin
    if "Kelvin" in unit1 and "Celsius" in unit2:
        result = round((ent1_input - 272.15), 2)
        converttemp1()
    elif "Kelvin" in unit1 and "Fahrenheit" in unit2:
        result = round((ent1_input * 1.8 - 459.67), 2)
        converttemp1()

    # Celsius
    elif "Celsius" in unit1 and "Kelvin" in unit2:
        result = round((ent1_input + 272.15), 2)
        converttemp1()
    elif "Celsius" in unit1 and "Fahrenheit" in unit2:
        result = round((ent1_input * 1.8 + 32), 2)
        converttemp1()

    # Fahrenheit
    elif "Fahrenheit" in unit1 and "Kelvin" in unit2:
        result = round((ent1_input / 1.8 + 459.67), 2)
        converttemp1()
    elif "Fahrenheit" in unit1 and "Celsius" in unit2:
        result = round(((ent1_input - 32) / 1.8), 2)
        converttemp1()

    else:
        result = "Something went wrong."
        print(unit1)
        print(unit2)
        converttemp15()




root = Toplevel()
root.geometry("400x300")
root.title("Converter")
start()
root.mainloop()