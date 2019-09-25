
from tkinter import *
from tkinter.ttk import *
import random
import time

alphabet = """abcdefghijklmnopqrstuvwxyzåäö .,/_-+=():'*?!1234567890&$€#@^~;
	"""  # Used for first level of encryption
alen = str.__len__(alphabet)  # Gets the length of this ^, used for easy adding of new characters
global notalphabet
notalphabet = """c!tp#eaw_m)ov*d5+.? j/
z3@flä$nrhqök&4u^0(6=8bisy71-g,2~;':9å€x	"""  # Used for second, third and fourth level of encryption, shuffled
textheight = 8
lvl3bg = 50
lvl3sm = 20


def strt():  # Start of the program, screen where you can choose between encrypt and decrypt.
    # Clears the entire window without deleting root
    for widget in window.winfo_children(): 
        widget.destroy()
    btn2 = Button(window, text = "Encrypt", command = encrypt) 
    btn3 = Button(window, text = "Decrypt", command = decrypt)
    lbl1 = Label(window, text = "What do you want to do?") 
    lbl1.pack()
    btn3.pack(side = BOTTOM)
    btn2.pack(side = BOTTOM)

def encrypt():
    for widget in window.winfo_children():
        widget.destroy()
    lbl6 = Label(window, text = "Choose a security level.")
    btn8 = Button(window, text = "Level 1", command = encrypt1)
    btn9 = Button(window, text = "Level 2", command = encrypt2)
    btn10 = Button(window, text = "Level 3", command = encrypt3)
    btn11 = Button(window, text = "Level 4", command = encrypt4)
    lbl6.pack(side = TOP)
    btn8.pack(fill = X)
    btn9.pack(fill = X)
    btn10.pack(fill = X)
    btn11.pack(fill = X)

def decrypt():
    for widget in window.winfo_children():
        widget.destroy()
    lbl6 = Label(window, text = "Choose a security level.")
    btn8 = Button(window, text = "Level 1", command = decrypt1)
    btn9 = Button(window, text = "Level 2", command = decrypt2)
    btn10 = Button(window, text = "Level 3", command = decrypt3)
    btn11 = Button(window, text = "Level 4", command = decrypt4)
    lbl6.pack(side = TOP)
    btn8.pack(fill = X)  # Fill is used for A S T H E T I C S
    btn9.pack(fill = X)
    btn10.pack(fill = X)
    btn11.pack(fill = X)


  # Level 1
def encrypt1(): # Easiest form of encrypting, uses something very similar to the ceasar chipher
    for widget in window.winfo_children():
        widget.destroy()
    global txt2 
    txt2 = Text(window, height = textheight) 
    btn4 = Button(window, text = "Encrypt", command = encrypt11)
    lbl2 = Label(window, text = 'Write the message you want to encrypt and press "Encrypt"')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()
    
def encrypt11():  # Multiple def's used because of lazyness
    temp2 = txt2.get('1.0', 'end-1c')  # Gets everything from the inptted text
    for widget in window.winfo_children():
        widget.destroy()
    temp2 = str.lower(temp2)
    message = list(temp2)
    msglen = len(message)
    x = 0
    while x < msglen:
        temp1 = message[x]
        temp1 = alphabet.find(temp1)
        if temp1 <= alen - 3:
            temp1 += 2
        elif temp1 == alen - 2:
            temp1 = 0
        elif temp1 == alen - 1:
            temp1 = 1
        else:
            print ("Error")
        temp1 = alphabet[temp1]
        message[x] = temp1
        x += 1
    message = ''.join(message)
    txt1 = Text(window, height = textheight) 
    txt1.insert(1.0, message)
    lbl3 = Label(window, text = "Here is your encrypted message:")
    btn5 = Button(window, text = "Restart Encrypt0r", command = strt)
    lbl3.pack(side = TOP)
    txt1.pack()
    btn5.pack(side = BOTTOM)
    txt1.configure(bg=window.cget('bg'), relief=FLAT)  # These two might be useless, but I can't be bothered to check
    txt1.configure(state="disabled")      


def decrypt1(): # Easiest form of decrypting, uses something very similar to the ceasar chipher
    for widget in window.winfo_children():
        widget.destroy()
    global txt2
    txt2 = Text(window, height = textheight)
    btn6 = Button(window, text = "Decrypt", command = decrypt11)
    lbl4 = Label(window, text = 'Write/paste the message you want to decrypt and press "Decrypt"')
    lbl4.pack(side = TOP)
    btn6.pack(side = BOTTOM)
    txt2.pack()

