import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import subprocess

# Create Labeled Frame
def create_labeled_frame(parent, text, bg_color, button_text):
    frame = tk.Frame(parent, bg=bg_color)
    label = tk.Label(frame, text=text, bg=bg_color, fg="white", font=("Helvetica", 12, "bold"))
    label.pack(expand=True, fill=tk.BOTH)
    button = tk.Button(frame, text=button_text, bg="#ffffff", fg="#000000", font=("Helvetica", 10), bd=0)
    button.pack(pady=(5, 10))
    return frame

# Function to open the Login script
def open_login():
    subprocess.Popen(["python", "Login.py"])

# Function to open the Register script
def open_register():
    subprocess.Popen(["python", "Register.py"])

# Create the main window
root = tk.Tk()
root.title("Sahayatri")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size to full screen
root.geometry(f"{screen_width}x{screen_height}")

# Create a frame for the header
header_frame = tk.Frame(root, bg="#3b82f6", height=70)
header_frame.pack(fill=tk.X)

# Create the header label
header_label = tk.Label(header_frame, text="SAHAYATRI", bg="#3b82f6", fg="white", font=("Arial", 36, "bold"))
header_label.pack(side=tk.LEFT, padx=20, pady=5)

# Create the login and register buttons with increased size
button_font = ("Arial", 14)
login_button = tk.Button(header_frame, text="Log In", command=open_login, bg="#3b82f6", fg="white", font=button_font, padx=20, pady=10)
login_button.pack(side=tk.RIGHT, padx=(0, 10), pady=10)

register_button = tk.Button(header_frame, text="Register", command=open_register, bg="#3b82f6", fg="white", font=button_font, padx=20, pady=10)
register_button.pack(side=tk.RIGHT, pady=10)

image_path = "cartoon-city-crossroads-with-cars-in-traffic-jam-vector-20863753.jpg"
try:
    image = Image.open(image_path)
except IOError:
    messagebox.showerror("Error", f"Image not found at {image_path}")
    root.destroy()
    exit()

# Resize image to fit screen
image = image.resize((screen_width, screen_height - 70), Image.LANCZOS)

# Prepare to draw text on the image
draw = ImageDraw.Draw(image)
try:
    pil_font = ImageFont.truetype("arial.ttf", 20)  # Adjusted font size to be smaller
except IOError:
    pil_font = ImageFont.load_default()

# Text to be added to the image
about_text = (
    "About us:\n"
    "This app keeps track of every single payment from the beginning.\n"
    "Furthermore, we are also going to analyze your data for you.\n"
    "Every driver has a driving record, which shows traffic violations.\n"
    "Because your driving record can affect your driving privileges,\n"
    "it's important to check your driving record for accuracy and even\n"
    "for handling traffic tickets, which can be done by our app."
)

# Add text to the bottom of the image, but a bit higher
text_position = (screen_width // 20, screen_height - 350)

draw.text(text_position, about_text, fill="black", font=pil_font)

# Convert to PhotoImage
photo = ImageTk.PhotoImage(image)

# Display the image in the window
image_label = tk.Label(root, image=photo)
image_label.pack(pady=0)

# Create a frame for the "About us" section and "Inquiry via email" button
about_frame = tk.Frame(root, bg="white", height=50)
about_frame.pack(fill=tk.X, pady=(0, 30))

# Add the "About us" text and "Inquiry via email" button
about_label = tk.Label(about_frame, text=about_text, bg="white", anchor="w", justify="left")
about_label.pack(side=tk.LEFT, padx=20)

inquiry_button = tk.Button(about_frame, text="Inquiry via email", bg="#3b82f6", fg="white", font=button_font)
inquiry_button.pack(side=tk.RIGHT, padx=30)

root.mainloop()
