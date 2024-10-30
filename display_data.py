import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient
from bson import ObjectId
from tkinter import messagebox

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['financial_tracker']
income_collection = db['income']

# Function to delete a record with confirmation
def delete_record(record_id, tree):
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
    if confirm:
        income_collection.delete_one({"_id": ObjectId(record_id)})
        messagebox.showinfo("Deleted", "Record deleted successfully.")
        for item in tree.get_children():
            tree.delete(item)
        load_data(tree)

# Function to open edit form and update the record
def edit_record(record_id, tree):
    # Fetch current record data
    record = income_collection.find_one({"_id": ObjectId(record_id)})
    
    # Create a new window for editing
    edit_window = tk.Toplevel()
    edit_window.title("Edit Record")
    edit_window.geometry("300x250")

    # Labels and Entry fields for each attribute
    tk.Label(edit_window, text="Amount").pack()
    amount_entry = tk.Entry(edit_window)
    amount_entry.pack()
    amount_entry.insert(0, record["amount"])  # Set current value

    tk.Label(edit_window, text="Source").pack()
    source_entry = tk.Entry(edit_window)
    source_entry.pack()
    source_entry.insert(0, record["source"])

    tk.Label(edit_window, text="Description").pack()
    description_entry = tk.Entry(edit_window)
    description_entry.pack()
    description_entry.insert(0, record["description"])

    tk.Label(edit_window, text="Date").pack()
    date_entry = tk.Entry(edit_window)
    date_entry.pack()
    date_entry.insert(0, record["date"])

    # Update function to save changes to MongoDB
    def save_changes():
        new_data = {
            "amount": amount_entry.get(),
            "source": source_entry.get(),
            "description": description_entry.get(),
            "date": date_entry.get()
        }
        income_collection.update_one({"_id": ObjectId(record_id)}, {"$set": new_data})
        messagebox.showinfo("Updated", "Record updated successfully.")
        edit_window.destroy()
        
        # Refresh the table view
        for item in tree.get_children():
            tree.delete(item)
        load_data(tree)

    # Save button
    save_button = tk.Button(edit_window, text="Save Changes", command=save_changes)
    save_button.pack()

# Function to load data into the table
def load_data(tree):
    records = income_collection.find()
    for index, record in enumerate(records, start=1):
        tree.insert("", tk.END, values=(index, record["amount"], record["source"], record["description"], record["date"], "Edit", "Delete"), tags=(str(record["_id"]),))

# Function to display stored data in a table format
def show_data(root):
    data_window = tk.Toplevel(root)
    data_window.title("Stored Data")
    data_window.geometry("650x300")

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    style.configure("Treeview", rowheight=25, font=("Arial", 10))
    style.configure("Treeview", borderwidth=1, relief="solid")
    style.map("Treeview", background=[("selected", "#ececec")])

    style.configure("Treeview", anchor="center")

    columns = ("Row", "Amount", "Source", "Description", "Date", "Edit", "Delete")
    tree = ttk.Treeview(data_window, columns=columns, show="headings", style="Treeview")

    tree.heading("Row", text="Row")
    tree.heading("Amount", text="Amount")
    tree.heading("Source", text="Source")
    tree.heading("Description", text="Description")
    tree.heading("Date", text="Date")
    tree.heading("Edit", text="Edit")
    tree.heading("Delete", text="Delete")

    tree.column("Row", width=50, anchor="center")
    tree.column("Amount", width=80, anchor="center")
    tree.column("Source", width=100, anchor="center")
    tree.column("Description", width=150, anchor="center")
    tree.column("Date", width=100, anchor="center")
    tree.column("Edit", width=50, anchor="center")
    tree.column("Delete", width=50, anchor="center")

    load_data(tree)

    def on_tree_click(event):
        item = tree.identify("item", event.x, event.y)
        if not item:  #If no item was clicked, exit the function
            return
    
        column = tree.identify_column(event.x)
        record_id = tree.item(item, "tags")

        # Check if record_id is available to prevent IndexError
        if record_id:
            record_id = record_id[0]  # Extract the actual ID from tags
            if column == "#6":  # Edit column
                edit_record(record_id, tree)
            elif column == "#7":  # Delete column
                delete_record(record_id, tree)

    tree.bind("<Button-1>", on_tree_click)
    tree.pack(fill=tk.BOTH, expand=True)
