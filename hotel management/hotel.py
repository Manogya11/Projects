from tkinter import*
from PIL import Image,ImageTk
from customer import cust_win
from room import roombooking
from details import room
from report import reportpg

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL Management System")
        self.root.geometry("1550x800+0+0")


        img1=Image.open("upp.png")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #__________________logo____________________
        
        img2=Image.open(r"logo3.png")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #_______________title_______________________

        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #____________Frame________________

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #___________menu___________________
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230,height=50)

        #____________Frame________________

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=45,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="BOOKING",command=self.room_book,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="ROOMS",command=self.room_add,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",command=self.dev_det,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOG OUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        #_____________________right image____________________________

        img3=Image.open("home.png")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)

    #    ______________________dowm images_____________________________

        img4=Image.open("r1.png")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=235,width=230,height=210)

        img5=Image.open("r2.png")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)

    def room_book(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)

    def room_add(self):
        self.new_window=Toplevel(self.root)
        self.app=room(self.new_window)

    def dev_det(self):
        self.new_window=Toplevel(self.root)
        self.app=reportpg(self.new_window)

    def logout(self):
        self.root.destroy()






        
if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root) 
    root.mainloop()