def decrypt11():
    global txt2
    temp2 = txt2.get('1.0', 'end-1c')  # Gets everything from the inptted text
    for widget in window.winfo_children():
        widget.destroy()
    message = list(temp2)
    msglen = len(message)
    x = 0
    while x < msglen:
        temp1 = message[x]
        temp1 = alphabet.find(temp1)
        if temp1 >= 2:
            temp1 += -2
        elif temp1 == 1:
            temp1 = alen - 2
        elif temp1 == 0:
            temp1 = alen - 1
        else:
            print ("Error")
        temp1 = alphabet[temp1]
        message[x] = temp1
        x += 1
    message = ''.join(message)
    txt2 = Text(window, height = textheight) 
    txt2.insert(1.0, message)
    lbl5 = Label(window, text = "Here is your decrypted message:")
    btn7 = Button(window, text = "Restart Encrypt0r", command = strt)
    lbl5.pack(side = TOP)
    txt2.pack()
    btn7.pack(side = BOTTOM)
    txt2.configure(bg=window.cget('bg'), relief=FLAT)  # These two might be useless, but I can't be bothered to check
    txt2.configure(state="disabled") 


  # Level 2    
def encrypt2():  # Second to easiest form of encryption, same as level 1 but with shuffled letters and symbols
    for widget in window.winfo_children():
        widget.destroy()
    global txt2
    txt2 = Text(window, height = textheight)  
    btn4 = Button(window, text = "Encrypt", command = encrypt22)
    lbl2 = Label(window, text = 'Write the message you want to encrypt and press "Encrypt"')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()

def encrypt22():
    temp2 = txt2.get('1.0', 'end-1c')  # Gets everything from the inputted text
    for widget in window.winfo_children():
        widget.destroy()
    temp2 = str.lower(temp2)
    message = list(temp2)
    msglen = len(message)
    x = 0
    while x < msglen:
        temp1 = message[x]
        temp1 = notalphabet.find(temp1)
        if temp1 <= alen - 3:
            temp1 += 2
        elif temp1 == alen - 2:
            temp1 = 0
        elif temp1 == alen - 1:
            temp1 = 1
        else:
            print ("Error")
        temp1 = notalphabet[temp1]
        message[x] = temp1
        x += 1
    message = ''.join(message)
    txt1 = Text(window, height = textheight) 
    txt1.insert(1.0, message)
    lbl3 = Label(window, text = "Here is your encrypted message:")
    btn5 = Button(window, text = "Restart Encrypt0r", command = strt)
    lbl3.pack(side = TOP)
    txt1.pack()
    btn5.pack(side = BOTTOM)
    txt1.configure(bg=window.cget('bg'), relief=FLAT)  # These two might be useless, but I can't be bothered to check
    txt1.configure(state="disabled")      


def decrypt2():  # Second to easiest form of decryption, same as level 1 but with shuffled letters and symbols
    for widget in window.winfo_children():
        widget.destroy()
    global txt2
    txt2 = Text(window, height = textheight)
    btn6 = Button(window, text = "Decrypt", command = decrypt22)
    lbl4 = Label(window, text = 'Write/paste the message you want to decrypt and press "Decrypt"')
    lbl4.pack(side = TOP)
    btn6.pack(side = BOTTOM)
    txt2.pack()

def decrypt22():
    global txt2
    temp2 = txt2.get("1.0",'end-1c')  # Gets everything from the inptted text
    for widget in window.winfo_children():
        widget.destroy()
    message = list(temp2)
    msglen = len(message)
    x = 0
    while x < msglen:
        temp1 = message[x]
        temp1 = notalphabet.find(temp1)
        if temp1 >= 2:
            temp1 += -2
        elif temp1 == 1:
            temp1 = alen - 2
        elif temp1 == 0:
            temp1 = alen - 1
        else:
            print ("Error")
        temp1 = notalphabet[temp1]
        message[x] = temp1
        x += 1
    message = ''.join(message)
    txt2 = Text(window, height = textheight) 
    txt2.insert(1.0, message)
    lbl5 = Label(window, text = "Here is your decrypted message:")
    btn7 = Button(window, text = "Restart Encrypt0r", command = strt)
    lbl5.pack(side = TOP)
    txt2.pack()
    btn7.pack(side = BOTTOM)
    txt2.configure(bg=window.cget('bg'), relief=FLAT)  # These two might be useless, but I can't be bothered to check
    txt2.configure(state="disabled") 


  # Level 3
def encrypt3():  # Third most insecure, this time a key is also used, wich eliminates looking through the code to find the letters.
    for widget in window.winfo_children():
        widget.destroy()
    global txt2
    txt2 = Text(window, height = textheight)  
    btn4 = Button(window, text = "Encrypt", command = encrypt31)
    lbl2 = Label(window, text = 'Write the message you want to encrypt and press "Encrypt"')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()
    
