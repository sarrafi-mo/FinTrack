import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient
from tkinter import messagebox

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['financial_tracker']
income_collection = db['income']

# Function to delete a record
def delete_record(record_id, tree):
    income_collection.delete_one({"_id": record_id})
    messagebox.showinfo("Deleted", "Record deleted successfully.")
    # Refresh the table view
    for item in tree.get_children():
        tree.delete(item)
    load_data(tree)

# Function to load data into the table
def load_data(tree):
    records = income_collection.find()
    for index, record in enumerate(records, start=1):
        tree.insert("", tk.END, values=(index, record["amount"], record["source"], record["description"], record["date"], "Edit", "Delete"), tags=(str(record["_id"]),))

# Function to display stored data in a table format
def show_data(root):
    # Create a new window
    data_window = tk.Toplevel(root)
    data_window.title("Stored Data")
    data_window.geometry("650x300")

    # Create style for Treeview
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    style.configure("Treeview", rowheight=25, font=("Arial", 10))
    style.configure("Treeview", borderwidth=1, relief="solid")  # Add border to cells
    style.map("Treeview", background=[("selected", "#ececec")])  # Background on selection

    # Center align the cell content
    style.configure("Treeview", anchor="center")

    # Create a Treeview widget for the table with an extra column for row numbers and actions
    columns = ("Row", "Amount", "Source", "Description", "Date", "Edit", "Delete")
    tree = ttk.Treeview(data_window, columns=columns, show="headings", style="Treeview")

    # Define column headings
    tree.heading("Row", text="Row")
    tree.heading("Amount", text="Amount")
    tree.heading("Source", text="Source")
    tree.heading("Description", text="Description")
    tree.heading("Date", text="Date")
    tree.heading("Edit", text="Edit")
    tree.heading("Delete", text="Delete")

    # Define column widths and center alignment
    tree.column("Row", width=50, anchor="center")
    tree.column("Amount", width=80, anchor="center")
    tree.column("Source", width=100, anchor="center")
    tree.column("Description", width=150, anchor="center")
    tree.column("Date", width=100, anchor="center")
    tree.column("Edit", width=50, anchor="center")
    tree.column("Delete", width=50, anchor="center")

    # Load data with edit and delete options
    load_data(tree)

    # Bind click events for edit and delete actions
    def on_tree_click(event):
        item = tree.identify("item", event.x, event.y)
        column = tree.identify_column(event.x)
        record_id = tree.item(item, "tags")[0]  # Get record ID from tags

        if column == "#6":  # Edit column
            # Placeholder for edit function
            messagebox.showinfo("Edit", f"Edit record with ID: {record_id}")
        elif column == "#7":  # Delete column
            delete_record(record_id, tree)

    tree.bind("<Button-1>", on_tree_click)

    # Add the table to the window and pack it
    tree.pack(fill=tk.BOTH, expand=True)
