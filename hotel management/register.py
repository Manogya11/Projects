from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import BOLD
import mysql.connector
import smtplib

class reg_window:
    def __init__(self,root):
        self.root=root
        self.root.title("registration")
        self.root.geometry("1550x1750+0+0")


        im1=Image.open("reg11.png")
        im1=im1.resize((1550,1750),Image.LANCZOS)
        self.photoim1=ImageTk.PhotoImage(im1)
        lbimg=Label(self.root,image=self.photoim1,bd=4)
        lbimg.place(x=0,y=0,width=1550,height=1750)

        frame=Frame(self.root,bg="pink")
        frame.place(x=610,y=170,width=340,height=450)

        im=Image.open("reg.png")
        im=im.resize((200,100),Image.LANCZOS)
        self.photoim=ImageTk.PhotoImage(im)
        lbimg1=Label(self.root,image=self.photoim,bg="WHITE",bd=4)
        lbimg1.place(x=700,y=175,width=200,height=100)
        self.username=StringVar()
        self.password=StringVar()
        self.mobile=StringVar()
        self.email=StringVar()


        # get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="BLUE")
        # get_str.place(x=95,y=120)


        user=Label(frame,text="User Name",font=("times new roman",15,"bold"),fg="RED",bg="WHITE")
        user.place(x=20,y=150)

        entryuser=ttk.Entry(frame,width=20,textvariable=self.username,font=("arial",13,BOLD))
        entryuser.place(x=130,y=150)


        mob=Label(frame,text=" Contact ",font=("times new roman",15,"bold"),fg="RED",bg="WHITE")
        mob.place(x=20,y=190)

        entrymob=ttk.Entry(frame,width=20,textvariable=self.mobile,font=("arial",13,BOLD))
        entrymob.place(x=130,y=190)

        email=Label(frame,text=" Email ID  ",font=("arial",13,BOLD),bg="WHITE",fg="RED")
        email.place(x=20,y=230)

        entryemail=ttk.Entry(frame,width=20,textvariable=self.email,font=("arial",13,BOLD))
        entryemail.place(x=130,y=230)

        
        passs=Label(frame,text="Password",font=("arial",13,BOLD),bg="WHITE",fg="RED")
        passs.place(x=20,y=270)

        entrypass=ttk.Entry(frame,width=20,textvariable=self.password,font=("arial",13,BOLD),show="*")
        entrypass.place(x=130,y=270)





        inbtt=Button(frame,text="Register",bd=3,relief=RIDGE,command=self.reg,bg="red",fg="white",font=("arial",13,BOLD))
        inbtt.place(x=110,y=350,width=120,height=35)

        # rbtt=Button(frame,text="Return",bd=3,relief=RIDGE,command=self.log,bg="red",fg="white",font=("arial",13,BOLD))
        # rbtt.place(x=110,y=360,width=120,height=35)

        # fbtt=Button(frame,text="Forgot Password",bd=3,relief=RIDGE,bg="red",fg="white",font=("arial",13,BOLD))
        # fbtt.place(x=170,y=360,width=150,height=35)

    # def log(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=login_window(self.new_window)

        




    def reg(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from login where email=%s ",(self.email.get(),))
        rows1=my_cursor.fetchone()

        if (self.username.get()=="")or (self.password.get()=="")or (self.email.get()=="")or (self.mobile.get()==""):
            messagebox.showerror("error","All fields are required",parent=self.root)
        elif rows1 != None:
             messagebox.showerror("error","Email is  already registered",parent=self.root)
        else:
            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                

                # start TLS for security
                s.starttls()

                # Authentication
                s.login("hmsglory6318@gmail.com", "2020100169")

                # message to be sent
            

                # sending the mail
                
                s.sendmail("hmsglory6318@gmail.com",str(self.email.get()),"Hello, "+str(self.username.get())+" You have registered successfully to the hotel glory")

                # terminating the session
                s.quit()
                my_cursor.execute("insert into login values(%s,%s,%s,%s)",(self.username.get(),self.password.get(),self.email.get(),self.mobile.get()))
                messagebox.showinfo("success","registration successful",parent=self.root)
                conn.commit()
                
            except:
                messagebox.showerror("error","Email does not exists",parent=self.root)
        conn.close()



        
        
        # my_cursor.execute("select * from login where user=%s and password=%s",(self.username.get(),self.password.get()))

        # rows=my_cursor.fetchone()
        # if rows==None:
        #     messagebox.showerror("Error","Invalid Details")
        # else:
        #     open_main=messagebox.askyesno("confirmation","Admin Only Area",parent=self.root)
        #     if open_main>0:
        #         self.new_window=Toplevel(self.root)
        #         self.app=HotelManagementSystem(self.new_window)
        #     else:
        #         if not open_main:
        #             return

    


            
       
        
        

if __name__=="__main__":
    root=Tk()
    obj=reg_window(root)
    root.mainloop()