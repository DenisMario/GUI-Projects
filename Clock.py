from tkinter import *
from tkinter import Tk
from tkinter import Label
import time
import sys


root = Tk()
root.title("Denis's Digital Clock")

def Time():
    timeVar=time.strftime("%H:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,Time)

clock = Label(root,font=("Arial",90),bg='black',fg='blue')
clock.pack()

Time()

root.mainloop
