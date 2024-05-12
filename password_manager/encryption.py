import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# Use PBKDF2 to derive a key from the master password
def generate_key(master_password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm='SHA256',
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

# Encrypt the plain password using the derived key
def encrypt_password(plain_password: str, key: bytes):
    cipher = Fernet(key)
    return cipher.encrypt(plain_password.encode())

# Decrypt the password using the derived key
def decrypt_password(encrypted_password: bytes, key: bytes):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password).decode()
