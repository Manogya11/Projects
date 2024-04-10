from tkinter import messagebox
from tkinter import *
from time import strftime
from datetime import datetime
import random
from tkinter.font import BOLD
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
class roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Booking")
        self.root.geometry("1295x600+230+220")

        ###variables
        self.var_contact=StringVar()
        self.var_CheckIn=StringVar()
        self.var_CheckOut=StringVar()
        self.var_roomt=StringVar()
        self.var_roomno=StringVar()
        self.var_days=StringVar()
        self.var_meal=StringVar()
        self.var_tax=StringVar()
        self.var_st=StringVar()
        self.var_gt=StringVar()
        self.paid=StringVar()
        # self.var_CheckIn=StringVar()


        #title
        
        Title=Label(self.root,text="Room Booking",bg="black",fg="gold",font=("times new roman",18,BOLD),relief=RIDGE)
        Title.place(x=0,y=0,width=1295,height=50)
        # Title.pack()
        
        #logo
        im2=Image.open("logo3.png")
        im2=im2.resize((100,40),Image.LANCZOS)
        self.photoim2=ImageTk.PhotoImage(im2)
        lbimg2=Label(self.root,image=self.photoim2,bd=0,relief=RIDGE)
        lbimg2.place(x=0,y=0,width=100,height=50)

        #left label
        lbframelft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",padx=2,font=("times new roman",12,BOLD))
        lbframelft.place(x=5,y=50,width=440,height=490)

        lbl_No=Label(lbframelft,text="Contact",font=("arial",12,BOLD),padx=2,pady=4)
        lbl_No.grid(row=0,column=0)

        entry_No=ttk.Entry(lbframelft,width=25,textvariable=self.var_contact,font=("arial",13,BOLD))
        entry_No.grid(row=0,column=1,sticky=W)

        bttdata=Button(lbframelft,text="Fetch",command=self.fetchdata,font=("arial",10,BOLD),fg="silver",bg="black",width=8)
        bttdata.place(x=345,y=4)

        lbl_chkin=Label(lbframelft,text="Check In",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_chkin.grid(row=1,column=0)

        entry_chkin=ttk.Entry(lbframelft,width=29,textvariable=self.var_CheckIn,font=("arial",13,BOLD))
        entry_chkin.grid(row=1,column=1,sticky=W)


        lbl_chkout=Label(lbframelft,text="Check Out",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_chkout.grid(row=2,column=0)

        entry_chkout=ttk.Entry(lbframelft,width=29,textvariable=self.var_CheckOut,font=("arial",13,BOLD))
        entry_chkout.grid(row=2,column=1,sticky=W)

          
        lbl_Type=Label(lbframelft,text="Room Type",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_Type.grid(row=3,column=0)

        conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomtype from details")
        ro=my_cursor.fetchall()

        combo_Type=ttk.Combobox(lbframelft,textvariable=self.var_roomt,font=("arial",12,BOLD),width=27,state="readonly")
        combo_Type["value"]=ro
        combo_Type.current(0)
        combo_Type.grid(row=3,column=1)


        lbl_RoomNo=Label(lbframelft,text="Room No.",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_RoomNo.grid(row=4,column=0)

        conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()

        combo_roomno=ttk.Combobox(lbframelft,textvariable=self.var_roomno,font=("arial",12,BOLD),width=27,state="readonly")
        combo_roomno["value"]=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1,sticky=W)

        # entry_RoomNo=ttk.Entry(lbframelft,width=29,textvariable=self.var_roomno,font=("arial",13,BOLD))
        # entry_RoomNo.grid(row=4,column=1,sticky=W)


        lbl_Meal=Label(lbframelft,text="Meal",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_Meal.grid(row=5,column=0)

        # entry_meal=ttk.Entry(lbframelft,width=29,font=("arial",13,BOLD))
        # entry_meal.grid(row=5,column=1,sticky=W)
        combo_meal=ttk.Combobox(lbframelft,textvariable=self.var_meal,font=("arial",12,BOLD),width=27,state="readonly")
        combo_meal["value"]=("Lunch","Dinner","Breakfast")
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1)


        lbl_days=Label(lbframelft,text="No of Days",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_days.grid(row=6,column=0)

        entry_days=ttk.Entry(lbframelft,width=29,textvariable=self.var_days,font=("arial",13,BOLD),state="readonly")
        entry_days.grid(row=6,column=1,sticky=W)



        lbl_tax=Label(lbframelft,text="Paid Tax",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_tax.grid(row=7,column=0)

        entry_tax=ttk.Entry(lbframelft,width=29,textvariable=self.var_tax,font=("arial",13,BOLD))
        entry_tax.grid(row=7,column=1,sticky=W)


        lbl_sub=Label(lbframelft,text="Sub Total",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_sub.grid(row=8,column=0)

        entry_sub=ttk.Entry(lbframelft,width=29,textvariable=self.var_st,font=("arial",13,BOLD))
        entry_sub.grid(row=8,column=1,sticky=W)


        lbl_Total=Label(lbframelft,text="Total Cost",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_Total.grid(row=9,column=0)

        entry_Total=ttk.Entry(lbframelft,width=29,textvariable=self.var_gt,font=("arial",13,BOLD))
        entry_Total.grid(row=9,column=1,sticky=W)

        #bttn1
        bttbill=Button(lbframelft,text="Bill",font=("arial",12,BOLD),command=self.total,fg="silver",bg="black",width=8,padx=10)
        bttbill.grid(row=10,column=0,sticky=W)
        # bttbil=Entry(lbframelft,font=("arial",12,BOLD),textvariable=self.paid,fg="silver",width=8)
        # bttbil.grid(row=10,column=4,sticky=W)

        combo_l=ttk.Combobox(lbframelft,textvariable=self.paid,font=("arial",12,BOLD),width=27,state="readonly")
        combo_l["value"]=("Paid","Unpaid")
        combo_l.current(0)
        combo_l.grid(row=10,column=3)
        combo_l.place(x=300,y=350)
        #button frame
        bttframe=Frame(lbframelft,bd=2,relief=RIDGE)
        bttframe.place(x=0,y=400,width=427,height=40)

        #bttn1
        btt1=Button(bttframe,text="Add",font=("arial",12,BOLD),command=self.add_data,fg="silver",bg="black",width=8,padx=10)
        btt1.grid(row=0,column=0)

        btt2=Button(bttframe,text="Update",font=("arial",12,BOLD),command=self.update,fg="silver",bg="black",width=8,padx=10)
        btt2.grid(row=0,column=1)

        btt3=Button(bttframe,text="Delete",font=("arial",12,BOLD),command=self.delete,fg="silver",bg="black",width=8,padx=10)
        btt3.grid(row=0,column=2)

        btt4=Button(bttframe,text="Reset",command=self.reset,font=("arial",12,BOLD),fg="silver",bg="black",width=8,padx=10)
        btt4.grid(row=0,column=4)



        im7=Image.open("imgy.png")
        im7=im7.resize((500,300),Image.LANCZOS)
        self.photoim7=ImageTk.PhotoImage(im7)
        lbimg7=Label(self.root,image=self.photoim7,bd=0,relief=RIDGE)
        lbimg7.place(x=760,y=55,width=500,height=300)

         ############################################################part2
        lblframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("times new roman",12,BOLD))
        lblframeright.place(x=435,y=280,width=860,height=260)

        lbl_search=Label(lblframeright,text="Search Detail By",font=("arial",12,BOLD),padx=2,pady=6,bg="red",fg="gold")
        lbl_search.grid(row=0,column=0)

        self.searchv=StringVar()
        comboser=ttk.Combobox(lblframeright,textvariable=self.searchv,font=("arial",12,BOLD),width=20,state="readonly")
        comboser["value"]=("contact","RoomNo")
        comboser.current(0)
        comboser.grid(row=0,column=2,padx=2)

        self.txtv=StringVar()

        entry_ser=ttk.Entry(lblframeright,width=25,textvariable=self.txtv,font=("arial",13,BOLD))
        entry_ser.grid(row=0,column=3,sticky=W,padx=2)

        bttsrch=Button(lblframeright,text="Search",font=("arial",12,BOLD),command=self.search,fg="gold",bg="black",width=8,padx=10)
        bttsrch.grid(row=0,column=4)



        bttshowall=Button(lblframeright,text="Show All",command=self.fetchd,font=("arial",12,BOLD),fg="gold",bg="black",width=8,padx=10)
        bttshowall.grid(row=0,column=5)


        #dataframe
        tableframe=Frame(lblframeright,bd=2,relief=RIDGE)
        tableframe.place(x=0,y=50,width=860,height=180)

        #scrollbar
        scrolly=ttk.Scrollbar(tableframe,orient=VERTICAL)
        scrollx=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
 
        #tablereal
        self.cust_table=ttk.Treeview(tableframe,columns=("Contact","Check In","Check Out","RoomType","Room No","Meal","No Of Days","Paid Tax","Sub Total","Total Cost","Status"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cust_table.xview)
        scrolly.config(command=self.cust_table.yview)


        #heading
        self.cust_table.heading("Contact",text="Contact")
        self.cust_table.heading("Check In",text="Check In")
        self.cust_table.heading("Check Out",text="Check Out")
        self.cust_table.heading("RoomType",text="Type")
        self.cust_table.heading("Room No",text="Room No.")
        self.cust_table.heading("Meal",text="Meal")
        self.cust_table.heading("No Of Days",text="No. Of Days")
        self.cust_table.heading("Paid Tax",text="Paid Tax")
        self.cust_table.heading("Sub Total",text="Sub Total")
        self.cust_table.heading("Total Cost",text="Total Cost")
        self.cust_table.heading("Status",text="Status")

       



        self.cust_table["show"]="headings"

        self.cust_table.column("Contact",width=150)
        self.cust_table.column("Check In",width=150)
        self.cust_table.column("Check Out",width=150)
        self.cust_table.column("RoomType",width=150)
        self.cust_table.column("Room No",width=150)
        self.cust_table.column("Meal",width=150)
        self.cust_table.column("No Of Days",width=150)
        self.cust_table.column("Paid Tax",width=150)
        self.cust_table.column("Sub Total",width=150)
        self.cust_table.column("Total Cost",width=150)
        self.cust_table.column("Status",width=150)
        


        self.cust_table.pack(fill=BOTH,expand=1)
        self.fetchd()
        self.cust_table.bind("<ButtonRelease-1>",self.get_cursor)

    def fetchdata(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact No.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
            my_cursor=conn.cursor()
            # my_cursor.execute("select Name from customer where Mobile=%s"),(self.var_contact)
            q=(("select name from customer where mobile=%s"))
            value=(self.var_contact.get(),)
            my_cursor.execute(q,value)
            rows=my_cursor.fetchone()
            if rows==None:
                messagebox.showerror("Error","This No. not exists",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showdata=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdata.place(x=455,y=55,width=300,height=180)
                blname=Label(showdata,text="Name:",font=("times new roman",12,BOLD))
                blname.place(x=0,y=0)

                lblname=Label(showdata,text=rows,font=("times new roman",12,BOLD))
                lblname.place(x=90,y=0)

                conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
                my_cursor=conn.cursor()
                q=(("select gender from customer where mobile=%s"))
                value=(self.var_contact.get(),)
                my_cursor.execute(q,value)
                rows=my_cursor.fetchone()

                blname=Label(showdata,text="Gender:",font=("times new roman",12,BOLD))
                blname.place(x=0,y=25)

                lblname=Label(showdata,text=rows,font=("times new roman",12,BOLD))
                lblname.place(x=90,y=25)

                conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
                my_cursor=conn.cursor()
                q=(("select email from customer where mobile=%s"))
                value=(self.var_contact.get(),)
                my_cursor.execute(q,value)
                rows=my_cursor.fetchone()

                blname=Label(showdata,text="Email:",font=("times new roman",12,BOLD))
                blname.place(x=0,y=50)

                lblname=Label(showdata,text=rows,font=("times new roman",12,BOLD))
                lblname.place(x=90,y=50)


                conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
                my_cursor=conn.cursor()
                q=(("select Idproof from customer where mobile=%s"))
                value=(self.var_contact.get(),)
                my_cursor.execute(q,value)
                rows=my_cursor.fetchone()

                blname=Label(showdata,text="ID Proof:",font=("times new roman",12,BOLD))
                blname.place(x=0,y=75)

                lblname=Label(showdata,text=rows,font=("times new roman",12,BOLD))
                lblname.place(x=90,y=75)


                conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
                my_cursor=conn.cursor()
                q=(("select Idnumber from customer where mobile=%s"))
                value=(self.var_contact.get(),)
                my_cursor.execute(q,value)
                rows=my_cursor.fetchone()

                blname=Label(showdata,text="IDNo:",font=("times new roman",12,BOLD))
                blname.place(x=0,y=100)

                lblname=Label(showdata,text=rows,font=("times new roman",12,BOLD))
                lblname.place(x=90,y=100)





    def add_data(self):
        if self.var_contact.get()=="" or self.var_CheckIn.get()=="" or self.var_CheckOut.get()=="" or self.var_roomt.get()=="" or self.var_roomno.get()=="" or self.var_meal.get()=="":
            messagebox.showerror("Error","Every Field is required")
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),self.var_CheckIn.get(),self.var_CheckOut.get(),self.var_roomt.get(),self.var_roomno.get(),self.var_meal.get(),self.var_days.get(),self.var_tax.get(),self.var_st.get(),self.var_gt.get(),self.paid.get()))
                conn.commit()
                self.fetchd()
                conn.close()  
                messagebox.showinfo("Success","Customer Has Been Inserted",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong{str(es)}",parent=self.root)

    def fetchd(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
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
        self.var_contact.set(row[0])
        self.var_CheckIn.set(row[1])
        self.var_CheckOut.set(row[2])
        self.var_roomt.set(row[3])
        self.var_roomno.set(row[4])
        self.var_meal.set(row[5])
        self.var_days.set(row[6])
        self.var_tax.set(row[7])
        self.var_st.set(row[8])
        self.var_gt.set(row[9])
        self.paid.set(row[10])

    def delete(self):
        delete=messagebox.askyesno("Deletion","Do you want to Delete",parent=self.root)     
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        elif not delete:
            return
        conn.commit()
        self.fetchd()
        conn.close()

    def update(self):
        
        if self.var_contact.get()=="" or self.var_CheckIn.get()=="" or self.var_CheckOut.get()=="" or self.var_roomt.get()=="" or self.var_roomno.get()=="" or self.var_meal.get()=="":
            messagebox.showerror("Error","Every Field is required")
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
                my_cursor=conn.cursor()
                my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,roomno=%s,meal=%s,days=%s,Tax=%s,Sub=%s,Total=%s,status=%s where contact=%s",(self.var_CheckIn.get(),self.var_CheckOut.get(),self.var_roomt.get(),self.var_roomno.get(),self.var_meal.get(),self.var_days.get(),self.var_tax.get(),self.var_st.get(),self.var_gt.get(),self.paid.get(),self.var_contact.get()))
                conn.commit()
                self.fetchd()
                conn.close()  
                messagebox.showinfo("Success","Customer Has Been Updated",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong{str(es)}",parent=self.root)

    def reset(self):
        # self.var_ref.set("")
        self.var_contact.set("")    
        self.var_CheckIn.set("")    
        # self.gender_var.set("")    
        self.var_CheckOut.set("")    
        # self.var_roomt.set("")    
        self.var_roomno.set("")    
        # self.nationality_var.set("")    
        # self.idproof_var.set("")    
        # self.var_meal.set("")    
        self.var_days.set("")    
        self.var_tax.set("")
        self.var_st.set("")
        self.var_gt.set("")
        
        # x=random.randint(1000,99999)
        # self.var_ref.set(str(x))

    def total(self):
        q1=0
        q2=0
        inDate=self.var_CheckIn.get()
        outDate=self.var_CheckOut.get()
        inDate=datetime.strptime(inDate, "%d/%m/%Y")
        outDate=datetime.strptime(outDate, "%d/%m/%Y")
        self.var_days.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Breakfast" and self.var_roomt.get()=="Budget"):
            q1=float(100)
            q2=float(1000)

        elif(self.var_meal.get()=="Lunch" and self.var_roomt.get()=="Budget"):
            q1=float(200)
            q2=float(1000)

        elif(self.var_meal.get()=="Dinner" and self.var_roomt.get()=="Budget"):
            q1=float(300)
            q2=float(1000)

        elif(self.var_meal.get()=="Breakfast" and self.var_roomt.get()=="Deluxe"):
            q1=float(200)
            q2=float(2000)

        elif(self.var_meal.get()=="Lunch" and self.var_roomt.get()=="Deluxe"):
            q1=float(400)
            q2=float(2000)

        elif(self.var_meal.get()=="Dinner" and self.var_roomt.get()=="Deluxe"):
            q1=float(500)
            q2=float(2000)

        elif(self.var_meal.get()=="Lunch" and self.var_roomt.get()=="Premium"):
            q1=float(800)
            q2=float(4000)

        elif(self.var_meal.get()=="Breakfast" and self.var_roomt.get()=="Premium"):
            q1=float(400)
            q2=float(4000)

        elif(self.var_meal.get()=="Dinner" and self.var_roomt.get()=="Premium"):
            q1=float(1000)
            q2=float(4000)


        q3=float(self.var_days.get())
        q4=float(q1+q2)
        q5=float(q4*q3)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        gt="Rs."+str("%.2f"%(q5+(q5)*0.1))
        self.var_gt.set(gt)
        self.var_st.set(ST)
        self.var_tax.set(Tax)   
             
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.searchv.get())+" LIKE '%"+str(self.txtv.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)==0:
                messagebox.showerror("Error","number does not exists",parent=self.root)
        else:
            self.cust_table.delete(*self.cust_table.get_children())
            for i in rows:
                self.cust_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        
                  


if __name__=="__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()