def encrypt31():
    global txt2
    global temp2
    temp2 = txt2.get("1.0",'end-1c')  # Gets everything from the inputted text
    for widget in window.winfo_children():
        widget.destroy()
    global key
    txt2 = Text(window, height = textheight)  
    btn4 = Button(window, text = "Use key", command = encrypt33)
    lbl2 = Label(window, text = 'Write the key you want to use, the larger the key the better the encryption.\nYou will need to securely send this key to your recipient.')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()

def encrypt33():
    global txt2
    key = txt2.get("1.0",'end-1c')  # Gets everything from the inputted text
    for widget in window.winfo_children():
        widget.destroy()
    global temp2
    temp2 = str.lower(temp2)
    message = list(temp2)
    x = 0
    for i in message:
        i = notalphabet.find(i)
        # The core of the calculation
        random.seed(key)
        i = i * random.randint(lvl3sm, lvl3bg)
        #
        message[x] = i
        x += 1
    message = '    '.join(str(e) for e in message)
    txt2 = Text(window, height = 8, wrap = WORD) 
    txt2.insert(1.0, message)
    lbl5 = Label(window, text = "Here is your encrypted message:")
    btn7 = Button(window, text = "Restart Encrypt0r", command = strt)
    lbl5.pack(side = TOP)
    txt2.pack()
    btn7.pack(side = BOTTOM)
    txt2.configure(bg=window.cget('bg'), relief=FLAT)  # These two might be useless, but I can't be bothered to check
    txt2.configure(state="disabled") 


def decrypt3():
    for widget in window.winfo_children():
        widget.destroy()
    global txt2
    txt2 = Text(window, height = textheight)  
    btn4 = Button(window, text = "Decrypt", command = decrypt31)
    lbl2 = Label(window, text = 'Write the message you want to decrypt and press "Decrypt"')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()
    
def decrypt31():
    global txt2
    global temp2
    temp2 = txt2.get("1.0",'end-1c')  # Gets everything from the inputted text
    for widget in window.winfo_children():
        widget.destroy()
    global key
    txt2 = Text(window, height = textheight)  
    btn4 = Button(window, text = "Use key", command = decrypt33)
    lbl2 = Label(window, text = 'Write the key that the sender has sent you securely.')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()

def decrypt33():
    global txt2
    key = txt2.get("1.0",'end-1c')  # Gets everything from the inputted text
    for widget in window.winfo_children():
        widget.destroy()
    message = temp2.split()
    x = 0
    for i in message:
        i = int(i)
        # The core of the calculation
        random.seed(key)
        i = i / random.randint(lvl3sm, lvl3bg)
        #
        i = int(i)
        i = notalphabet[i]
        message[x] = i
        x += 1
    message = ''.join(str(e) for e in message)
    txt2 = Text(window, height = 8, wrap = WORD) 
    txt2.insert(1.0, message)
    lbl5 = Label(window, text = "Here is your decrypted message:")
    btn7 = Button(window, text = "Restart Encrypt0r", command = strt)
    lbl5.pack(side = TOP)
    txt2.pack()
    btn7.pack(side = BOTTOM)
    txt2.configure(bg=window.cget('bg'), relief=FLAT)  # These two might be useless, but I can't be bothered to check
    txt2.configure(state="disabled") 


  # Level 4
def encrypt4():  # Fourth most insecure, this time a key is used to generate a random sequence to raise the numbers by.
    for widget in window.winfo_children():
        widget.destroy()
    global txt2
    txt2 = Text(window, height = textheight)  
    btn4 = Button(window, text = "Encrypt", command = encrypt41)
    lbl2 = Label(window, text = 'Write the message you want to encrypt and press "Encrypt"')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()
    
def encrypt41():
    global txt2
    global temp2
    temp2 = txt2.get("1.0",'end-1c')  # Gets everything from the inputted text
    for widget in window.winfo_children():
        widget.destroy()
    global key
    txt2 = Text(window, height = textheight)  
    btn4 = Button(window, text = "Use key", command = encrypt44)
    lbl2 = Label(window, text = 'Write the key you want to use, the larger the key the better the encryption.\nYou will need to securely send this key to your recipient.\nYou can use both numbers, letters and special characters.')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()

