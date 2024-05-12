from password_manager import encryption, database

def add_password(website, username, plain_password, description):
    key = encryption.generate_key("master_password")
    encrypted_password = encryption.encrypt_password(plain_password, key)
    database.insert_password(website, username, encrypted_password, description)

def get_all_passwords():
    return database.get_all_passwords()

def view_password(website):
    key = encryption.generate_key("master_password")
    encrypted_password = database.get_password(website)
    if encrypted_password:
        plain_password = encryption.decrypt_password(encrypted_password, key)
        password_data = {
            "website": website,
            "username": database.get_username(website),
            "password": plain_password,
            "description": database.get_description(website)
        }
        return password_data
    return None

def delete_password(website):
    database.delete_password(website)
