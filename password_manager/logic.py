from password_manager import encryption, database
import os

def add_password(website, username, plain_password, description):
    # Generate a random salt for this password
    salt = os.urandom(16)  # 16-byte salt
    
    # Generate the encryption key using the master password and salt
    master_password = "your_master_password"  # This should be securely obtained
    key = encryption.generate_key(master_password, salt)
    
    # Encrypt the password using the key
    encrypted_password = encryption.encrypt_password(plain_password, key)
    
    # Insert the password, username, website, description, and salt into the database
    database.insert_password(website, username, encrypted_password, description, salt)

def get_all_passwords():
    # Retrieve all passwords from the database
    return database.get_all_passwords()

def view_password(website):
    # Retrieve the encrypted password and salt from the database
    encrypted_password, salt = database.get_password(website)
    
    if not encrypted_password:
        return None
    
    # Generate the encryption key using the master password and the retrieved salt
    master_password = "your_master_password"  # This should be securely obtained
    key = encryption.generate_key(master_password, salt)
    
    # Decrypt the password
    plain_password = encryption.decrypt_password(encrypted_password, key)
    
    # Retrieve other password information (e.g., username, description)
    username = database.get_username(website)
    description = database.get_description(website)
    
    return {
        "website": website,
        "username": username,
        "password": plain_password,
        "description": description
    }

def delete_password(website):
    database.delete_password(website)

def update_password(old_website, new_website, new_username, new_password, new_description):
    # Fetch the salt used for the old password
    _, salt = database.get_password(old_website)
    
    # Generate a new encryption key using the master password and the existing salt
    master_password = "your_master_password"  # This should be securely obtained
    key = encryption.generate_key(master_password, salt)
    
    # Encrypt the updated password
    encrypted_password = encryption.encrypt_password(new_password, key)
    
    # Update the password entry in the database
    database.update_password(old_website, new_website, new_username, encrypted_password, new_description)

