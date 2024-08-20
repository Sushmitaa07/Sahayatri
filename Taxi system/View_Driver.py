import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


def refresh_driver_table():
    # Clear the existing rows in the table
    for row in driver_table.get_children():
        driver_table.delete(row)

    # Fetch and display data
    conn = sqlite3.connect('Sahayatri.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM drivers')
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        driver_table.insert("", "end", values=row)

def view_drivers():
    # Create a new window
    view_window = tk.Toplevel(root)
    view_window.title("View Drivers")
    view_window.geometry("800x600")

    # Create a Treeview to display the drivers
    columns = ("id", "license_id", "driver_email", "full_name", "vehicle_name", "license_issue_date", "license_expiry_date")
    tree = ttk.Treeview(view_window, columns=columns, show='headings')

    # Define headings
    tree.heading("id", text="ID")
    tree.heading("license_id", text="License ID")
    tree.heading("driver_email", text="Email")
    tree.heading("full_name", text="Full Name")
    tree.heading("vehicle_name", text="Vehicle Name")
    tree.heading("license_issue_date", text="Issue Date")
    tree.heading("license_expiry_date", text="Expiry Date")

    # Define column widths
    tree.column("id", width=50)
    tree.column("license_id", width=100)
    tree.column("driver_email", width=150)
    tree.column("full_name", width=150)
    tree.column("vehicle_name", width=150)
    tree.column("license_issue_date", width=150)
    tree.column("license_expiry_date", width=150)

    tree.pack(fill="both", expand=True)

    # Fetch and display data
    conn = sqlite3.connect('Sahayatri.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM drivers')
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", "end", values=row)

# Create the main application window
root = tk.Tk()
root.title("Driver Management System")


# Set the window to fullscreen
root.state('zoomed')  # This maximizes the window to full screen

# Colors
sidebar_bg = "#2F4F6F"  # Sidebar background color
header_bg = "#3E5881"   # Header background color
content_bg = "#F2F2F2"  # Main content background color
button_bg = "#2F4F6F"   # Button background color
button_fg = "#FFFFFF"   # Button text color
text_fg = "#000000"     # Text color

# Sidebar Frame
sidebar = tk.Frame(root, bg=sidebar_bg, width=250)
sidebar.pack(side="left", fill="y")

# Sidebar buttons
dashboard_button = tk.Button(sidebar, text="Dashboard", bg=button_bg, fg=button_fg, font=("Helvetica", 16), bd=0)
dashboard_button.pack(pady=10)

add_driver_button = tk.Button(sidebar, text="Add Driver", bg=button_bg, fg=button_fg, font=("Helvetica", 16), bd=0)
add_driver_button.pack(pady=10)

view_driver_button = tk.Button(sidebar, text="View Driver", bg=button_bg, fg=button_fg, font=("Helvetica", 16), bd=0)
view_driver_button.pack(pady=10)

# Header Frame
header = tk.Frame(root, bg=header_bg, height=80)
header.pack(side="top", fill="x")

# Main content area
content = tk.Frame(root, bg=content_bg)
content.pack(side="top", fill="both", expand=True, padx=20, pady=20)

# Title label in content area
title_label = tk.Label(content, text="Driver Details", font=("Helvetica", 24), bg=content_bg, fg=text_fg)
title_label.grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 20))

# Driver Table
driver_table = ttk.Treeview(content, columns=("id", "license_id", "driver_email", "full_name", "vehicle_name", "license_issue_date", "license_expiry_date"), show='headings')
driver_table.heading("id", text="ID")
driver_table.heading("license_id", text="License ID")
driver_table.heading("driver_email", text="Email")
driver_table.heading("full_name", text="Full Name")
driver_table.heading("vehicle_name", text="Vehicle Name")
driver_table.heading("license_issue_date", text="Issue Date")
driver_table.heading("license_expiry_date", text="Expiry Date")

# Define column widths
driver_table.column("id", width=50)
driver_table.column("license_id", width=100)
driver_table.column("driver_email", width=150)
driver_table.column("full_name", width=150)
driver_table.column("vehicle_name", width=150)
driver_table.column("license_issue_date", width=150)
driver_table.column("license_expiry_date", width=150)

driver_table.grid(row=1, column=0, columnspan=4, pady=(20, 0), sticky="nsew")

# Refresh table on startup
refresh_driver_table()

root.mainloop()
