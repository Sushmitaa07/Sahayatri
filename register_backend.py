import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

# Function to create the database and user table
def create_database():
    conn = sqlite3.connect('sahayatri.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        license_no TEXT,
        contact_no TEXT,
        temp_address TEXT,
        perm_address TEXT,
        email TEXT,
        password TEXT
    )
    ''')
    conn.commit()
    conn.close()

# Function to handle the register button click event
def register():
    full_name = entry_full_name.get()
    license_no = entry_license.get()
    contact_no = entry_contact.get()
    temp_address = entry_temp_address.get()
    perm_address = entry_perm_address.get()
    email = entry_email.get()
    password = entry_password.get()

    if not full_name or not license_no or not contact_no or not temp_address or not perm_address or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Insert the user data into the database
    conn = sqlite3.connect('sahayatri.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (full_name, license_no, contact_no, temp_address, perm_address, email, password)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (full_name, license_no, contact_no, temp_address, perm_address, email, password))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Register", "Registration successful!")
    clear_entries()

# Function to clear the entry fields
def clear_entries():
    entry_full_name.delete(0, tk.END)
    entry_license.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    entry_temp_address.delete(0, tk.END)
    entry_perm_address.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Page")
root.geometry("1000x600")
root.configure(bg='#4a90e2')

# Load the background image
image_path = "traffic.webp"
image = Image.open(image_path)
image = image.resize((500, 500), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)

# Create a label for the image
label_image = tk.Label(root, image=background_image)
label_image.place(relx=0.75, rely=0.5, anchor='center')

# Create a frame for the registration form
frame_register = tk.Frame(root, bg='#dcdcdc', bd=2, relief='solid')
frame_register.place(relx=0.25, rely=0.5, anchor='center', width=400, height=500)

# Full name label and entry
label_full_name = tk.Label(frame_register, text="Full name", bg='#dcdcdc')
label_full_name.pack(pady=(10, 5))
entry_full_name = tk.Entry(frame_register, width=35)
entry_full_name.pack(pady=(0, 10))

# License number label and entry
label_license = tk.Label(frame_register, text="License no", bg='#dcdcdc')
label_license.pack(pady=(0, 5))
entry_license = tk.Entry(frame_register, width=35)
entry_license.pack(pady=(0, 10))

# Contact number label and entry
label_contact = tk.Label(frame_register, text="Contact no", bg='#dcdcdc')
label_contact.pack(pady=(0, 5))
entry_contact = tk.Entry(frame_register, width=35)
entry_contact.pack(pady=(0, 10))

# Temporary address label and entry
label_temp_address = tk.Label(frame_register, text="Temporary address", bg='#dcdcdc')
label_temp_address.pack(pady=(0, 5))
entry_temp_address = tk.Entry(frame_register, width=35)
entry_temp_address.pack(pady=(0, 10))

# Permanent address label and entry
label_perm_address = tk.Label(frame_register, text="Permanent address", bg='#dcdcdc')
label_perm_address.pack(pady=(0, 5))
entry_perm_address = tk.Entry(frame_register, width=35)
entry_perm_address.pack(pady=(0, 10))

# Email label and entry
label_email = tk.Label(frame_register, text="Email", bg='#dcdcdc')
label_email.pack(pady=(0, 5))
entry_email = tk.Entry(frame_register, width=35)
entry_email.pack(pady=(0, 10))

# Password label and entry
label_password = tk.Label(frame_register, text="Password", bg='#dcdcdc')
label_password.pack(pady=(0, 5))
entry_password = tk.Entry(frame_register, show='*', width=35)
entry_password.pack(pady=(0, 10))

# Register button
button_register = tk.Button(frame_register, text="Register", command=register, bg='#4a90e2', fg='white', bd=0)
button_register.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

# Create the database and table when the script is run
create_database()