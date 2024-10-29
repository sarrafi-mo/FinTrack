import tkinter as tk
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['financial_tracker']
income_collection = db['income']

# Function to display saved data
# show_data : Creates a new window, retrieves data from MongoDB, and displays each record.

def show_data(root):
    # Create a new window
    data_window = tk.Toplevel(root)
    data_window.title("Stored Data")
    data_window.geometry("400x300")

    # Retrieve data from MongoDB
    records = income_collection.find()

    # Display data in the new window
    for index, record in enumerate(records):
        tk.Label(data_window, text=f"Record {index + 1}").pack()
        tk.Label(data_window, text=f"Amount: {record['amount']}").pack()
        tk.Label(data_window, text=f"Source: {record['source']}").pack()
        tk.Label(data_window, text=f"Description: {record['description']}").pack()
        tk.Label(data_window, text=f"Date: {record['date']}").pack()
        tk.Label(data_window, text="-" * 30).pack()  # Divider
