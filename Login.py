from tkinter import *
from tkinter import messagebox

def login():
    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo("","You need to type in your username and password!")

    elif (username=='Denis' and password=="admin123"):
        messagebox.showinfo("","Login Successful")

    else:
        messagebox.showinfo('','Incorrect username and password!')


root=Tk()
root.title("Login")
root.geometry('300x250')

global entry1
global entry2

Label(root,text='Username').place(x=25,y=25)
Label(root,text='Password').place(x=25,y=75)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=25)

entry2=Entry(root,bd=5)
entry2.place(x=140,y=75)

Button(root,text='Sign in',command=login,height=3,width=13,bd=6).place(x=100,y=120)

root.mainloop()
