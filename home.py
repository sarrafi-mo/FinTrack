import tkinter as tk
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['financial_tracker']
income_collection = db['income']

def add_income():
    amount = entry_amount.get()
    source = entry_source.get()
    description = entry_description.get()
    date = entry_date.get()
    
    income_collection.insert_one({
        'amount': float(amount),
        'source': source,
        'description': description,
        'date': date
    })
    
    entry_amount.delete(0, tk.END)
    entry_source.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_date.delete(0, tk.END)

# Functions to clear default text on focus
# on_focus_in: This function clears the text when the entry is focused, if it contains the default text.
# on_focus_out: This function re-adds the default text if the entry is empty after losing focus.
def on_focus_in(entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tk.END)

def on_focus_out(entry, default_text):
    if entry.get() == "":
        entry.insert(0, default_text)

# Set up the GUI
root = tk.Tk()
root.title("Financial Tracker")
root.geometry("400x300")  # Set window size

# Labels and input fields
entry_amount = tk.Entry(root, width=30)
entry_amount.insert(0, "Amount")
entry_amount.bind("<FocusIn>", lambda event: on_focus_in(entry_amount, "Amount"))
entry_amount.bind("<FocusOut>", lambda event: on_focus_out(entry_amount, "Amount"))
entry_amount.pack(pady=5)

entry_source = tk.Entry(root, width=30)
entry_source.insert(0, "Source")
entry_source.bind("<FocusIn>", lambda event: on_focus_in(entry_source, "Source"))
entry_source.bind("<FocusOut>", lambda event: on_focus_out(entry_source, "Source"))
entry_source.pack(pady=5)

entry_description = tk.Entry(root, width=30)
entry_description.insert(0, "Description")
entry_description.bind("<FocusIn>", lambda event: on_focus_in(entry_description, "Description"))
entry_description.bind("<FocusOut>", lambda event: on_focus_out(entry_description, "Description"))
entry_description.pack(pady=5)

entry_date = tk.Entry(root, width=30)
entry_date.insert(0, "Date (YYYY-MM-DD)")
entry_date.bind("<FocusIn>", lambda event: on_focus_in(entry_date, "Date (YYYY-MM-DD)"))
entry_date.bind("<FocusOut>", lambda event: on_focus_out(entry_date, "Date (YYYY-MM-DD)"))
entry_date.pack(pady=5)

# Button to add income
add_button = tk.Button(root, text="Add Income", command=add_income)
add_button.pack(pady=15)

root.mainloop()
