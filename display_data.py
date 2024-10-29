import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['financial_tracker']
income_collection = db['income']

# Function to display stored data in a table format
def show_data(root):
    # Create a new window
    data_window = tk.Toplevel(root)
    data_window.title("Stored Data")
    data_window.geometry("550x300")

    # Create style for Treeview
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    style.configure("Treeview", rowheight=25, font=("Arial", 10))
    style.configure("Treeview", borderwidth=1, relief="solid")  # Add border to cells
    style.map("Treeview", background=[("selected", "#ececec")])  # Background on selection

    # Center align the cell content
    style.configure("Treeview", anchor="center")

    # Create a Treeview widget for the table with an extra column for row numbers
    columns = ("Row", "Amount", "Source", "Description", "Date")
    tree = ttk.Treeview(data_window, columns=columns, show="headings", style="Treeview")

    # Define column headings
    tree.heading("Row", text="Row")
    tree.heading("Amount", text="Amount")
    tree.heading("Source", text="Source")
    tree.heading("Description", text="Description")
    tree.heading("Date", text="Date")

    # Define column widths and center alignment
    tree.column("Row", width=50, anchor="center")  # Row number column
    tree.column("Amount", width=80, anchor="center")
    tree.column("Source", width=100, anchor="center")
    tree.column("Description", width=150, anchor="center")
    tree.column("Date", width=100, anchor="center")

    # Insert data into the table with row numbers
    records = income_collection.find()
    for index, record in enumerate(records, start=1):  # Start row numbering from 1
        tree.insert("", tk.END, values=(index, record["amount"], record["source"], record["description"], record["date"]))

    # Add the table to the window and pack it
    tree.pack(fill=tk.BOTH, expand=True)
