from cryptography.fernet import Fernet

def generate_key(master_password):
    # Derive a key from the master password
    key = Fernet.generate_key()
    return key

def encrypt_password(plain_password, key):
    cipher = Fernet(key)
    return cipher.encrypt(plain_password.encode())

def decrypt_password(encrypted_password, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password).decode()
