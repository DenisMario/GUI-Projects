from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Quiz')
root.geometry('220x190')

def CorrectAns():
    messagebox.showinfo("",'Right answer')

def WrongAns():
    messagebox.showinfo("",'Wrong answer')

    

Label1= Label(root,text='Multiple choice Quiz')
Label1.pack()
Label2= Label(root,text='What is the chemical symbol for Neon?',fg='blue')
Label2.pack()

Button1= Button(root,text='Ne',command=CorrectAns,bd=6,)
Button1.pack()
Button2= Button(root,text='Pb',command=WrongAns,bd=6)
Button2.pack()
Button3 = Button(root,text='Ni',command=WrongAns,bd=6)
Button3.pack()
Button4 = Button(root,text='Hg',command=WrongAns,bd=6)
Button4.pack()

root.mainloop()
