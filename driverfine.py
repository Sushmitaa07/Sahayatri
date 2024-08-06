import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Function to load and resize images
def load_image(path, size):
    image = Image.open(path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

# Create the main window
root = tk.Tk()
root.title("Dashboard")
root.geometry("1200x600")

# Extracted color from the provided image (assuming the color is similar to #2C3E50)
sidebar_color = '#34699A'  # Replace this with the exact hex color code if different

# Sidebar frame with increased width
sidebar = tk.Frame(root, bg=sidebar_color, width=350, height=600, relief='sunken', borderwidth=2)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# Main content frame
main_content = tk.Frame(root, bg='#ecf0f1', width=850, height=600)
main_content.pack(expand=True, fill='both', side='right')

# Load and resize images
dashboard_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/dashboard.png", (24, 24))
pending_fine_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/driver's pending fine.png", (24, 24))
paid_fine_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/Driver paid fine.png", (24, 24))
provision_details_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/Provision details.png", (24, 24))

# Sidebar buttons with icons
dashboard_button = tk.Button(sidebar, text="Dashboard", bg=sidebar_color, fg='white', relief='flat', font=("Arial", 14), image=dashboard_icon, compound=tk.LEFT)
dashboard_button.pack(pady=20)

pending_fine_button = tk.Button(sidebar, text="Driver's pending fine", bg=sidebar_color, fg='white', relief='flat', font=("Arial", 14), image=pending_fine_icon, compound=tk.LEFT)
pending_fine_button.pack(pady=20)

paid_fine_button = tk.Button(sidebar, text="Drivers paid fine", bg=sidebar_color, fg='white', relief='flat', font=("Arial", 14), image=paid_fine_icon, compound=tk.LEFT)
paid_fine_button.pack(pady=20)

provision_details_button = tk.Button(sidebar, text="Provision details", bg=sidebar_color, fg='white', relief='flat', font=("Arial", 14), image=provision_details_icon, compound=tk.LEFT)
provision_details_button.pack(pady=20)

# Main content title and breadcrumb frame
title_frame = tk.Frame(main_content, bg='#ecf0f1')
title_frame.pack(fill='x', padx=20, pady=(20, 0))

# Main content title
title_label = tk.Label(title_frame, text="Driver's Pending Fine", bg='#ecf0f1', fg='black', font=("Arial", 24))
title_label.pack(anchor='w')

# Breadcrumb
breadcrumb_label = tk.Label(title_frame, text="Dashboard / Driver's Pending Fine", bg='#ecf0f1', fg='gray', font=("Arial", 14))
breadcrumb_label.pack(anchor='w')

# Table frame
table_frame = tk.Frame(main_content, bg='#ecf0f1')
table_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Define columns
columns = ("Action", "Reference no", "Provision", "VEHICLE NO", "Issue date", "Expiry date", "Fine amount")

# Create Treeview
table = ttk.Treeview(table_frame, columns=columns, show='headings', height=10)
table.pack(fill='both', expand=True)

# Define headings
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=150, anchor='center')

# Style the Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12))
style.configure("Treeview", font=("Arial", 12), rowheight=25)

# Run the application
root.mainloop()
