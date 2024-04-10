from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk



class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("HOSPITAL Management System")
        self.root.geometry("1295x550+230+225") 


        


         #_______________title_______________________

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #__________________logo____________________
        
        img2=Image.open("logo1.png")
        img2=img2.resize((100,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #_________________labelframe________________
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",15,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #__________________labels and entries________
        #___________________custname_________________
        lbl_cust_ref=Label(labelframeleft,text="CUSTOMER REF",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,font=("times new roman",13,"bold"))
        enty_ref.grid(row=0,column=1)

        #__________________________________mother name______________
        lbl_cust_ref=Label(labelframeleft,text="MOTHER NAME",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,font=("times new roman",13,"bold"))
        enty_ref.grid(row=1,column=1)


        #____________________________________gender combobox_____________
        lbl_cust_ref=Label(labelframeleft,text="GENDER",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=2,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=25,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)

        


        #___________________________________POSTCODE
        lbl_cust_ref=Label(labelframeleft,text="POST CODE",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=3,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,font=("times new roman",13,"bold"))
        enty_ref.grid(row=3,column=1)


        #______________________________________MOBILE NO
        lbl_cust_ref=Label(labelframeleft,text="MOBILE NO.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=4,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,font=("times new roman",13,"bold"))
        enty_ref.grid(row=4,column=1)

        #__________________________________________EMAIL
        lbl_cust_ref=Label(labelframeleft,text="EMAIL",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=5,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,font=("times new roman",13,"bold"))
        enty_ref.grid(row=5,column=1)


        #______________________________________NATIONALITY
        lbl_cust_ref=Label(labelframeleft,text="NATIONALITY",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=6,column=0,sticky=W)

        new=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=25,state="readonly")
        new["value"]=("INDIAN","AMERICAN","AFRICAN","Other")
        new.current(0)
        new.grid(row=6,column=1)








        #_______________________________________ID PROOF TYPE
        lbl_cust_ref=Label(labelframeleft,text="ID PROOF TYPE",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=7,column=0,sticky=W)


        combo_id=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=25,state="readonly")
        combo_id["value"]=("ADHAAR","PAN","VOTER ID","Other")
        combo_id.current(0)
        combo_id.grid(row=7,column=1)






        #________________________________________ID NUMBER
        lbl_cust_ref=Label(labelframeleft,text="ID NO.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=8,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,font=("times new roman",13,"bold"))
        enty_ref.grid(row=8,column=1)






        #_________________________________________ADDRESS
        lbl_cust_ref=Label(labelframeleft,text="ADDRESS",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=9,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=27,font=("times new roman",13,"bold"))
        enty_ref.grid(row=9,column=1)


        #___________________BUTTONS
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)


        btnAdd1=Button(btn_frame,text="ADD",font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd1.grid(row=0,column=0,padx=1)

        btnAdd2=Button(btn_frame,text="UPDATE",font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd2.grid(row=0,column=1,padx=1)


        btnAdd3=Button(btn_frame,text="DELETE",font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd3.grid(row=0,column=2,padx=1)


        btnAdd4=Button(btn_frame,text="RESET",font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd4.grid(row=0,column=3,padx=1)

        #__________________tabelframe

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and search system",font=("times new roman",13,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)

        lblsearchby=Label(Table_frame,font=("times new roman",13,"bold"),text="Search by :",bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(Table_frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile No.","Reference No.")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        search_entry=ttk.Entry(Table_frame,width=26,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=2)
         
        btnsearch=Button(Table_frame,text="Search",font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=2)

        btnshowall=Button(Table_frame,text="Show all",font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
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


   








if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()