from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from tkinter.font import BOLD

class diabetes:
    dataset = pd.read_csv('diabetes_data_upload.csv')
    def __init__(self, root):
        self.root = root
        self.root.title("Diabetes Prediction")
        self.root.geometry("1360x800+0+0")
        self.Age = StringVar()
        self.gender = StringVar()
        self.polyuria = StringVar()
        self.polydypsia = StringVar()
        self.wl = StringVar()
        self.weak = StringVar()
        self.polyphagia = StringVar()
        self.gt = StringVar()
        self.blur = StringVar()
        self.itchr = StringVar()
        self.irr = StringVar()
        self.delay = StringVar()
        self.para = StringVar()
        self.muscle = StringVar()
        self.Alo = StringVar()
        self.obe = StringVar()

        self.main_frame = Frame(self.root, bd=0, bg="antique white", relief=SUNKEN)
        self.main_frame.place(x=0, y=0, width=1360, height=540)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Existing code...
          
        #title
        Title=Label(self.root,text="EARLY STAGE DIABETES DETECTION",bg="black",fg="gold",font=("times new roman",34),relief=RIDGE)
        Title.place(x=0,y=10,width=1360,height=50)
        # Title=Label(self.root,text="Answer the Given Questions",bg="black",fg="white",font=("times new roman",24),relief=RIDGE)
        # Title.place(x=0,y=60,width=1560,height=100)
    
        #frame menu
        frame1=Frame(self.root,bd=4,bg="antique white",relief=SUNKEN)
        frame1.place(x=0,y=60,width=1360,height=800)
        Title=Label(frame1,text="Enter Age",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=0,y=00,width=360,height=40)
        Title=Label(frame1,text="Gender(0 for male,1 for female)",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=0,y=50,width=360,height=40)
        Title=Label(frame1,text="Excessive Urine",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=0,y=100,width=360,height=40)
        Title=Label(frame1,text="Excessive Thirst",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=0,y=150,width=360,height=40)
        Title=Label(frame1,text="Sudden Weight Loss",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=0,y=200,width=360,height=40)
        Title=Label(frame1,text="Weakness",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=0,y=250,width=360,height=40)
        Title=Label(frame1,text="Excessive Hunger",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=0,y=300,width=360,height=40)
        Title=Label(frame1,text="Genetial Thrush",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=0,y=350,width=360,height=40)


        #label 2nd
        Title=Label(frame1,text="Blurred Vision",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=760,y=00,width=360,height=40)
        Title=Label(frame1,text="Itchiness",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=760,y=50,width=360,height=40)
        Title=Label(frame1,text="Frustration on Small matters",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=760,y=100,width=360,height=40)
        Title=Label(frame1,text="Delayed Healing",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=760,y=150,width=360,height=40)
        Title=Label(frame1,text="Partial Paralysis",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=760,y=200,width=360,height=40)
        Title=Label(frame1,text="Muscle Stiffness",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=760,y=250,width=360,height=40)
        Title=Label(frame1,text="Hair Loss from anywhere",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=760,y=300,width=360,height=40)
        Title=Label(frame1,text="Excessive Body Fat",bg="black",fg="white",font=("times new roman",20),relief=RIDGE)
        Title.place(x=760,y=350,width=360,height=40)
        

        entry=ttk.Entry(frame1,width=29,textvariable=self.Age,font=("arial",13,BOLD))
        entry.place(x=400,y=00,width=160,height=40)
        #entries
        c1=ttk.Combobox(frame1,textvariable=self.gender,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=400,y=50,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.polyuria,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=400,y=100,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.polydypsia,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=400,y=150,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.wl,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=400,y=200,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.weak,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=400,y=250,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.polyphagia,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=400,y=300,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.gt,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=400,y=350,width=160,height=40)


        c1=ttk.Combobox(frame1,textvariable=self.blur,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=1160,y=00,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.itchr,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=1160,y=50,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.irr,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=1160,y=100,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.delay,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=1160,y=150,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.para,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=1160,y=200,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.muscle,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=1160,y=250,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.Alo,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=1160,y=300,width=160,height=40)
        c1=ttk.Combobox(frame1,textvariable=self.obe,font=("arial",12,BOLD),width=27,state="readonly")
        c1["value"]=(0,1)
        c1.current(0)
        c1.place(x=1160,y=350,width=160,height=40)

        #submit Button
        b1=Button(frame1,text="Submit",command=self.result,width=22,bg="black",fg="gold",font=("times new roman",14,BOLD),relief=RIDGE)
        b1.place(x=540,y=420)
        
    def result(self):
        # Modify the result method to use the class attribute dataset
        X = diabetes.dataset.iloc[:, :-1].values
        y = diabetes.dataset.iloc[:, -1].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
        classifier.fit(X_train, y_train)
        val = classifier.predict(sc.transform([[int(self.Age.get()),
                                                 int(self.gender.get()),
                                                 int(self.polyuria.get()),
                                                 int(self.polydypsia.get()),
                                                 int(self.wl.get()),
                                                 int(self.weak.get()),
                                                 int(self.polyphagia.get()),
                                                 int(self.gt.get()),
                                                 int(self.blur.get()),
                                                 int(self.itchr.get()),
                                                 int(self.irr.get()),
                                                 int(self.delay.get()),
                                                 int(self.para.get()),
                                                 int(self.muscle.get()),
                                                 int(self.Alo.get()),
                                                 int(self.obe.get())]]))
        result_text = ""
        if val[0] == 0:
            result_text = "Negative - You have no signs of Diabetes"
        else:
            result_text = "Positive - You have signs of diabetes. Contact a Diabetic doctor."

        # Create a DataFrame with patient data and result
        patient_data = {
            'Age': [self.Age.get()],
            'Gender': [self.gender.get()],
            'Polyuria': [self.polyuria.get()],
            'Polydipsia': [self.polydypsia.get()],
            'Sudden Weight Loss': [self.wl.get()],
            'Weakness': [self.weak.get()],
            'Polyphagia': [self.polyphagia.get()],
            'Genital Thrush': [self.gt.get()],
            'Blurred Vision': [self.blur.get()],
            'Itching': [self.itchr.get()],
            'Irritability': [self.irr.get()],
            'Delayed Healing': [self.delay.get()],
            'Partial Paresis': [self.para.get()],
            'Muscle Stiffness': [self.muscle.get()],
            'Alopecia': [self.Alo.get()],
            'Obesity': [self.obe.get()],
            'Result': [result_text]
        }

        # Append the patient data to the existing dataset
        patient_df = pd.DataFrame(patient_data)
        updated_dataset = pd.concat([diabetes.dataset, patient_df], ignore_index=True)

        # Save the updated dataset to an Excel file
        updated_dataset.to_excel('diabetes_data_upload_with_results.xlsx', index=False)

        # Display result to the user
        frame1 = Frame(self.root, bd=0, bg="antique white", relief=SUNKEN)
        frame1.place(x=0, y=540, width=1560, height=250)

        if val[0] == 0:
            r1 = Label(frame1, text=f"Class: Negative \n {result_text}", bg="black", fg="white",
                       font=("times new roman", 24), relief=RIDGE)
        else:
            r1 = Label(frame1, text=f"Class: Positive \n {result_text}", bg="black", fg="white",
                       font=("times new roman", 24), relief=RIDGE)
        r1.place(x=350, y=20, height=80, width=700)

        b1 = Button(frame1, text="Okay", command=self.logout, width=22, bg="black", fg="gold",
                    font=("times new roman", 14, BOLD), relief=RIDGE)
        b1.place(x=540, y=120)

        y_pred = classifier.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        print(cm)
        print(accuracy_score(y_test, y_pred))
        
    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = diabetes(root)
    root.mainloop()
