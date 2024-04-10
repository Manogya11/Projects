import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
from datetime import datetime
import time
from mtcnn import MTCNN
from facenet_pytorch import MTCNN, InceptionResnetV1, prewhiten, training
import torch
import firebase_admin
from firebase_admin import credentials, db, storage
import face_recognition
import pickle

# Initialize global variables
encodeListKnown = []
studentIds = []

# Initialize a dictionary to keep track of last attendance marking time for each student
last_attendance_time = {}

# Initialize Firebase
def initialize_firebase(app_name=None):
    if not firebase_admin._apps:
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': "https://face-recognition-94653-default-rtdb.firebaseio.com/"
        }, name=app_name)

# Function to generate the encoding file
def generate_encode_file():
    # Import EncodeGenerator here
    import EncodeGenerator

    # Importing student images
    folderPath = 'Images'
    pathList = os.listdir(folderPath)
    imgList = []
    studentIds = []
    for path in pathList:
        imgList.append(cv2.imread(os.path.join(folderPath, path)))
        studentIds.append(os.path.splitext(path)[0])

        fileName = f'{folderPath}/{path}'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)

    def findEncodings(imagesList):
        encodeList = []
        for img in imagesList:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)
            if len(encode) > 0: # If faces are detected, add their encodings to the list
                encodeList.append(encode[0])

        return encodeList

    encodeListKnown = findEncodings(imgList)
    encodeListKnownWithIds = [encodeListKnown, studentIds]

    file = open("EncodeFile.p", 'wb')
    pickle.dump(encodeListKnownWithIds, file)
    file.close()

# Call the function to generate the encoding file
generate_encode_file()

# Initialize Tkinter
root = tk.Tk()
root.geometry("800x600")
root.configure(bg="#FFFACD")
root.title("Face Recognition Attendance System")

# Load logo image and resize
logo_image = Image.open("srms_logo.png")
logo_image = logo_image.resize((200, 75), Image.BICUBIC)  # Adjust the size as needed
logo_image = ImageTk.PhotoImage(logo_image)

# Logo
logo_label = tk.Label(root, image=logo_image, bg="#FFFACD")
logo_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Title
title = tk.Label(root, text="Automated Face Recognition Attendance System", font=("Arial", 20, "bold"), bg="#FFFACD", fg="#880808")
title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

