from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import BOLD
import mysql.connector
from hotel import HotelManagementSystem
from register import reg_window
conn=mysql.connector.connect(host="localhost",user="root",password="Priyank@123",database="ne")
my_cursor=conn.cursor()
query="delete from login where user=%s"
value=("Priyank",)
my_cursor.execute(query,value)
conn.commit()
conn.close()
