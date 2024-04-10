import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def capture_image():
    print("Capture image")

def take_attendance():
    print("Take attendance")

def update_details():
    print("Update details")

def delete_details():
    print("Delete details")

def show_attendance():
    print("Show attendance")

def show_attendance_details():
    print("Show attendance details")

def exit_program():
    root.destroy()

root = tk.Tk()
root.geometry("800x600")
root.configure(bg="#FFFACD")

# Load logo image and resize
logo_image = Image.open("srms_logo.png")
logo_image = logo_image.resize((200, 75), Image.BICUBIC)  # Adjust the size as needed
logo_image = ImageTk.PhotoImage(logo_image)

# Logo
logo_label = tk.Label(root, image=logo_image, bg="#FFFACD")
logo_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Custom Style for Buttons
button_style = ttk.Style()
button_style.configure("Custom.TButton", font=("Arial", 12))

# Title
title = tk.Label(root, text="Automated Face Recognition Attendance System", font=("Arial", 20, "bold"), bg="#FFFACD", fg="#880808")
title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# List box
listbox = tk.Listbox(root, width=40, height=15)
listbox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Left side buttons
left_button_frame = tk.Frame(root, bg="#FFFACD")
left_button_frame.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

capture_image_button = ttk.Button(left_button_frame, text="Capture image", command=capture_image, width=15, style="Custom.TButton")
capture_image_button.pack(pady=5)

take_attendance_button = ttk.Button(left_button_frame, text="Take attendance", command=take_attendance, width=15, style="Custom.TButton")
take_attendance_button.pack(pady=5)

update_details_button = ttk.Button(left_button_frame, text="Update details", command=update_details, width=15, style="Custom.TButton")
update_details_button.pack(pady=5)

# Right side buttons
right_button_frame = tk.Frame(root, bg="#FFFACD")
right_button_frame.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

delete_details_button = ttk.Button(right_button_frame, text="Delete details", command=delete_details, width=15, style="Custom.TButton")
delete_details_button.pack(pady=5)

show_attendance_button = ttk.Button(right_button_frame, text="Show attendance", command=show_attendance, width=15, style="Custom.TButton")
show_attendance_button.pack(pady=5)

show_attendance_details_button = ttk.Button(right_button_frame, text="Show attendance details", command=show_attendance_details, width=15, style="Custom.TButton")
show_attendance_details_button.pack(pady=5)

# Exit button
exit_button = ttk.Button(root, text="Exit", command=exit_program, style="Custom.TButton", width=15)
exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

root.mainloop()
