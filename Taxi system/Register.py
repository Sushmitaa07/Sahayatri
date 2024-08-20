import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

# Create or connect to a SQLite database
conn = sqlite3.connect("Sahayatri.db")
cursor = conn.cursor()

# Create the 'register' table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS register (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    license_no TEXT NOT NULL,
                    contact_no TEXT NOT NULL,
                    temp_address TEXT NOT NULL,
                    perm_address TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL)''')
conn.commit()

# Function to handle the register button click event
def register():
    full_name = entry_full_name.get()
    license_no = entry_license.get()
    contact_no = entry_contact.get()
    temp_address = entry_temp_address.get()
    perm_address = entry_perm_address.get()
    email = entry_email.get()
    password = entry_password.get()  # Updated to match the correct widget name

    # Insert the registration data into the database
    cursor.execute("INSERT INTO register (full_name, license_no, contact_no, temp_address, perm_address, email, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (full_name, license_no, contact_no, temp_address, perm_address, email, password))
    conn.commit()

    messagebox.showinfo("Register", "Registration successful!")

# Create the main window
root = tk.Tk()
root.title("Registration Page")
root.geometry("1600x900")  # Increase the window size
root.configure(bg='#4a90e2')  # Blue background

# Load the background image
image_path = "traffic.webp"
image = Image.open(image_path)
image = image.resize((500, 500), Image.LANCZOS)  # Resize the image to fit in the middle
background_image = ImageTk.PhotoImage(image)

# Create a label for the image
label_image = tk.Label(root, image=background_image)
label_image.place(relx=0.75, rely=0.5, anchor='center')  # Place the image in the middle right

# Create a frame for the registration form
frame_register = tk.Frame(root, bg='#dcdcdc', bd=2, relief='solid')
frame_register.place(relx=0.25, rely=0.5, anchor='center', width=400, height=500)  # Increased height to accommodate the button

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
entry_password = tk.Entry(frame_register, width=35, show="*")  # Use 'show' to hide password
entry_password.pack(pady=(0, 10))

# Register button
button_register = tk.Button(frame_register, text="Register", command=register, bg='#4a90e2', fg='white', bd=0)
button_register.pack(pady=20)  # Added padding to ensure it's not too close to the entries

# Run the Tkinter event loop
root.mainloop()

# Close the database connection when the application is closed
conn.close()
