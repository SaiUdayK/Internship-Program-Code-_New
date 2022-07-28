from tkinter import *
import random,os
from PIL import Image, ImageTk



root = Tk()#Starting the root.

root.geometry("800x600") #The dimensions of the screen
root.title("Rock Paper Scissors") #The title
root.resizable(False,False)  #It should not be able to resize itself. 
#Adding an image
image2=Image.open("rock1.png")
image1=ImageTk.PhotoImage(image2)

label1=Label(root,image=image1).place(x=0,y=0)
    
var1=StringVar()#String Variable 1

#Labels:- Labels are used for showing the text on the main screen. The (.place)is used for setting the coordinates of the particular text.

Heading1=Label(root,text="Welcome!", font=("Candara",40), bg="#ffea00").place(x=300,y=5)
Heading2=Label(root,text="Rock,Paper and Scissors Game",font=("Candara",30,"bold"),bg="#ffea00").place(x=160,y=100)
instructions=Label(root,text="Instructions: Type if U want scissors, rock or paper and wait for the computer to play its move.",font=("Candara",15), bg="#ffea00").place(x=1,y=160)
instructions2=Label(root,text="Pls type either Paper, Rock or Scissors in the box given below and then click enter.",font=("Candara",15), bg="#ffea00").place(x=50,y=460)




Computer=""

#random.randrange(1,4):- It saves any number from 1 to 3 in the variable named var1. 

rand1=random.randrange(1,4)
if rand1==1:
    Computer="Rock"
elif rand1==2:
    Computer="Scissors"
elif rand1==3:
    Computer="Paper"

def rockpaperscissor(e): #These are conditions which are used in the backend of the program to give us the result.
 #state=Disabled is used so that the user does not manipulate the game to win. It does not allow to change the entry once the game is completed.
    x1=419
    y1=410
    Label(root,text=" ", bg="#1c8e9d").place(x=x1,y=y1)
    if var1.get().lower()=="paper" and rand1==1:
                dispaly_label = Label(root,text="Congrats on winning, Robot selected - Rock", font=("Candara",15), bg="#19C25D")
                dispaly_label.place(x=x1,y=y1)
                entry.config(state=DISABLED)

    elif var1.get().lower()=="paper" and rand1==2  :
        dispaly_label = Label(root,text="Try again next time Robot selected - Scissors", font=("Candara",15), bg="#D31818")
        dispaly_label.place(x=x1,y=y1)
        entry.config(state=DISABLED)
    elif var1.get().lower()=="paper" and rand1==3 :
        dispaly_label = Label(root,text="Nice Try, Robot selected - Paper", font=("Candara",15), bg="#F0D10B")
        dispaly_label.place(x=x1,y=y1)
        entry.config(state=DISABLED)
    elif var1.get().lower()=="scissors" and rand1==1  :
        dispaly_label = Label(root,text="Try again next time, Robot selected - Rock", font=("Candara",15), bg="#D31818")
        dispaly_label.place(x=x1,y=y1)
        entry.config(state=DISABLED)
    elif var1.get().lower()=="scissors" and rand1==2  :
        dispaly_label = Label(root,text="Nice try, Robot selected - Scissors", font=("Candara",15), bg="#F0D10B")
        dispaly_label.place(x=x1,y=y1)
        entry.config(state=DISABLED)
    elif var1.get().lower()=="scissors" and rand1==3 :
        dispaly_label = Label(root,text="Congrats on winning, Robot selected - Paper", font=("Candara",15), bg="#19C25D")
        dispaly_label.place(x=x1,y=y1)
        entry.config(state=DISABLED)
    elif var1.get().lower()=="rock" and rand1==1 :
        dispaly_label = Label(root,text="Nice try, Robot selected - Rock", font=("Candara",15), bg="#F0D10B")
        dispaly_label.place(x=x1,y=y1)
        entry.config(state=DISABLED)
    elif var1.get().lower()=="rock" and rand1==2 :
        dispaly_label = Label(root,text="Congrats on winning, Robot selected - Scissors", font=("Candara",15), bg="#19C25D")
        dispaly_label.place(x=412,y=y1)
        entry.config(state=DISABLED)
    elif var1.get().lower()=="rock" and rand1==3  :
        dispaly_label = Label(root,text="Try again next time, Robot selected - Paper", font=("Candara",15), bg="#D31818")
        dispaly_label.place(x=x1,y=y1)
        entry.config(state=DISABLED)
        
    else:
        Label(root,text="Please input valid words:- (Rock, Paper, Scissors)",font=("Candara",13),bg="#BD3434").place(x=x1,y=y1)
root.bind('<Return>', rockpaperscissor)#This is for binding the "Enter button" on our keyboard to the event.
def restart():
    root.destroy()#Closing the program
    os.startfile("rock_paper_scissors.pyw")#Starting the program using the path we saved.



#Entry:- This is for typing an entry.

entry = Entry(root, font=('Candara', 18, 'bold'), bd=7, state=NORMAL, width=6, textvariable=var1)
entry.place(x=1, y=400, width=400)

def function1():
    entry.config(state=DISABLED)#state=Disabled is used so that the user does not manipulate the game to win. It does not allow to change the entry once the game is completed.

Lab=Label(root,text="Thanks a lot for playing", font=("Candara",30),bg="#1c8e9d").place(x=200,y=700)
Reset=Button(root,relief=SOLID,text="Play Again!",font=("Candara",20),bg="#8C26A8",activebackground="#8C26A8",border=1,command=restart).place(x=325,y=540)
#Button is used for restarting the game.

#root.mainloop():- The tkinter program runs using this.

root.mainloop()