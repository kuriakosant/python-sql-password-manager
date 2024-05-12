
# Python SQL Password Manager

## Overview

This is a simple password manager built using Python, SQLite for local database storage, and Tkinter for the graphical user interface (GUI). It allows you to securely store, retrieve, and manage passwords using a master password. The stored passwords are encrypted using the `cryptography` library.

## Features

- **Master Password Protection**: Access to the application is protected by a master password. If the master password is entered incorrectly 10 times, all stored passwords are permanently deleted.
- **Password Encryption**: All passwords are encrypted before they are stored in the database.
- **Password Management**: Add, view, and delete stored passwords.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/kuriakosant/python-sql-password-manager.git
    cd python-sql-password-manager
    ``` 
    
2. **Install the dependencies**:
 Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ``` 
    
3. **Initialize the SQLite database**:
 Run the following command to create the necessary database tables:
    ```bash
    python -c "from password_manager import database; database.create_tables()"
    ``` 
    
## Running the Application

To run the application, simply execute the `main.py` file:

```bash
python main.py
```

The GUI will prompt you for the master password before allowing access to the password manager.

