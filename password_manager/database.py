import sqlite3

def create_connection():
    return sqlite3.connect("password_manager.db")

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        website TEXT NOT NULL,
                        username TEXT NOT NULL,
                        password BLOB NOT NULL,
                        description TEXT,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS master_password (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        password_hash TEXT NOT NULL,
                        salt TEXT NOT NULL
                      )''')

    conn.commit()
    conn.close()

def insert_password(website, username, password, description):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO passwords (website, username, password, description)
                      VALUES (?, ?, ?, ?)''', (website, username, password, description))
    conn.commit()
    conn.close()

def get_password(website):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT password FROM passwords WHERE website = ?''', (website,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def get_all_passwords():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords")
    passwords = cursor.fetchall()
    conn.close()
    return passwords

def get_username(website):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM passwords WHERE website = ?", (website,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def get_description(website):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT description FROM passwords WHERE website = ?", (website,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def delete_password(website):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE website = ?", (website,))
    conn.commit()
    conn.close()
