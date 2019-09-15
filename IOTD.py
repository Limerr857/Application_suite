
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
      # Remove all previous widgets
    for widget in root.winfo_children():
        widget.destroy()
      # Gets the dir where images is located
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "images/"
    file_path = os.path.join(script_dir, rel_path)
      # Puts those images into "files"
    files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    fileslen = len(files)
      # Calculates key for next step
    key = round(time.time() / 86400)
      # Randomises what file to pick using key of roughly current day
    random.seed(key)
    randfile = random.randint(0, fileslen-1)
    randfile = files[randfile]
      # Displays image
    img1 = Image.open(join("images/", randfile))
    img1 = img1.resize((426, 240))
    img1 = ImageTk.PhotoImage(img1)
    lbl2 = Label(root, image=img1)
    lbl2.image = img1
    lbl2.pack()


root = Toplevel()
root.geometry("550x300")
root.title("Image Of The Day")
btn1 = Button(root, text = "Get me the image of the day!", command = begin)
btn1.pack()
lbl1 = Label(root, text = 'Displays an random image from the folder "images" inside of the same folder as the .exe. \nSupports most file formats, images with a 16:9 aspect ratio works best.')
lbl1.pack()
root.mainloop()