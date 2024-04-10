from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import BOLD
import mysql.connector
import random
import smtplib

class for_window:
    def __init__(self,root):
        self.root=root
        
        self.root.title("Password")
        self.root.geometry("1600x1750+0+0")


        im1=Image.open("for11.png")
        im1=im1.resize((1550,1750),Image.LANCZOS)
        self.photoim1=ImageTk.PhotoImage(im1)
        lbimg=Label(self.root,image=self.photoim1,bd=4)
        lbimg.place(x=0,y=0,width=1550,height=1750)

        frame=Frame(self.root,bg="pink")
        frame.place(x=610,y=170,width=340,height=300)

        im=Image.open("pass.png")
        im=im.resize((200,100),Image.LANCZOS)
        self.photoim=ImageTk.PhotoImage(im)
        lbimg1=Label(self.root,image=self.photoim,bg="WHITE",bd=4)
        lbimg1.place(x=685,y=175,width=200,height=100)
        self.username=StringVar()
        self.password=StringVar()
        self.OTP=StringVar()
        self.email=StringVar()
        self.y=StringVar()
        self.temp=StringVar()

        self.x=random.randint(100,9999)


        # get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="BLUE")
        # get_str.place(x=95,y=120)


        # user=Label(frame,text="Email ID",font=("times new roman",15,"bold"),fg="RED",bg="WHITE")
        # user.place(x=20,y=150)

        # entryuser=ttk.Entry(frame,width=20,textvariable=self.username,font=("arial",13,BOLD))
        # entryuser.place(x=130,y=150)


        # mob=Label(frame,text=" Contact ",font=("times new roman",15,"bold"),fg="RED",bg="WHITE")
        # mob.place(x=20,y=190)

        # entrymob=ttk.Entry(frame,width=20,textvariable=self.mobile,font=("arial",13,BOLD))
        # entrymob.place(x=130,y=190)

        email=Label(frame,text=" Email ID  ",font=("arial",13,BOLD),bg="WHITE",fg="RED")
        email.place(x=20,y=130)

        entryemail=ttk.Entry(frame,width=20,textvariable=self.email,font=("arial",13,BOLD))
        entryemail.place(x=130,y=130)


        OTP=Label(frame,text="Enter OTP",font=("arial",13,BOLD),bg="WHITE",fg="RED")
        OTP.place(x=20,y=170)

        entryOTP=ttk.Entry(frame,width=20,textvariable=self.OTP,font=("arial",13,BOLD))
        entryOTP.place(x=130,y=170)

        
        # passs=Label(frame,text="Password",font=("arial",13,BOLD),bg="WHITE",fg="RED")
        # passs.place(x=20,y=270)

        # entrypass=ttk.Entry(frame,width=20,textvariable=self.password,font=("arial",13,BOLD),show="*")
        # entrypass.place(x=130,y=270)





        inbtt=Button(frame,text="Send OTP",command=self.forgot,bd=3,relief=RIDGE,bg="red",fg="white",font=("arial",13,BOLD))
        inbtt.place(x=20,y=230,width=120,height=35)
        
        pbtt=Button(frame,text="Send password",command=self.send,bd=3,relief=RIDGE,bg="red",fg="white",font=("arial",13,BOLD))
        pbtt.place(x=170,y=230,width=150,height=35)
    
    def forgot(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
        my_cursor=conn.cursor()
        my_cursor.execute("select user from login where email=%s ",(self.email.get(),))
        rows1=my_cursor.fetchone()
        if rows1=="":
            messagebox.showerror("Error","email is not registered",parent=self.root)
            
            
        else:
            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                

                # start TLS for security
                s.starttls()

                # Authentication
                s.login("hmsglory6318@gmail.com", "2020100169")

                # message to be sent
            

                # sending the mail
                self.y=str(self.x)
                s.sendmail("hmsglory6318@gmail.com",str(self.email.get()),str(self.x)+" This your is OTP")

                # terminating the session
                s.quit()
                messagebox.showinfo("success","OTP sent",parent=self.root)
            except:
                messagebox.showerror("error","Email is invalid",parent=self.root)

            
            
            

    def send(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
        my_cursor=conn.cursor()
        my_cursor.execute("select password from login where email=%s ",(self.email.get(),))
        rows2=my_cursor.fetchone()
        self.temp=rows2
        if(self.OTP.get()==""):
            messagebox.showerror("Error","Enter OTP",parent=self.root)

        
        elif str(self.OTP.get())==self.y:
            s = smtplib.SMTP('smtp.gmail.com', 587)
                

                # start TLS for security
            s.starttls()

                # Authentication
            s.login("hmsglory6318@gmail.com", "2020100169")

                # message to be sent
            

                # sending the mail
            s.sendmail("hmsglory6318@gmail.com",str(self.email.get()),str(rows2[0])+" is your Password for hotel glory admin")

                # terminating the session
            s.quit()
            messagebox.showinfo("success","Password sent",parent=self.root)
        else:
            messagebox.showerror("Error","Incorrect OTP",parent=self.root)




    



    



if __name__=="__main__":
    root=Tk()
    obj=for_window(root)
    root.mainloop()