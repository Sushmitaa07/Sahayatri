import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

# Function to handle the login button click event
def login():
    email = entry_email.get()
    password = entry_password.get()
    
    conn = sqlite3.connect('sahayatri.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM register WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Login", "Login successful!")
        root.destroy()  # Close the login window
        subprocess.Popen(["python", "Dashboard.py"])  # Open the Dashboard.py page
    else:
        messagebox.showerror("Error", "Invalid email or password")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("1600x900")  # Increase the window size
root.configure(bg='#4a90e2')  # Blue background

# Load the background image
image_path = "traffic.webp"
image = Image.open(image_path)
image = image.resize((500, 500), Image.LANCZOS)  # Resize the image to fit in the middle
background_image = ImageTk.PhotoImage(image)

# Create a label for the image
label_image = tk.Label(root, image=background_image)
label_image.place(relx=0.7, rely=0.5, anchor='center')  # Place the image in the middle right

# Create a frame for the login form
frame_login = tk.Frame(root, bg='#dcdcdc', bd=2, relief='solid')
frame_login.place(relx=0.3, rely=0.5, anchor='center', width=350, height=250)  # Increase width and height

# Email label and entry
label_email = tk.Label(frame_login, text="Email", bg='#dcdcdc')
label_email.pack(pady=(20, 5))
entry_email = tk.Entry(frame_login, width=35)  # Increase width of the entry
entry_email.pack(pady=(0, 10))

# Password label and entry
label_password = tk.Label(frame_login, text="Password", bg='#dcdcdc')
label_password.pack(pady=(0, 5))
entry_password = tk.Entry(frame_login, show='*', width=35)  # Increase width of the entry
entry_password.pack(pady=(0, 10))

# Login button
button_login = tk.Button(frame_login, text="Log in", command=login, bg='#4a90e2', fg='white', bd=0)
button_login.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
