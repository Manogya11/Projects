from tkinter import *
from tkinter import messagebox
from time import strftime
from datetime import datetime
import random
from tkinter.font import BOLD
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
class room:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Booking")
        self.root.geometry("1295x600+230+220")

        self.var_floor=StringVar()
        self.var_roomno=StringVar()
        self.var_roomt=StringVar()
        # self.var_roomt=StringVar()
        # self.var_roomno=StringVar()
        # self.var_days=StringVar()
        # self.var_meal=StringVar()
        # self.var_tax=StringVar()
        # self.var_st=StringVar()
        # self.var_gt=StringVar()

    #title
        
        Title=Label(self.root,text="Room Adding Department",bg="black",fg="gold",font=("times new roman",18,BOLD),relief=RIDGE)
        Title.place(x=0,y=0,width=1295,height=50)
        # Title.pack()
        
        #logo
        im2=Image.open("logo3.png")
        im2=im2.resize((100,40),Image.LANCZOS)
        self.photoim2=ImageTk.PhotoImage(im2)
        lbimg2=Label(self.root,image=self.photoim2,bd=0,relief=RIDGE)
        lbimg2.place(x=2,y=2,width=100,height=50)

        #left label
        lbframelft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Adding",padx=2,font=("times new roman",12,BOLD))
        lbframelft.place(x=5,y=50,width=540,height=340)


        lbl_floor=Label(lbframelft,text="Floor",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0)

        entry_floor=ttk.Entry(lbframelft,width=29,textvariable=self.var_floor,font=("arial",13,BOLD))
        entry_floor.grid(row=0,column=1,sticky=W)

        
        lbl_roomno=Label(lbframelft,text="Room No.",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0)

        entry_roomno=ttk.Entry(lbframelft,width=29,textvariable=self.var_roomno,font=("arial",13,BOLD))
        entry_roomno.grid(row=1,column=1,sticky=W)


       

          
        lbl_Type=Label(lbframelft,text="Room Type",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_Type.grid(row=2,column=0)

        combo_Type=ttk.Combobox(lbframelft,textvariable=self.var_roomt,font=("arial",12,BOLD),width=27,state="readonly")
        combo_Type["value"]=("Budget","Deluxe","Premium")
        combo_Type.current(0)
        combo_Type.grid(row=2,column=1)

        bttframe=Frame(lbframelft,bd=2,relief=RIDGE)
        bttframe.place(x=0,y=200,width=427,height=40)

        btt1=Button(bttframe,text="Add",font=("arial",12,BOLD),command=self.add_data,fg="silver",bg="black",width=8,padx=10)
        btt1.grid(row=0,column=0)

        btt2=Button(bttframe,text="Update",command=self.update,font=("arial",12,BOLD),fg="silver",bg="black",width=8,padx=10)
        btt2.grid(row=0,column=1)

        btt3=Button(bttframe,text="Delete",command=self.delete,font=("arial",12,BOLD),fg="silver",bg="black",width=8,padx=10)
        btt3.grid(row=0,column=2)

        btt4=Button(bttframe,command=self.reset,text="Reset",font=("arial",12,BOLD),fg="silver",bg="black",width=8,padx=10)
        btt4.grid(row=0,column=4)


        lblframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("times new roman",12,BOLD))
        lblframeright.place(x=600,y=55,width=600,height=350)

        

        #scrollbar
        scrolly=ttk.Scrollbar(lblframeright,orient=VERTICAL)
        scrollx=ttk.Scrollbar(lblframeright,orient=HORIZONTAL)
 
        #tablereal
        self.cust_table=ttk.Treeview(lblframeright,columns=("Floor","RoomNo","RoomType"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cust_table.xview)
        scrolly.config(command=self.cust_table.yview)


        #heading
        self.cust_table.heading("Floor",text="Floor")
        self.cust_table.heading("RoomNo",text="Room No.")
        self.cust_table.heading("RoomType",text="Room Type")
       



        self.cust_table["show"]="headings"

        self.cust_table.column("Floor",width=50)
        self.cust_table.column("RoomNo",width=50)
        self.cust_table.column("RoomType",width=50)
  
        self.cust_table.pack(fill=BOTH,expand=1)
        self.fetchd()
        self.cust_table.bind("<ButtonRelease-1>",self.get_cursor)



    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomno.get()=="" or self.var_roomt.get()=="":
            messagebox.showerror("Error","Every Field is required")
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",username="root",password="Priyank@123",database="ne")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),self.var_roomno.get(),self.var_roomt.get()))
                conn.commit()
                self.fetchd()
                conn.close()  
                messagebox.showinfo("Success","Room Has Been Inserted",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong{str(es)}",parent=self.root)

    def fetchd(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_table.delete(*self.cust_table.get_children())
            for i in rows:
                self.cust_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.cust_table.focus()
        content=self.cust_table.item(cursor_row)
        row=content["values"]
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])    
        self.var_roomt.set(row[2])    
        

    def delete(self):
        delete=messagebox.askyesno("Deletion","Do you want to Delete",parent=self.root)     
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
            my_cursor=conn.cursor()
            query="delete from details where floor=%s"
            value=(self.var_floor.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetchd()
        conn.close()


    def update(self):
        try: 
            conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set roomno=%s,roomtype=%s where floor=%s",(self.var_roomno.get(),self.var_roomt.get(),self.var_floor.get()))
            conn.commit()
            self.fetchd()
            conn.close()  
            messagebox.showinfo("Success","Customer Has Been Updated",parent=self.root)
        except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong{str(es)}",parent=self.root)
        
        
            

    def reset(self):
          
        self.var_floor.set("")    
         
        self.var_roomno.set("")    
        

if __name__=="__main__":
    root=Tk()
    obj=room(root)
    root.mainloop()