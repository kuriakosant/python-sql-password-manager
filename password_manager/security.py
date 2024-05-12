MAX_ATTEMPTS = 10
attempts = 0

def check_master_password(entered_password):
    global attempts
    if entered_password == "correct_master_password":  # Use a hashed version of the password
        attempts = 0
        return True
    else:
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            from password_manager import database
            database.delete_all_passwords()
            return False
        return False
