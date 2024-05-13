import sqlite3

def create_connection():
    return sqlite3.connect("password_manager.db")

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Drop the existing table (if necessary)
    cursor.execute('''DROP TABLE IF EXISTS passwords''')

    # Create the passwords table with the correct schema including the salt column
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        website TEXT NOT NULL,
                        username TEXT NOT NULL,
                        password BLOB NOT NULL,
                        description TEXT,
                        salt BLOB NOT NULL,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                      )''')

    # Create the master password table
    cursor.execute('''CREATE TABLE IF NOT EXISTS master_password (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        password_hash TEXT NOT NULL,
                        salt BLOB NOT NULL
                      )''')
    
    conn.commit()
    conn.close()

def insert_password(website, username, password, description, salt):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Insert the website, username, encrypted password, description, and salt
    cursor.execute('''INSERT INTO passwords (website, username, password, description, salt)
                      VALUES (?, ?, ?, ?, ?)''', (website, username, password, description, salt))
    
    conn.commit()
    conn.close()

def get_password(website):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Retrieve the encrypted password and salt for the given website
    cursor.execute('''SELECT password, salt FROM passwords WHERE website = ?''', (website,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return result  # Return the encrypted password and salt
    else:
        return (None, None)

def get_all_passwords():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Retrieve all passwords (for viewing in a list)
    cursor.execute('''SELECT website, username FROM passwords''')
    results = cursor.fetchall()
    
    conn.close()
    return results

def get_username(website):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT username FROM passwords WHERE website = ?''', (website,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def get_description(website):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT description FROM passwords WHERE website = ?''', (website,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def delete_password(website):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM passwords WHERE website = ?', (website,))
    conn.commit()
    conn.close()
