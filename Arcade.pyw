from tkinter import *
import random
import os
from PIL import Image, ImageTk

root = Tk()#Starting the root.

class game: #Class:- Contains all the def functions
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
    def rockpaperscissors(): #Rockpaperscissors
        os.startfile("rock_paper_scissors.pyw")#Opening rock paper scissors.
    def guessthenumber():
        os.startfile("Guess the number.pyw")#Opening guess the number.


root.geometry("612x612") #The dimensions of the screen
root.title("Arcade") #The title
root.resizable(False,False)  #It should not be able to resize itself.
main_img=ImageTk.PhotoImage(Image.open("Arcade.jpg"))#Opening the image
#Creating a canvas for the image

canvas=Canvas(root,width=1600,height=1600)
canvas.pack(expand=True,fill=BOTH)
canvas.create_image(0,0,image=main_img,anchor="nw")

#Labels
Lab=Label(root,text="Welcome to the Arcade!!", font=("Candara",20,"bold"),bg="#6d1c6b").place(x=160,y=30)
Lab1=Label(root,text="Choose any one from the options below",font=("Canadara",12,"bold"),bg="#6d1c6b").place(x=160,y=100)
#Buttons for accessing the game
Game1=Button(root,relief=SOLID,text="Rock Paper Scissors!",font=("Candara",15,"bold"),bg="#8C26A8",activebackground="#8C26A8",border=1,command=game.rockpaperscissors).place(x=215,y=400)
Game2=Button(root,relief=SOLID,text="Guess the Number!",font=("Candara",15,"bold"),bg="#8C26A8",activebackground="#8C26A8",border=1,command=game.guessthenumber).place(x=220,y=450)

root.mainloop()