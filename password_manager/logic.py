from password_manager import encryption, database

def add_password(website, username, plain_password, description):
    key = encryption.generate_key("master_password")
    encrypted_password = encryption.encrypt_password(plain_password, key)
    database.insert_password(website, username, encrypted_password, description)

def view_password(website):
    key = encryption.generate_key("master_password")
    encrypted_password = database.get_password(website)
    if encrypted_password:
        return encryption.decrypt_password(encrypted_password, key)
    else:
        return None

def delete_password(website):
    database.delete_password(website)