def encrypt44():
    global txt2
    key = txt2.get("1.0",'end-1c')  # Gets everything from the inputted text
    for widget in window.winfo_children():
        widget.destroy()
    try:
        key = int(key)
    except:
        key = list(key)
        x = 0
        global notalphabet
        for i in key:
            temp1 = notalphabet.find(i)
            key[x] = temp1
            x += 1
        key = '+'.join(str(e) for e in key)
        key = eval(key)
    global temp2
    temp2 = str.lower(temp2)
    msglen = len(temp2)
    message = list(temp2)
    x = 4
    days = round(time.time() / 86400)
    random.seed(key + days)
    temp4 = random.randint(10 ** ((msglen) * 6), 10 ** ((msglen + 1) * 6) - 1)
    temp6 = [int(x) for x in str(temp4)]
    y = 0
    while y < msglen * 1.2:
        temp6[x] = ","
        y += 1
        x += 5
    temp6 = ''.join(str(e) for e in temp6)
    temp6 = temp6.split(",")
    x = 0
    temp6 = list(map(int, temp6))
    notalphabet = str(notalphabet)
    for i in message:
        i = notalphabet.find(i)
        # The core of the calculation
        i += temp6[x]
        #
        message[x] = i
        x += 1
    message = '    '.join(str(e) for e in message)
    txt2 = Text(window, height = 8, wrap = WORD) 
    txt2.insert(1.0, message)
    lbl5 = Label(window, text = "Here is your encrypted message:")
    btn7 = Button(window, text = "Restart Encrypt0r", command = strt)
    scr1 = Scrollbar(window, command=txt2.yview)
    txt2['yscrollcommand'] = scr1.set
    scr1.grid(row = 2, column = 1, sticky="ns")
    lbl5.grid(row = 1)
    txt2.grid(row = 2)
    btn7.grid(row = 3)


def decrypt4():  # Fourth most insecure, this time a key is used to generate a random sequence to raise the numbers by.
    for widget in window.winfo_children():
        widget.destroy()
    global txt2
    txt2 = Text(window, height = textheight)  
    btn4 = Button(window, text = "Decrypt", command = decrypt41)
    lbl2 = Label(window, text = 'Write the message you want to decrypt and press "Decrypt"')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()
    
def decrypt41():
    global txt2
    global temp2
    temp2 = txt2.get("1.0",'end-1c')  # Gets everything from the inputted text
    for widget in window.winfo_children():
        widget.destroy()
    global key
    txt2 = Text(window, height = textheight)  
    btn4 = Button(window, text = "Use key", command = decrypt44)
    lbl2 = Label(window, text = 'Write the key that the sender has sent you securely.')
    lbl2.pack(side = TOP)
    btn4.pack(side = BOTTOM)
    txt2.pack()

def decrypt44():
    global txt2
    global temp2
    key = txt2.get("1.0",'end-1c')  # Gets everything from the inputted text
    for widget in window.winfo_children():
        widget.destroy()
    try:
        key = int(key)
    except:
        key = list(key)
        x = 0
        global notalphabet
        for i in key:
            temp1 = notalphabet.find(i)
            key[x] = temp1
            x += 1
        key = '+'.join(str(e) for e in key)
        key = eval(key)
    message = temp2.split()
    msglen = len(message)
    x = 4
    days = round(time.time() / 86400)
    random.seed(key + days)
    temp4 = random.randint(10 ** ((msglen) * 6), 10 ** ((msglen + 1) * 6) - 1)
    temp6 = [int(x) for x in str(temp4)] 
    y = 0
    while y < msglen * 1.2:
        temp6[x] = ","
        y += 1
        x += 5
    temp6 = ''.join(str(e) for e in temp6)
    temp6 = temp6.split(",")
    x = 0
    temp6 = list(map(int, temp6))
    x = 0
    for i in message:
        i = int(i)
        # The core of the calculation
        i -= temp6[x]
        #
        i = int(i)
        notalphabet = list(notalphabet)
        i = notalphabet[i]
        message[x] = i
        x += 1
    message = ''.join(str(e) for e in message)
    txt2 = Text(window, height = 8, wrap = WORD) 
    txt2.insert(1.0, message)
    lbl5 = Label(window, text = "Here is your decrypted message:")
    btn7 = Button(window, text = "Restart Encrypt0r", command = strt)
    lbl5.pack(side = TOP)
    txt2.pack()
    btn7.pack(side = BOTTOM)
    txt2.configure(bg=window.cget('bg'), relief=FLAT)  # These two might be useless, but I can't be bothered to check
    txt2.configure(state="disabled") 


global window
window = Tk()
window.geometry("700x400")
window.title("Encrypt0r")
btn1 = Button(window, text = "Start Encrypt0r", command = strt)
btn1.pack()
window.mainloop()