def mark_attendance(student_id):
    global last_attendance_time
    
    # Get current time
    current_time = time.time()
    
    # Check if the student has been marked recently (within 30 seconds)
    if student_id in last_attendance_time:
        if current_time - last_attendance_time[student_id] < 30:
            return False  # Return False to indicate attendance not marked
    
    try:
        # Get a reference to the student's attendance record
        attendance_ref = db.reference(f'Students/{student_id}/total_attendance')
        
        # Increment the total attendance count
        attendance_ref.transaction(lambda current_value: (current_value or 0) + 1)

        # Update the last attendance time
        db.reference(f'Students/{student_id}/last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        # Update the last attendance marking time for the student
        last_attendance_time[student_id] = current_time
        
        # You can add more complex logic here if needed
        
        return True  # Return True to indicate successful attendance marking
    except Exception as e:
        print(f"Error marking attendance for student ID {student_id}: {e}")
        return False  # Return False to indicate failure

def process_video_feed():
    global encodeListKnown, studentIds
    
    # Load the updated encoding list
    with open('EncodeFile.p', 'rb') as file:
        encodeListKnownWithIds = pickle.load(file)
    encodeListKnown, studentIds = encodeListKnownWithIds

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    mtcnn = MTCNN(keep_all=True, device=device)

    while True:
        success, img = cap.read()

        if not success:
            print("Failed to read frame from camera.")
            continue

        imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        boxes, _ = mtcnn.detect(imgS)

        if boxes is not None and len(boxes) > 0:  # Check if faces are detected
            # Initialize a list to keep track of marked attendance
            marked_attendance = []

            # Perform recognition on individual faces
            for box in boxes:
                box = [int(coord) for coord in box]
                top, right, bottom, left = box
                
                face_img = img[top:bottom, left:right]
                
                if face_img is not None and len(face_img) > 0:  # Check if face image is valid
                    face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
                    
                    # Resize and preprocess the face image for recognition
                    face_img = cv2.resize(face_img, (160, 160))
                    face_img = prewhiten(face_img)

                    # Convert to tensor
                    face_tensor = torch.tensor(face_img[np.newaxis], dtype=torch.float32).to(device)

                    # Encode the face using FaceNet
                    encode = model(face_tensor).detach().cpu().numpy()

                    # Initialize a variable to store the best match
                    best_match_index = None

                    if len(encode) > 0:
                        matches = face_recognition.compare_faces(encodeListKnown, encode[0])
                        face_distances = face_recognition.face_distance(encodeListKnown, encode[0])

                        if len(face_distances) > 0:
                            best_match_index = np.argmin(face_distances)
                            if matches[best_match_index] and studentIds[best_match_index] not in marked_attendance:
                                # Mark attendance if face matches and it hasn't been marked already
                                marked_attendance.append(studentIds[best_match_index])
                                mark_attendance(studentIds[best_match_index])

                    # Draw bounding box and label
                    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(img, f"{best_match_index} - {studentIds[best_match_index] if best_match_index is not None else 'Unknown'}",
                                (left, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to capture images and add new students
def capture_images():
    global encodeListKnown, studentIds  # Ensure we're using the global variables
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        cv2.imshow("Capture Images", img)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Ask for student details
            student_id = simpledialog.askstring("Capture Images", "Enter Student ID:")
            name = simpledialog.askstring("Capture Images", "Enter Student Name:")
            branch = simpledialog.askstring("Capture Images", "Enter Student Branch:")
            starting_year = simpledialog.askinteger("Capture Images", "Enter Starting Year:")
            year = simpledialog.askinteger("Capture Images", "Enter Student Year:")

            if student_id and name and branch and starting_year is not None and year is not None:
                # Save image with student_id as filename
                img_path = f"images/{student_id}.jpg"
                cv2.imwrite(img_path, img)

                # Update database with student details
                ref = db.reference(f'Students/{student_id}')
                ref.set({
                    'name': name,
                    'branch': branch,
                    'starting_year': starting_year,
                    'total_attendance': 0,
                    'year': year,
                    'last_attendance_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

                print("Student details added successfully!")

                # Call the function to generate the encoding file
                generate_encode_file()

                # Reload the encoder and database modules
                import EncodeGenerator
                import Database

                # Reload the database to include the new student
                import importlib
                importlib.reload(Database)

                # Load the updated encoding list
                with open('EncodeFile.p', 'rb') as file:
                    encodeListKnownWithIds = pickle.load(file)
                    encodeListKnown, studentIds = encodeListKnownWithIds

                # Update the student listbox
                update_student_listbox()

                break
            else:
                messagebox.showwarning("Warning", "Invalid input or canceled operation.")

        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to take attendance
def take_attendance():
    # Load the updated encoding list
    with open('EncodeFile.p', 'rb') as file:
        encodeListKnownWithIds = pickle.load(file)
    encodeListKnown, studentIds = encodeListKnownWithIds

    # Call the process_video_feed function with the updated encoding data
    process_video_feed()

# Function to update the student details
def update_student(student_id):
    student_info_ref = db.reference(f'Students/{student_id}')
    student_info = student_info_ref.get()
    # Ask for updated student details
    name = simpledialog.askstring("Update Student", "Enter Updated Student Name:",
                                  initialvalue=student_info['name'])
    branch = simpledialog.askstring("Update Student", "Enter Updated Student Branch:",
                                    initialvalue=student_info['branch'])
    starting_year = simpledialog.askinteger("Update Student", "Enter Updated Starting Year:",
                                             initialvalue=student_info['starting_year'])
    year = simpledialog.askinteger("Update Student", "Enter Updated Student Year:",
                                    initialvalue=student_info['year'])

    # Update the student details in the database
    student_info_ref.update({
        'name': name,
        'branch': branch,
        'starting_year': starting_year,
        'year': year,
        'last_attendance_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print("Student details updated successfully!")
    
# Function to delete the student details
def delete_student():
    # Ask the user for the student ID to delete
    student_id = simpledialog.askstring("Delete Student", "Enter Student ID to delete:")
    if student_id:
        try:
            # Fetch the current list of student IDs from the database
            student_ids_ref = db.reference('Students').get()
            
            print("Student IDs from Firebase:", student_ids_ref.keys())  # Print student IDs from Firebase
            
            # Check if the student ID exists in the list
            if student_id in student_ids_ref:
                # Remove the student from the Firebase database
                db.reference(f'Students/{student_id}').delete()

                # Remove the student's encoded face from the list
                encoded_face_idx = studentIds.index(student_id)
                del encodeListKnown[encoded_face_idx]
                del studentIds[encoded_face_idx]

                # Remove the student's encoded face filename from the encoder file
                with open('EncodeFile.p', 'wb') as file:
                    pickle.dump((encodeListKnown, studentIds), file)

                # Delete the student's images from the local directory
                img_path = f"Images/{student_id}.jpg"
                if os.path.exists(img_path):
                    os.remove(img_path)

                print("Student deleted successfully!")

                # Update the student listbox after deletion
                update_student_listbox()
            else:
                messagebox.showwarning("Warning", f"Student with ID {student_id} does not exist.")
        except Exception as e:
            print(f"Error occurred while deleting student: {e}")
            messagebox.showerror("Error", f"An error occurred while deleting student: {e}")

# Function to manually adjust student attendance
def adjust_attendance():
    student_id = simpledialog.askstring("Adjust Attendance", "Enter Student ID:")
    if student_id:
        # Fetch the current attendance count
        attendance_ref = db.reference(f'Students/{student_id}/total_attendance')
        current_attendance = attendance_ref.get() or 0

        # Ask for the number of attendances to adjust
        adjustment_amount = simpledialog.askinteger("Adjust Attendance", "Enter the number of attendances to adjust:")
        if adjustment_amount is not None:
            # Update the attendance count in the database
            new_attendance = max(current_attendance + adjustment_amount, 0)  # Ensure it doesn't go below 0
            attendance_ref.set(new_attendance)
            print(f"Attendance for Student ID {student_id} adjusted successfully. New attendance: {new_attendance}")
        else:
            messagebox.showwarning("Warning", "Invalid input.")
            return

        # Update the attendance count in the database
        attendance_ref.set(new_attendance)
        print(f"Attendance for Student ID {student_id} adjusted successfully.")

def save_attendance_to_excel():
    try:
        # Fetch the latest student data from the Firebase database
        students_data = db.reference('Students').get()
        
        # Create a list to store student attendance data
        attendance_data = []
        
        # Add student details to the list
        for student_id, student_info in students_data.items():
            name = student_info.get('name', 'Unknown')
            branch = student_info.get('branch', 'Unknown')
            starting_year = student_info.get('starting_year', 'Unknown')
            year = student_info.get('year', 'Unknown')
            total_attendance = student_info.get('total_attendance', 0)
            last_attendance_time = student_info.get('last_attendance_time', 'Unknown')
            
            # Append a new dictionary to the list
            attendance_data.append({'Student ID': student_id,
                                    'Name': name,
                                    'Branch': branch,
                                    'Starting Year': starting_year,
                                    'Year': year,
                                    'Total Attendance': total_attendance,
                                    'Last Attendance Time': last_attendance_time})
        
        # Create a DataFrame from the list
        attendance_df_new = pd.DataFrame(attendance_data)
        
        # Check if the existing DataFrame is empty
        if 'attendance_df' not in globals():
            # If empty, assign the new DataFrame to it
            globals()['attendance_df'] = attendance_df_new
        else:
            # If not empty, concatenate the new DataFrame with the existing one
            globals()['attendance_df'] = pd.concat([attendance_df, attendance_df_new], ignore_index=True)
        
        # Save the DataFrame to an Excel file
        attendance_df.to_excel('student_attendance.xlsx', index=False)
        print("Student attendance details saved to 'student_attendance.xlsx'")
    except Exception as e:
        print(f"Error occurred while saving attendance to Excel: {e}")

# Function to display attendance
def show_attendance():
    # Fetch updated attendance data from Firebase
    attendance_ref = db.reference('Students')
    attendance_data = attendance_ref.get()

    # Create a window to display attendance
    attendance_window = tk.Toplevel(root)
    attendance_window.title("Attendance Details")
    attendance_window.geometry("600x400")

    # Add widgets to display attendance data
    for student_id, attendance_info in attendance_data.items():
        name = attendance_info.get('name', 'Unknown')
        total_attendance = attendance_info.get('total_attendance', 0)
        year = attendance_info.get('year', 'Unknown')

        label = tk.Label(attendance_window, text=f"{name} ({student_id}): {total_attendance} attendances in Year {year}")
        label.pack()

# Function to display complete student details
def display_student_details():
    # Fetch the latest student data from the Firebase database
    students_data = db.reference('Students').get()

    # Create a window to display student details
    student_details_window = tk.Toplevel(root)
    student_details_window.title("Student Details")
    student_details_window.geometry("600x400")

    # Add a scrollbar
    scrollbar = tk.Scrollbar(student_details_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a text widget
    text_area = tk.Text(student_details_window, yscrollcommand=scrollbar.set)
    text_area.pack(fill=tk.BOTH, expand=1)

    # Configure the scrollbar
    scrollbar.config(command=text_area.yview)

    # Add student details to the text widget
    text_area.insert(tk.END, "Student Details:\n\n")
    for student_id, student_info in students_data.items():
        name = student_info.get('name', 'Unknown')  # Get name with default value 'Unknown' if key 'name' is missing
        branch = student_info.get('branch', 'Unknown')
        starting_year = student_info.get('starting_year', 'Unknown')
        year = student_info.get('year', 'Unknown')
        total_attendance = student_info.get('total_attendance', 0)
        last_attendance_time = student_info.get('last_attendance_time', 'Unknown')
        text_area.insert(tk.END, f"Student ID: {student_id}\n")
        text_area.insert(tk.END, f"Name: {name}\n")  # Use the name retrieved with .get() method
        text_area.insert(tk.END, f"Branch: {branch}\n")
        text_area.insert(tk.END, f"Starting Year: {starting_year}\n")
        text_area.insert(tk.END, f"Year: {year}\n")
        text_area.insert(tk.END, f"Total Attendance: {total_attendance}\n")
        text_area.insert(tk.END, f"Last Attendance Time: {last_attendance_time}\n\n")

# Set the style for the buttons
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 12))

# Define the width and height of the buttons
button_width = 20
button_height = 2

# Create buttons for various operations
capture_button = ttk.Button(root, text="Capture Images", command=capture_images, style="Custom.TButton", width=button_width)
capture_button.place(relx=0.25, rely=0.45, anchor=tk.CENTER)

update_button = ttk.Button(root, text="Update Details", command=update_student, style="Custom.TButton", width=button_width)
update_button.place(relx=0.25, rely=0.55, anchor=tk.CENTER)

delete_button = ttk.Button(root, text="Delete Student Details", command=delete_student, style="Custom.TButton", width=button_width)
delete_button.place(relx=0.25, rely=0.65, anchor=tk.CENTER)

attendance_button = ttk.Button(root, text="Take Attendance", command=take_attendance, style="Custom.TButton", width=button_width)
attendance_button.place(relx=0.75, rely=0.45, anchor=tk.CENTER)

show_attendance_button = ttk.Button(root, text="Show Attendance", command=show_attendance, style="Custom.TButton", width=button_width)
show_attendance_button.place(relx=0.75, rely=0.55, anchor=tk.CENTER)

display_details_button = ttk.Button(root, text="Display Student Details", command=display_student_details, style="Custom.TButton", width=button_width)
display_details_button.place(relx=0.75, rely=0.65, anchor=tk.CENTER)

adjust_attendance_button = ttk.Button(root, text="Adjust Attendance", command=adjust_attendance, style="Custom.TButton", width=button_width)
adjust_attendance_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Create a listbox to display student details
student_listbox = tk.Listbox(root, width=40, height=20)
student_listbox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Function to update the student listbox
def update_student_listbox():
    student_listbox.delete(0, tk.END)  # Clear the listbox
    # Fetch the latest student data from the Firebase database
    students_data = db.reference('Students').get()
    # Add student details to the listbox
    for student_id, student_info in students_data.items():
        name = student_info.get('name', 'Unknown')
        branch = student_info.get('branch', 'Unknown')
        starting_year = student_info.get('starting_year', 'Unknown')
        year = student_info.get('year', 'Unknown')
        total_attendance = student_info.get('total_attendance', 0)
        last_attendance_time = student_info.get('last_attendance_time', 'Unknown')
        student_listbox.insert(tk.END, f"ID: {student_id}, Name: {name}, Branch: {branch}, Starting Year: {starting_year}, Year: {year}, Total Attendance: {total_attendance}, Last Attendance Time: {last_attendance_time}")

# Call the function to initially populate the student listbox
update_student_listbox()

# Function to exit the application
def exit_app():
    root.destroy()

# Adjusting the size of the exit button
exit_button = ttk.Button(root, text="Exit", command=exit_app, style="Custom.TButton", width=button_width)
exit_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# Set padding to adjust the button height
for button in (capture_button, update_button, delete_button, attendance_button, show_attendance_button, display_details_button, adjust_attendance_button, exit_button):
    button["padding"] = (button_height // 2, button_height // 2)

# Start the Tkinter event loop
root.mainloop()
