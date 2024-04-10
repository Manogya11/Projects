from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("HOSPITAL Management System")
        self.root.geometry("1295x600+230+225") 


        #______________________varriables to database
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


         #_______________title_______________________

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #__________________logo____________________
        
        img2=Image.open("logo3.png")
        img2=img2.resize((100,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #_________________labelframe________________
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",15,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #__________________labels and entries________
        #___________________custref_________________
        lbl_cust_ref=Label(labelframeleft,text="CUSTOMER REF",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,textvariable=self.var_ref,font=("times new roman",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

        # custname
        lbl_cust_ref=Label(labelframeleft,text="CUSTOMER NAME",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,textvariable=self.var_cust_name,font=("times new roman",13,"bold"))
        enty_ref.grid(row=1,column=1)

        #__________________________________mother name______________
        lbl_cust_ref=Label(labelframeleft,text="MOTHER NAME",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=2,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,textvariable=self.var_mother,font=("times new roman",13,"bold"))
        enty_ref.grid(row=2,column=1)


        #____________________________________gender combobox_____________
        lbl_cust_ref=Label(labelframeleft,text="GENDER",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=25,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        


        #___________________________________POSTCODE
        lbl_cust_ref=Label(labelframeleft,text="POST CODE",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=4,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,textvariable=self.var_post,font=("times new roman",13,"bold"))
        enty_ref.grid(row=4,column=1)


        #______________________________________MOBILE NO
        lbl_cust_ref=Label(labelframeleft,text="MOBILE NO.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=5,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,textvariable=self.var_mobile,font=("times new roman",13,"bold"))
        enty_ref.grid(row=5,column=1)

        #__________________________________________EMAIL
        lbl_cust_ref=Label(labelframeleft,text="EMAIL",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=6,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,textvariable=self.var_email,font=("times new roman",13,"bold"))
        enty_ref.grid(row=6,column=1)


        #______________________________________NATIONALITY
        lbl_cust_ref=Label(labelframeleft,text="NATIONALITY",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=7,column=0,sticky=W)

        new=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=25,state="readonly")
        new["value"]=("INDIAN","AMERICAN","AFRICAN","Other")
        new.current(0)
        new.grid(row=7,column=1)








        #_______________________________________ID PROOF TYPE
        lbl_cust_ref=Label(labelframeleft,text="ID PROOF TYPE",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=8,column=0,sticky=W)


        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=25,state="readonly")
        combo_id["value"]=("ADHAAR","PAN","VOTER ID","Other")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)






        #________________________________________ID NUMBER
        lbl_cust_ref=Label(labelframeleft,text="ID NO.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=9,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,textvariable=self.var_id_number,font=("times new roman",13,"bold"))
        enty_ref.grid(row=9,column=1)






        #_________________________________________ADDRESS
        lbl_cust_ref=Label(labelframeleft,text="ADDRESS",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=10,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,textvariable=self.var_address,font=("times new roman",13,"bold"))
        enty_ref.grid(row=10,column=1)


        #___________________BUTTONS
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=425,width=412,height=40)


        btnAdd1=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd1.grid(row=0,column=0,padx=1)

        btnAdd2=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd2.grid(row=0,column=1,padx=1)


        btnAdd3=Button(btn_frame,text="DELETE",command=self.mdelete,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd3.grid(row=0,column=2,padx=1)


        btnAdd4=Button(btn_frame,text="RESET",command=self.reset,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd4.grid(row=0,column=3,padx=1)

        #__________________tabelframe

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and search system",font=("times new roman",13,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)

        lblsearchby=Label(Table_frame,font=("times new roman",13,"bold"),text="Search by :",bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.searchv=StringVar()

        combo_search=ttk.Combobox(Table_frame,textvariable=self.searchv,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("mobile","reference")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.searcht=StringVar()

        search_entry=ttk.Entry(Table_frame,textvariable=self.searcht,width=26,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=2)
         
        btnsearch=Button(Table_frame,text="Search",command=self.search,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=2)

        btnshowall=Button(Table_frame,command=self.fetch_data,text="Show all",font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=2)


        #_________________show data
        details_frame=Frame(Table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=350)


        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)


        self.cust_details_Table=ttk.Treeview(details_frame,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_Table.xview)
        scroll_y.config(command=self.cust_details_Table.yview)

        #__________________________________table
        self.cust_details_Table.heading("ref",text="Refer no.")
        self.cust_details_Table.heading("name",text="Name")
        self.cust_details_Table.heading("mother",text="Mother Name")
        self.cust_details_Table.heading("gender",text="Gender")
        self.cust_details_Table.heading("post",text="Postcode")
        self.cust_details_Table.heading("mobile",text="Mobile")
        self.cust_details_Table.heading("email",text="Email")
        self.cust_details_Table.heading("nationality",text="Nationality")
        self.cust_details_Table.heading("idproof",text="Id Proof")
        self.cust_details_Table.heading("idnumber",text="Id number")
        self.cust_details_Table.heading("address",text="Address")

        self.cust_details_Table["show"]="headings"

        self.cust_details_Table.column("ref",width=100)
        self.cust_details_Table.column("name",width=100)
        self.cust_details_Table.column("mother",width=100)
        self.cust_details_Table.column("gender",width=100)
        self.cust_details_Table.column("post",width=100)
        self.cust_details_Table.column("mobile",width=100)
        self.cust_details_Table.column("email",width=100)
        self.cust_details_Table.column("nationality",width=100)
        self.cust_details_Table.column("idproof",width=100)
        self.cust_details_Table.column("idnumber",width=100)
        self.cust_details_Table.column("address",width=100)


        self.cust_details_Table.pack(fill=BOTH,expand=1)
        self.cust_details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="ne")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                                    self.var_cust_name.get(),
                                                                                                    self.var_mother.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_post.get(),
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_nationality.get(),
                                                                                                    self.var_id_proof.get(),
                                                                                                    self.var_id_number.get(),
                                                                                                    self.var_address.get()))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning",f"Some thing went wrong :{str(es)}",parent=self.root)                                                                                   


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="ne")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_Table.delete(*self.cust_details_Table.get_children())
            for i in rows:
                self.cust_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_rows=self.cust_details_Table.focus()
        content=self.cust_details_Table.item(cursor_rows)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter a mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="ne")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s,mother=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where reference=%s",(self.var_cust_name.get(),
                                                                                                                                                                                    self.var_mother.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_post.get(),
                                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                                                    self.var_id_proof.get(),
                                                                                                                                                                                    self.var_id_number.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_ref.get()))
    

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfuly",parent=self.root)

    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel management system","Do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="ne")
            my_cursor=conn.cursor()
            query="delete from customer where reference=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        
        self.var_id_number.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):
           
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="ne")
            my_cursor=conn.cursor()

            my_cursor.execute("select * from customer where "+str(self.searchv.get())+" LIKE '%"+str(self.searcht.get())+"%'")
        
            rows=my_cursor.fetchall()
           
            if len (rows)==0:
                messagebox.showerror("Error","number does not exists",parent=self.root)
            else:
                self.cust_details_Table.delete(*self.cust_details_Table.get_children())
                for i in rows:
                    self.cust_details_Table.insert("",END,values=i)
                conn.commit()
            conn.close()
            

        












if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop() 