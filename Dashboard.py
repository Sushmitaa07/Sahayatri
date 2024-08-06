import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk

def show_add_driver_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()
    create_add_driver_frame(content_frame)

def show_view_driver_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()
    create_view_driver_frame(content_frame)

def create_add_driver_frame(parent):
    ttk.Label(parent, text="Add Driver", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, pady=20)

    form_labels = [
        ("License ID:", 1, 0),
        ("Driver Email:", 1, 2),
        ("Driver's Full Name:", 2, 0),
        ("Vehicle Name:", 2, 2),
        ("Driver's Email:", 3, 0),
        ("License Issue Date:", 4, 0),
        ("License Expiry Date:", 4, 2)
    ]
    
    for text, row, col in form_labels:
        label = ttk.Label(parent, text=text, font=("Arial", 14))
        label.grid(row=row, column=col, sticky=tk.E, pady=10, padx=10)

    ttk.Entry(parent, font=("Arial", 14)).grid(row=1, column=1, pady=10, padx=10, sticky=(tk.W, tk.E))
    ttk.Entry(parent, font=("Arial", 14)).grid(row=1, column=3, pady=10, padx=10, sticky=(tk.W, tk.E))
    ttk.Entry(parent, font=("Arial", 14)).grid(row=2, column=1, pady=10, padx=10, sticky=(tk.W, tk.E))
    ttk.Entry(parent, font=("Arial", 14)).grid(row=2, column=3, pady=10, padx=10, sticky=(tk.W, tk.E))
    ttk.Entry(parent, font=("Arial", 14)).grid(row=3, column=1, pady=10, padx=10, sticky=(tk.W, tk.E))
    DateEntry(parent, font=("Arial", 14)).grid(row=4, column=1, pady=10, padx=10, sticky=(tk.W, tk.E))
    DateEntry(parent, font=("Arial", 14)).grid(row=4, column=3, pady=10, padx=10, sticky=(tk.W, tk.E))

    parent.columnconfigure(1, weight=1)
    parent.columnconfigure(3, weight=1)

def create_view_driver_frame(parent):
    ttk.Label(parent, text="View Driver", font=("Arial", 20, "bold")).grid(row=0, column=0, pady=20)
    # Add content for the "View Driver" page here

def create_main_window():
    global content_frame  # Declare content_frame as global to access in other functions

    # Create the main window
    root = tk.Tk()
    root.title("Driver Management System")
    root.state('zoomed')  # Set the window to full screen

    # Define the color for the sidebar
    sidebar_color = "#34699A"  # Replace with the actual hex color code

    # Create the main frame
    main_frame = ttk.Frame(root, padding="10 10 10 10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Configure grid
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=4)
    main_frame.rowconfigure(0, weight=1)

    # Create the sidebar frame
    sidebar_frame = tk.Frame(main_frame, width=200, relief=tk.RAISED, bg=sidebar_color, padx=10, pady=10)
    sidebar_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))

    # Create the main content frame
    content_frame = ttk.Frame(main_frame, padding="10 10 10 10")
    content_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Configure grid to expand with window
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=4)
    main_frame.rowconfigure(0, weight=1)
    sidebar_frame.columnconfigure(0, weight=1)
    content_frame.columnconfigure(0, weight=1)

    # Load and resize the icons
    dashboard_image = Image.open("C:/Users/Acer/Documents/python_programs/Traffic/dashboard.png")
    dashboard_image = dashboard_image.resize((24, 24), Image.LANCZOS)
    dashboard_icon = ImageTk.PhotoImage(dashboard_image)

    add_driver_image = Image.open("C:/Users/Acer/Documents/python_programs/Traffic/add driver.png")
    add_driver_image = add_driver_image.resize((24, 24), Image.LANCZOS)
    add_driver_icon = ImageTk.PhotoImage(add_driver_image)

    view_driver_image = Image.open("C:/Users/Acer/Documents/python_programs/Traffic/view driver.png")
    view_driver_image = view_driver_image.resize((24, 24), Image.LANCZOS)
    view_driver_icon = ImageTk.PhotoImage(view_driver_image)

    # Add buttons to the sidebar
    sidebar_buttons = [
        ("Dashboard", None, dashboard_icon),
        ("Add driver", show_add_driver_frame, add_driver_icon),
        ("View driver", show_view_driver_frame, view_driver_icon)
    ]
    for i, (text, command, icon) in enumerate(sidebar_buttons):
        button = tk.Button(sidebar_frame, text=text, font=("Arial", 16, "bold"), bg=sidebar_color, fg="white", bd=0, command=command, image=icon, compound=tk.LEFT)
        button.grid(row=i, column=0, pady=20, padx=10, sticky=tk.W)

    # Show the Add Driver form by default
    show_add_driver_frame()

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
