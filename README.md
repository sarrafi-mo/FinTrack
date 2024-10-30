# FinTrack

**FinTrack** is a simple financial tracking application built with raw Python and MongoDB. This desktop application allows users to log, view, edit, and delete their income records in a table view format.

## Features
- Add new income records with amount, source, description, and date.
- View all income records in a sortable, structured table.
- Edit or delete any record with a simple click.
- User-friendly interface with options to navigate and manage records efficiently.

## Technologies Used
- **Python** (for GUI and backend logic)
- **Tkinter** (for creating the GUI interface)
- **MongoDB** (for storing data)

## Prerequisites
- Python 3.x installed on your system
- MongoDB server running locally or in a cloud environment

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/sarrafi-mo/FinTrack.git
    cd FinTrack
    ```

2. Install the required Python packages (if any additional packages are specified):
    ```bash
    pip install pymongo
    ```

3. Make sure MongoDB is running on your machine. By default, the code connects to MongoDB at `mongodb://localhost:27017/`.

## Usage
1. Run the application:
    ```bash
    python main.py
    ```
2. The main window will open, allowing you to:
   - Add a new record using the input fields and submit button.
   - View all records in a structured table with options to edit or delete each entry.

## Project Structure
- **main.py**: Contains the main application logic and the form to add new records.
- **display_data.py**: Handles viewing, editing, and deleting records in a table format.
  
## License
This project is open-source and available under the MIT License.

