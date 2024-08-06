import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to handle the login button click event
def login():
    license_no = entry_license.get()
    password = entry_password.get()
    # Implement your login logic here
    messagebox.showinfo("Login", f"License No: {license_no}\nPassword: {password}")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("1000x600")  # Increase the window size
root.configure(bg='#4a90e2')  # Blue background

# Load the background image
image_path = "C:/Users/Acer/Documents/python_programs/Traffic/e17f5cfb-2c42-43c3-8be1-93b704cc820d.jpg"
image = Image.open(image_path)
image = image.resize((500, 500), Image.LANCZOS)  # Resize the image to fit in the middle
background_image = ImageTk.PhotoImage(image)

# Create a label for the image
label_image = tk.Label(root, image=background_image)
label_image.place(relx=0.7, rely=0.5, anchor='center')  # Place the image in the middle right

# Create a frame for the login form
frame_login = tk.Frame(root, bg='#dcdcdc', bd=2, relief='solid')
frame_login.place(relx=0.3, rely=0.5, anchor='center', width=350, height=250)  # Increase width and height

# License number label and entry
label_license = tk.Label(frame_login, text="Enter License no", bg='#dcdcdc')
label_license.pack(pady=(20, 5))
entry_license = tk.Entry(frame_login, width=35)  # Increase width of the entry
entry_license.pack(pady=(0, 10))

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
