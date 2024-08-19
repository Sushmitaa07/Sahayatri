import tkinter as tk
import sqlite3

# Function to create a labeled frame with a button
def create_labeled_frame(parent, text, bg_color, button_text):
    frame = tk.Frame(parent, bg=bg_color)
    label = tk.Label(frame, text=text, bg=bg_color, fg="white", font=("Helvetica", 12, "bold"))
    label.pack(expand=True, fill=tk.BOTH)
    button = tk.Button(frame, text=button_text, bg="#ffffff", fg="#000000", font=("Helvetica", 10), bd=0)
    button.pack(pady=(5, 10))
    return frame

# Database functions
def get_pending_fines_count():
    try:
        conn = sqlite3.connect('fines.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM pending_fines')
        count = cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        count = 0
    finally:
        conn.close()
    return count

def get_pending_fines_amount():
    try:
        conn = sqlite3.connect('fines.db')
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(fine_amount) FROM pending_fines')
        total_amount = cursor.fetchone()[0] or 0
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        total_amount = 0
    finally:
        conn.close()
    return total_amount

def get_paid_fines_count():
    try:
        conn = sqlite3.connect('fines.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM paid_fines')
        count = cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        count = 0
    finally:
        conn.close()
    return count

def get_paid_fines_amount():
    try:
        conn = sqlite3.connect('fines.db')
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(fine_amount) FROM paid_fines')
        total_amount = cursor.fetchone()[0] or 0
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        total_amount = 0
    finally:
        conn.close()
    return total_amount

def update_fine_info():
    pending_count = get_pending_fines_count()
    pending_amount = get_pending_fines_amount()
    paid_count = get_paid_fines_count()
    paid_amount = get_paid_fines_amount()

    frame1_label.config(text=f"PENDING FINE COUNT\n{pending_count}")
    frame2_label.config(text=f"PENDING FINE AMOUNT\n${pending_amount:.2f}")
    frame3_label.config(text=f"PAID FINE COUNT\n{paid_count}")
    frame4_label.config(text=f"PAID FINE AMOUNT\n${paid_amount:.2f}")

# Insert test data (Run this once to populate the database)
def insert_test_data():
    try:
        conn = sqlite3.connect('fines.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO pending_fines (fine_amount) VALUES (100.00)')
        cursor.execute('INSERT INTO pending_fines (fine_amount) VALUES (150.00)')
        cursor.execute('INSERT INTO paid_fines (fine_amount) VALUES (50.00)')
        cursor.execute('INSERT INTO paid_fines (fine_amount) VALUES (75.00)')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Uncomment the following line if you need to insert test data
# insert_test_data()

# Initialize main window
root = tk.Tk()
root.title("Sahayatri")
root.geometry("1024x768")
root.configure(bg="#eaeff2")

# Left navigation menu
nav_frame = tk.Frame(root, bg="#26384a", width=200)
nav_frame.grid(row=0, column=0, rowspan=3, sticky="ns")

# Configure grid column and row weights to ensure they expand correctly
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

# Navigation items
nav_items = ["Dashboard", "Driver's pending fine", "Drivers paid fine", "Provision details"]
for item in nav_items:
    button = tk.Button(nav_frame, text=item, bg="#26384a", fg="white", font=("Helvetica", 12), bd=0, padx=10, pady=10, anchor="w")
    button.pack(fill=tk.X)

# Main content area
content_frame = tk.Frame(root, bg="white")
content_frame.grid(row=0, column=1, columnspan=4, rowspan=3, sticky="nswe", padx=20, pady=20)

# Top row - Pending Fine Count and Amount
frame1 = create_labeled_frame(content_frame, "PENDING FINE COUNT", "#d88459", "View Details")
frame2 = create_labeled_frame(content_frame, "PENDING FINE AMOUNT", "#ce5858", "View Details")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")
frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

# Second row - Paid Fine Count and Amount
frame3 = create_labeled_frame(content_frame, "PAID FINE COUNT", "#79c39a", "View Details")
frame4 = create_labeled_frame(content_frame, "PAID FINE AMOUNT", "#8172b3", "View Details")
frame3.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")
frame4.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")

# Ensure content frames expand to cover the window
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_rowconfigure(1, weight=1)

# Update labels with data from database
frame1_label = frame1.children['!label']
frame2_label = frame2.children['!label']
frame3_label = frame3.children['!label']
frame4_label = frame4.children['!label']
root.after(100, update_fine_info)  # Call update_fine_info after UI initialization

# Key Traffic Rules for Drivers
rules_label = tk.Label(content_frame, text="Key Traffic Rules for Drivers", bg="white", fg="black", font=("Helvetica", 14, "bold"))
rules_label.grid(row=2, column=0, columnspan=2, pady=(20, 10), sticky="w")

rules_text = """• Obey all speed limits, loading limits, and safety restrictions on vehicles.
• Follow traffic signs and signals properly. Never drink and drive.
• Ensure your vehicle documents and insurance papers are up to date.
• Use pedestrian crossings and footpaths only to cross roads.
• Rash driving, overspeeding, and negligent driving attract huge fines.
• Always wear seatbelts and helmets when traveling.
• Never use cell phones when driving or crossing roads.
• Learn all essential traffic rules and spread awareness on road safety.
• Consider eco-friendly electric vehicles for greener, safer commuting."""
rules_content = tk.Label(content_frame, text=rules_text, bg="white", fg="black", font=("Helvetica", 12), justify=tk.LEFT)
rules_content.grid(row=3, column=0, columnspan=4, sticky="w")

# Run the Tkinter event loop
root.mainloop()
