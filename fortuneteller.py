import random
from tkinter import *


root = Tk()
root.geometry('450x300')
root.resizable(False,False)
root.title('Fortune Telling Game by Denis')

Label(root,text='Fortune Teller',font='arial 25 bold',fg='#ffd700',bg='mediumblue').pack()
Label(root,text='Ask a yes  or  no question:',font='arial 15 bold').place(x=100,y=70)
Label(root,text='Yes',fg='green',font='arial 15 bold').place(x=160,y=70)
Label(root,text='No',fg='red',font='arial 15 bold').place(x=230,y=70)
link=StringVar()
enter=Entry(root, width = 45, textvariable=link,bd=3).place(x=90,y=100)

def Response():
    num = random.randint(1,11)

    if num == 1:
        answer = 'Of course!'
    elif num == 2:
        answer = 'Yes'
    elif num == 3:
        answer = 'Yes but be cautious'
    elif num == 4:
        answer = 'Definitely!'
    elif num == 5:
        answer = 'Why not?'
    elif num == 6:
        answer = 'Uncertain, try again later..'
    elif num == 7:
        answer = 'No'
    elif num == 8:
        answer = 'Nope!'
    elif num == 9:
        answer = 'Doubt it'
    elif num == 10:
        answer = "Don't even bother"
    else:
        answer = 'Cannot Predict'
    
            

    Label(root, text=answer, font='roman 23 bold',bg='mediumaquamarine',fg='black').place(x=100, y=220)

Button(root,text='Respond to question', font='arial 18 bold',bg='papayawhip',fg='black', command = Response).place(x=100,y=129)



root.mainloop()
        
