import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('Sahayatri.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS drivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        license_id TEXT NOT NULL UNIQUE,
        driver_email TEXT NOT NULL,
        full_name TEXT NOT NULL,
        vehicle_name TEXT NOT NULL,
        license_issue_date DATE NOT NULL,
        license_expiry_date DATE NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def add_driver(license_id, driver_email, full_name, vehicle_name, license_issue_date, license_expiry_date):
    conn = sqlite3.connect('Sahayatri.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO drivers (license_id, driver_email, full_name, vehicle_name, license_issue_date, license_expiry_date)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (license_id, driver_email, full_name, vehicle_name, license_issue_date, license_expiry_date))
    conn.commit()
    conn.close()

def show_add_driver_result():
    try:
        license_id = entries[0].get()
        driver_email = entries[1].get()
        full_name = entries[2].get()
        vehicle_name = entries[3].get()
        license_issue_date = entries[4].get()
        license_expiry_date = entries[5].get()

        # Validate date formats
        datetime.strptime(license_issue_date, "%Y-%m-%d")
        datetime.strptime(license_expiry_date, "%Y-%m-%d")

        add_driver(license_id, driver_email, full_name, vehicle_name, license_issue_date, license_expiry_date)
        messagebox.showinfo("Success", "Driver added successfully!")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid date format or other error: {e}")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Driver with this License ID already exists!")

# Create the main application window
root = tk.Tk()
root.title("Driver Management System")

# Initialize database and tables
init_db()

# Set the window to fullscreen
root.state('zoomed')  # This maximizes the window to full screen

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
title_label = tk.Label(content, text="Add Driver", font=("Helvetica", 24), bg=content_bg, fg=text_fg)
title_label.grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 20))

# Breadcrumbs label
breadcrumbs_label = tk.Label(content, text="Dashboard / Add Driver", font=("Helvetica", 12), bg=content_bg, fg=text_fg)
breadcrumbs_label.grid(row=1, column=0, columnspan=4, sticky="w", pady=(0, 10))

# Labels and entry fields
labels = ["License ID", "Driver Email", "Full Name", "Vehicle Name", "License Issue Date (YYYY-MM-DD)", "License Expiry Date (YYYY-MM-DD)"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(content, text=label_text, font=("Helvetica", 16), bg=content_bg, fg=text_fg)
    label.grid(row=(i // 2) + 2, column=(i % 2) * 2, sticky="w", padx=(0, 20), pady=(10, 10))

    entry = tk.Entry(content, font=("Helvetica", 16), width=30, bg=entry_bg, fg=text_fg, bd=0)
    entry.grid(row=(i // 2) + 2, column=(i % 2) * 2 + 1, sticky="w", pady=(10, 10))
    entries.append(entry)

# Add Driver Button
add_driver_action_button = tk.Button(content, text="Add Driver", bg=button_bg, fg=button_fg, font=("Helvetica", 16), command=show_add_driver_result)
add_driver_action_button.grid(row=8, column=0, columnspan=4, pady=(20, 0))

root.mainloop()
