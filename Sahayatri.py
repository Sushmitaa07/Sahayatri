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

# Define the custom color
custom_color = '#29497A'

# Sidebar frame
sidebar = tk.Frame(root, bg=custom_color, width=350, height=600, relief='sunken', borderwidth=2)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# Top bar frame
top_bar = tk.Frame(root, bg=custom_color, height=50)
top_bar.pack(expand=False, fill='x', side='top')

# Settings label on the top bar
settings_label = tk.Label(top_bar, text="Settings", bg=custom_color, fg='white', font=("Arial", 14))
settings_label.pack(side='right', padx=20, pady=10)

# Main content frame
main_content = tk.Frame(root, bg='#ecf0f1', width=850, height=550)
main_content.pack(expand=True, fill='both', side='right', anchor='nw')

# Load and resize images
dashboard_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/dashboard.png", (24, 24))
pending_fine_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/driver's pending fine.png", (24, 24))
paid_fine_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/Driver paid fine.png", (24, 24))
provision_details_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/Provision details.png", (24, 24))
pending_count_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/pending count.png", (24, 24))
paid_fine_count_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/Paid fine count.png", (24, 24))

# Sidebar buttons and title
title_label = tk.Label(sidebar, text="sahayatri", bg=custom_color, fg='white', font=("Arial", 14))
title_label.pack(pady=(20, 40))

dashboard_button = tk.Button(sidebar, text="Dashboard", bg=custom_color, fg='white', relief='flat', font=("Arial", 14), image=dashboard_icon, compound=tk.LEFT)
dashboard_button.pack(pady=10)

pending_fine_button = tk.Button(sidebar, text="Driver's pending fine", bg=custom_color, fg='white', relief='flat', font=("Arial", 14), image=pending_fine_icon, compound=tk.LEFT)
pending_fine_button.pack(pady=10)

paid_fine_button = tk.Button(sidebar, text="Drivers paid fine", bg=custom_color, fg='white', relief='flat', font=("Arial", 14), image=paid_fine_icon, compound=tk.LEFT)
paid_fine_button.pack(pady=10)

provision_details_button = tk.Button(sidebar, text="Provision details", bg=custom_color, fg='white', relief='flat', font=("Arial", 14), image=provision_details_icon, compound=tk.LEFT)
provision_details_button.pack(pady=10)

# Main content panels (increased size)
panel_width = 250
panel_height = 250

panel1 = tk.Frame(main_content, bg='#E67E22', width=panel_width, height=panel_height)
panel1.pack_propagate(False)
panel1.grid(row=0, column=0, padx=20, pady=30)

panel2 = tk.Frame(main_content, bg='#E74C3C', width=panel_width, height=panel_height)
panel2.pack_propagate(False)
panel2.grid(row=0, column=1, padx=20, pady=30)

panel3 = tk.Frame(main_content, bg='#1ABC9C', width=panel_width, height=panel_height)
panel3.pack_propagate(False)
panel3.grid(row=0, column=2, padx=20, pady=30)

panel4 = tk.Frame(main_content, bg='#9B59B6', width=panel_width, height=panel_height)
panel4.pack_propagate(False)
panel4.grid(row=0, column=3, padx=20, pady=30)

# Panel buttons
label_font = ("Arial", 14)

panel1_button = tk.Button(panel1, text="PENDING FINE COUNT", bg='#E67E22', fg='white', font=label_font, image=pending_count_icon, compound=tk.LEFT)
panel1_button.pack(expand=True)

panel2_button = tk.Button(panel2, text="PENDING FINE AMOUNT", bg='#E74C3C', fg='white', font=label_font, image=pending_fine_icon, compound=tk.LEFT)
panel2_button.pack(expand=True)

panel3_button = tk.Button(panel3, text="PAID FINE COUNT", bg='#1ABC9C', fg='white', font=label_font, image=paid_fine_count_icon, compound=tk.LEFT)
panel3_button.pack(expand=True)

panel4_button = tk.Button(panel4, text="PAID FINE AMOUNT", bg='#9B59B6', fg='white', font=label_font, image=paid_fine_count_icon, compound=tk.LEFT)
panel4_button.pack(expand=True)

# Run the application
root.mainloop()
