#Guess the number:-)
from tkinter import *
import random
import os
from PIL import Image, ImageTk
root = Tk()#Starting the root.



class win:#Class
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
           
    
    def event(e):
        number = var1.get()
        Label1=Label(root,text="", font=("Candara",24), bg="#c6cdaf")
        Label1.place(x=250,y=400)
        try:
            if int(number) < 0:
                dispaly_label = Label(root,text="Number cannot be negative", font=("Candara",24), bg="#06fc5c").place(250,400)
            else:
                dispaly_label = Label(root,text="Enter space to continue", font=("Candara",24), bg="#06fc5c").place(250,400)
        except:
            dispaly_label = Label(root,text="Pls input valid number", font=("Candara",18), bg="#c6cdaf")
            dispaly_label.place(x=1,y=350)
        count=0
        x1=1
        y1=350
        
        if int(var1.get())==rand2:
            dispaly_label = Label(root,text="Congrats on winning", font=("Candara",24), bg="#06fc5c")
            dispaly_label.place(x=x1,y=y1)
            Entry1.config(state=DISABLED)
            
        elif int(var1.get())>rand2:
            dispaly_label = Label(root,text="The number is too large", font=("Candara",20), bg="#FABF2D")
            dispaly_label.place(x=x1,y=y1)
            
        elif int(var1.get())<rand2:
            dispaly_label = Label(root,text="The number is too small", font=("Candara",20), bg="#FABF2D")
            dispaly_label.place(x=x1,y=y1)
        
            
        
            
    def restart():
        
        root.destroy()#Closing the program
        os.startfile("Guess the number.pyw")#Starting the program using the path we saved.
    

            
root.geometry("596x400") #The dimensions of the screen
root.title("Guess The Number") #The title
root.resizable(False,False)  #It should not be able to resize it
root.config(bg="#c6cdaf")#It configures the background to blue
#Image
image2=Image.open("guess the number.png")
image1=ImageTk.PhotoImage(image2)

label1=Label(root,image=image1).place(x=0,y=0)

var1=StringVar()#Integer Variable 1

#Labels:- Labels are used for showing the text on the main screen. The (.place)is used for setting the coordinates of the particular text.

Heading1=Label(root,text="Welcome!", font=("Candara",40), bg="#edb152").place(x=200,y=15)

instructions=Label(root,text="Instructions: Type any number from 1 to 10, and try to guess the correct number!(Click Enter on keyboard to play)",font=("Candara",9), bg="#edb152").place(x=1,y=250)

rand2=random.randrange(1,11)



Entry1=Entry(root,font=("Candara",18,"bold"),bd=7, state=NORMAL, width=6, textvariable=var1)
Entry1.place(x=1, y=300, width=400)



Reset=Button(root,relief=SOLID,text="Play Again!",font=("Candara",20),bg="#8C26A8",activebackground="#8C26A8",command=win.restart).place(x=430,y=300)


root.bind('<Return>', win.event)
root.mainloop()