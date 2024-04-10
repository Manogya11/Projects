
from os import name
from tkinter import *
import random
import mysql.connector
from tkinter.font import BOLD
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

from mysql.connector import connection
class reportpg:
    def __init__(self,root):
        self.root=root
        self.root.title("Developer Details")
        self.root.geometry("1295x600+230+220")


        Title=Label(self.root,text="Developer Details",bg="black",fg="gold",font=("times new roman",18,BOLD),relief=RIDGE)
        Title.place(x=0,y=0,width=1295,height=50)
        # Title.pack()


        showdata=Frame(self.root,bd=4,relief=RIDGE,padx=2)
        showdata.place(x=255,y=55,width=800,height=400)

        name=Label(showdata,text="Developer Name 1:  Karan gautam",font=("times new roman",28,BOLD))
        name.grid(row=0,column=0,padx=120)
        name=Label(showdata,text="Developer Name 2:  Priyank Gupta",font=("times new roman",28,BOLD))
        name.grid(row=1,column=0,padx=120)
        name=Label(showdata,text="Developer Name 3:  Manogya singh",font=("times new roman",28,BOLD))
        name.grid(row=2,column=0,padx=120)

        # mobile=Label(showdata,text="Mobile No. :    6396415727",font=("times new roman",28,BOLD))
        # mobile.grid(row=1,column=0,padx=150)
        email=Label(showdata,text="Email 1 :  karangautam@gmail.com      ",font=("times new roman",28,BOLD))
        email.grid(row=4,column=0,padx=100)

        email=Label(showdata,text="  Email 2 :  priyankgupta292@gmail.com  ",font=("times new roman",28,BOLD))
        email.grid(row=5,column=0,padx=100)

        email=Label(showdata,text="Email 3 :  singhmanogya@gmail.com     ",font=("times new roman",28,BOLD))
        email.grid(row=6,column=0,padx=100)
        
if __name__=="__main__":
    root=Tk()
    obj=reportpg(root)
    root.mainloop()