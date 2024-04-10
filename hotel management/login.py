from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import BOLD
import mysql.connector
from hotel import HotelManagementSystem
from register import reg_window
from forgot import for_window
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1550x1750+0+0")


        im1=Image.open("log1.png")
        im1=im1.resize((1550,1750),Image.LANCZOS)
        self.photoim1=ImageTk.PhotoImage(im1)
        lbimg=Label(self.root,image=self.photoim1,bd=4)
        lbimg.place(x=0,y=0,width=1550,height=1750)

        frame=Frame(self.root,bg="BLUE")
        frame.place(x=610,y=170,width=340,height=450)

        im=Image.open("lock.png")
        im=im.resize((200,100),Image.LANCZOS)
        self.photoim=ImageTk.PhotoImage(im)
        lbimg1=Label(self.root,image=self.photoim,bg="WHITE",bd=4)
        lbimg1.place(x=700,y=175,width=200,height=100)
        self.email=StringVar()
        self.password=StringVar()


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="BLUE")
        get_str.place(x=95,y=120)


        user=Label(frame,text=" Email ID ",font=("times new roman",15,"bold"),fg="RED",bg="WHITE")
        user.place(x=20,y=155)

        entryuser=ttk.Entry(frame,width=20,textvariable=self.email,font=("arial",13,BOLD))
        entryuser.place(x=130,y=155)

        passs=Label(frame,text="Password",font=("arial",13,BOLD),bg="WHITE",fg="RED")
        passs.place(x=20,y=230)

        entrypass=ttk.Entry(frame,width=20,textvariable=self.password,font=("arial",13,BOLD),show="*")
        entrypass.place(x=130,y=230)





        inbtt=Button(frame,text="Login",bd=3,relief=RIDGE,command=self.login,bg="red",fg="white",font=("arial",13,BOLD))
        inbtt.place(x=110,y=300,width=120,height=35)

        rbtt=Button(frame,text="Registration",bd=3,relief=RIDGE,command=self.reg,bg="red",fg="white",font=("arial",13,BOLD))
        rbtt.place(x=10,y=360,width=120,height=35)

        fbtt=Button(frame,text="Forgot Password",command=self.fg,bd=3,relief=RIDGE,bg="red",fg="white",font=("arial",13,BOLD))
        fbtt.place(x=170,y=360,width=150,height=35)

    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=reg_window(self.new_window)


        




    def login(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from login where email=%s and password=%s",(self.email.get(),self.password.get()))

        rows=my_cursor.fetchone()
        if self.email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif rows==None:
            messagebox.showerror("Error","Invalid Details",parent=self.root)
        else:
            open_main=messagebox.askyesno("confirmation","Admin Only Area",parent=self.root)
            if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=HotelManagementSystem(self.new_window)
            else:
                if not open_main:
                    return
        conn.commit()
        conn.close()

    def fg(self):
        
        self.new_window=Toplevel(self.root)
        self.app=for_window(self.new_window)

    


            
       
        
        

if __name__=="__main__":
    root=Tk()
    obj=login_window(root)
    root.mainloop()