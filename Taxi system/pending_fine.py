import tkinter as tk
from tkinter import ttk
import sqlite3
import subprocess

# Database functions
def connect_db():
    return sqlite3.connect('Sahayatri.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pending_fines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chit_no TEXT,
        provision TEXT,
        vehicle_no TEXT,
        issue_date TEXT,
        fine_amount REAL
    )
    ''')
    conn.commit()
    conn.close()

def insert_fine(chit_no, provision, vehicle_no, issue_date, fine_amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO pending_fines (chit_no, provision, vehicle_no, issue_date, fine_amount)
    VALUES (?, ?, ?, ?, ?)
    ''', (chit_no, provision, vehicle_no, issue_date, fine_amount))
    conn.commit()
    conn.close()

def fetch_pending_fines():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pending_fines')
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_fine(id, chit_no, provision, vehicle_no, issue_date, fine_amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE pending_fines
    SET chit_no = ?, provision = ?, vehicle_no = ?, issue_date = ?, fine_amount = ?
    WHERE id = ?
    ''', (chit_no, provision, vehicle_no, issue_date, fine_amount, id))
    conn.commit()
    conn.close()

def delete_fine(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pending_fines WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# Initialize database
create_tables()

# Example test data insertion
def insert_test_data():
    insert_fine('123', 'Speeding', 'ABC123', '2024-08-17', 100.00)
    insert_fine('124', 'Parking', 'XYZ789', '2024-08-18', 50.00)

# Uncomment the following line to insert test data
# insert_test_data()

# Create the main application window
root = tk.Tk()
root.title("Driver's Pending Fine")
root.geometry("1600x900")
root.configure(bg='#e8eaed')

# Define colors
side_menu_bg = "#2b4560"
header_bg = "#2b4573"
content_bg = "#e8eaed"
button_bg = "#5a6cae"
text_color = "#000000"

# Create the sidebar frame
side_menu = tk.Frame(root, bg=side_menu_bg, width=200)
side_menu.pack(side="left", fill="y")

# Sidebar buttons
dashboard_button = tk.Button(side_menu, text="Dashboard", font=("Arial", 12), fg="#ffffff", bg=side_menu_bg, anchor="w", padx=10, pady=10, bd=0)
dashboard_button.pack(fill="x")

pending_fine_button = tk.Button(side_menu, text="Driver's pending fine", font=("Arial", 12), fg="#ffffff", bg=side_menu_bg, anchor="w", padx=10, pady=10, bd=0)
pending_fine_button.pack(fill="x")

paid_fine_button = tk.Button(side_menu, text="Drivers paid fine", font=("Arial", 12), fg="#ffffff", bg=side_menu_bg, anchor="w", padx=10, pady=10, bd=0)
paid_fine_button.pack(fill="x")

provision_details_button = tk.Button(side_menu, text="Provision details", font=("Arial", 12), fg="#ffffff", bg=side_menu_bg, anchor="w", padx=10, pady=10, bd=0)
provision_details_button.pack(fill="x")

# Create the header frame
header = tk.Frame(root, bg=header_bg, height=50)
header.pack(side="top", fill="x")

header_label = tk.Label(header, text="Driver's Pending Fine", font=("Arial", 20), fg=text_color, bg=header_bg)
header_label.pack(pady=10)

# Create the breadcrumb frame
breadcrumb = tk.Frame(root, bg=content_bg, height=30)
breadcrumb.pack(side="top", fill="x")

breadcrumb_label = tk.Label(breadcrumb, text="Dashboard/ Driver's Pending Fine", font=("Arial", 10), fg=text_color, bg=content_bg)
breadcrumb_label.pack(pady=5, padx=10, anchor="w")

# Create the content frame
content = tk.Frame(root, bg=content_bg)
content.pack(side="top", fill="both", expand=True, padx=20, pady=10)

# Define columns
columns = ("id", "chit_no", "provision", "vehicle_no", "issue_date", "fine_amount")

# Create Treeview widget
tree = ttk.Treeview(content, columns=columns, show='headings', height=15)
tree.pack(fill="both", expand=True)

# Define headings
tree.heading("id", text="ID")
tree.heading("chit_no", text="Chit No")
tree.heading("provision", text="Provision")
tree.heading("vehicle_no", text="Vehicle No")
tree.heading("issue_date", text="Issue Date")
tree.heading("fine_amount", text="Fine Amount")

# Define column width
tree.column("id", width=50)
tree.column("chit_no", width=100)
tree.column("provision", width=150)
tree.column("vehicle_no", width=150)
tree.column("issue_date", width=150)
tree.column("fine_amount", width=150)

# Add grid lines (rows) to simulate Excel-like cells
def load_data():
    for item in tree.get_children():
        tree.delete(item)
    fines = fetch_pending_fines()
    for fine in fines:
        tree.insert("", "end", values=fine)

load_data()

# Add a placeholder function for "FINE Payment"
def open_fine_payment():
    subprocess.Popen(["python", "Fine_payment.py"])  # Adjust script name if needed

# Fine Payment Button
payment_button = tk.Button(content, text="FINE Payment", font=("Arial", 12), command=open_fine_payment, fg="#ffffff", bg=button_bg, padx=10, pady=5)
payment_button.pack(pady=20)

# Style Treeview to show gridlines
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 10), foreground="black", background="lightgrey")
style.configure("Treeview", font=("Arial", 10), rowheight=25, borderwidth=1, relief="solid")
style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])  # Remove borders

# Run the application
root.mainloop()
