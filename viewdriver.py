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
root.geometry("1200x600")  # Increase the size of the main window

# Define the new color for the sidebar and top section
sidebar_color = '#23507A'

# Sidebar frame (increased width)
sidebar = tk.Frame(root, bg=sidebar_color, width=350, height=600, relief='sunken', borderwidth=2)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# Top frame
top_frame = tk.Frame(root, bg=sidebar_color, width=1200, height=50)
top_frame.pack(expand=False, fill='x', side='top')

# Main content frame
main_content = tk.Frame(root, bg='#ffffff', width=850, height=550)
main_content.pack(expand=True, fill='both', side='right')

# Load and resize images
dashboard_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/dashboard.png", (24, 24))
add_driver_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/add driver.png", (24, 24))
view_driver_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/view driver.png", (24, 24))
register_driver_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/add driver.png", (24, 24))
last_month_register_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/register driver.png", (24, 24))
last_year_register_icon = load_image("C:/Users/Acer/Documents/python_programs/Traffic/Last year registerd.png", (24, 24))

# Sidebar buttons with icons
dashboard_button = tk.Button(sidebar, text="Dashboard", bg=sidebar_color, fg='white', relief='flat', font=("Arial", 14), image=dashboard_icon, compound=tk.LEFT)
dashboard_button.pack(pady=20)

add_driver_button = tk.Button(sidebar, text="Add driver", bg=sidebar_color, fg='white', relief='flat', font=("Arial", 14), image=add_driver_icon, compound=tk.LEFT)
add_driver_button.pack(pady=20)

view_driver_button = tk.Button(sidebar, text="View driver", bg=sidebar_color, fg='white', relief='flat', font=("Arial", 14), image=view_driver_icon, compound=tk.LEFT)
view_driver_button.pack(pady=20)

# Main content panels (specific size and colors)
panel1 = tk.Frame(main_content, bg='#E67E22', width=250, height=200)
panel1.pack_propagate(False)  # Prevents the frame from resizing to fit the content
panel1.grid(row=0, column=0, padx=30, pady=30)

panel2 = tk.Frame(main_content, bg='#E74C3C', width=250, height=200)
panel2.pack_propagate(False)
panel2.grid(row=0, column=1, padx=30, pady=30)

panel3 = tk.Frame(main_content, bg='#1ABC9C', width=250, height=200)
panel3.pack_propagate(False)
panel3.grid(row=0, column=2, padx=30, pady=30)

# Panel buttons with icons
panel1_button = tk.Button(panel1, text="Registered Driver", bg='#E67E22', fg='white', font=("Arial", 16), image=register_driver_icon, compound=tk.LEFT)
panel1_button.pack(expand=True)

panel2_button = tk.Button(panel2, text="Last month registered", bg='#E74C3C', fg='white', font=("Arial", 16), image=last_month_register_icon, compound=tk.LEFT)
panel2_button.pack(expand=True)

panel3_button = tk.Button(panel3, text="Last year registered", bg='#1ABC9C', fg='white', font=("Arial", 16), image=last_year_register_icon, compound=tk.LEFT)
panel3_button.pack(expand=True)

# Run the application
root.mainloop()
