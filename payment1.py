import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Driver's Pending Fine")
root.geometry("800x400")

# Create the left sidebar frame
sidebar_frame = tk.Frame(root, bg='#2E4C6D', width=200)
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

# Add the sidebar buttons and icons (using text for simplicity)
buttons = ['Dashboard', "Driver's pending fine", 'Drivers paid fine', 'Provision details']
for button in buttons:
    btn = tk.Button(sidebar_frame, text=button, bg='#2E4C6D', fg='white', anchor='w', padx=10)
    btn.pack(fill=tk.X)

# Create the main content frame
content_frame = tk.Frame(root, bg='#F4F4F4')
content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add the heading
heading_label = tk.Label(content_frame, text="Driver's Pending fine", font=("Arial", 16), bg='#F4F4F4')
heading_label.pack(pady=10)

# Add the sub-heading (breadcrumb)
breadcrumb_label = tk.Label(content_frame, text="Dashboard / Driver's Pending Fine", bg='#E0E0E0', anchor='w', padx=10)
breadcrumb_label.pack(fill=tk.X)

# Add the table
table_frame = tk.Frame(content_frame)
table_frame.pack(pady=20, padx=20)

# Create the treeview (table)
columns = ("Action", "Chit no", "Provision", "VEHICLE NO", "Issue date", "Fine amount")
tree = ttk.Treeview(table_frame, columns=columns, show='headings')
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Define headings
for col in columns:
    tree.heading(col, text=col)

# Add a scrollbar to the table
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

# Add the Fine Payment button
fine_payment_button = tk.Button(content_frame, text="FINE Payment", bg='#3B73AF', fg='white')
fine_payment_button.pack(pady=20)

# Start the application
root.mainloop()