import bcrypt
from password_manager import database

MAX_ATTEMPTS = 10
attempts = 0

def master_password_exists():
    conn = database.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM master_password")
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

def set_master_password(master_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(master_password.encode(), salt)
    
    conn = database.create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO master_password (password_hash, salt) VALUES (?, ?)", (hashed_password, salt))
    conn.commit()
    conn.close()

def check_master_password(entered_password):
    global attempts
    conn = database.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, salt FROM master_password")
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hash, salt = result
        if bcrypt.checkpw(entered_password.encode(), stored_hash):
            attempts = 0
            return True
        else:
            attempts += 1
            if attempts >= MAX_ATTEMPTS:
                database.delete_all_passwords()
                return False
            return False
    return False
