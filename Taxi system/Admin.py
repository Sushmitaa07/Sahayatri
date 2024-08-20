import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3
import subprocess  # Import subprocess if you want to run external scripts

# Create the main application window
root = tk.Tk()
root.title("Driver Management System")

# Set the window to fullscreen
root.state('zoomed')  # This maximizes the window to full screen

# Function to launch the add driver script
def open_Dashboard():
    root.destroy()  # Close the login window
    subprocess.Popen(["python", "Dashboard.py"])  # Adjust script name as needed
    
# Function to launch the add driver script
def open_add_driver():
    subprocess.Popen(["python", "Add_Driver.py"])  # Adjust script name as needed

# Function to open view driver functionality
def open_view_driver():
    subprocess.Popen(["python", "View_Driver.py"])  # Adjust script name as needed



# Colors
sidebar_bg = "#2F4F6F"  # Sidebar background color
header_bg = "#3E5881"   # Header background color
content_bg = "#F2F2F2"  # Main content background color
button_bg = "#2F4F6F"   # Button background color
button_fg = "#FFFFFF"   # Button text color
text_fg = "#000000"     # Text color
entry_bg = "#DCDCDC"    # Entry background color

# Sidebar Frame
sidebar = tk.Frame(root, bg=sidebar_bg, width=250)
sidebar.pack(side="left", fill="y")

# Sidebar buttons
dashboard_button = tk.Button(sidebar, text="Dashboard", bg=button_bg,command=open_Dashboard, fg=button_fg, font=("Helvetica", 16), bd=0)
dashboard_button.pack(pady=10)

add_driver_button = tk.Button(sidebar, text="Add Driver", bg=button_bg, command=open_add_driver, fg=button_fg, font=("Helvetica", 16), bd=0)
add_driver_button.pack(pady=10)

view_driver_button = tk.Button(sidebar, text="View Driver", bg=button_bg, command=open_view_driver, fg=button_fg, font=("Helvetica", 16), bd=0)
view_driver_button.pack(pady=10)

# Header Frame
header = tk.Frame(root, bg=header_bg, height=80)
header.pack(side="top", fill="x")

# Main content area
content = tk.Frame(root, bg=content_bg)
content.pack(side="top", fill="both", expand=True, padx=20, pady=20)

root.mainloop()
