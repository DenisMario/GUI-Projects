from tkinter import *
from tkinter import messagebox

def login():
    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo("","You need to type in your username and password!")

    elif (username=='Denis' and password=="Admin123"):
        messagebox.showinfo("","Login Successful")

    else:
        messagebox.showinfo('','Incorrect username and password!')


root=Tk()
root.title("Login")
root.geometry('400x350')

#Adding a frame
frame1 = Frame(root, highlightbackground="Red", highlightthickness=4,width=650, height=650, bd= 8)
frame1.pack()

global entry1
global entry2

Label(root,text='Username:',fg='green',font='Bold').place(x=25,y=25)
Label(root,text='Password:',fg='orange',font='Bold').place(x=25,y=75)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=25)

entry2=Entry(root,bd=5)
entry2.place(x=140,y=75)

#Buttons that add option to sign in or exit the program
button1 = Button(root,text='Sign in',command=login,fg='purple',font='Bold',height=3,width=6,bd=10).place(x=100,y=120)
button2 = Button(root,text='Exit',command=root.destroy,fg='red',font='Bold',height=3,width=6,bd=10).place(x=100,y=200)
root.mainloop()
