import tkinter as tk
from tkinter import simpledialog, messagebox
from password_manager import logic, security

def start():
    window = tk.Tk()
    window.title("Password Manager")
    
    def login():
        master_password = simpledialog.askstring("Master Password", "Enter Master Password", show="*")
        if not security.check_master_password(master_password):
            messagebox.showerror("Error", "Incorrect master password. Exiting...")
            window.quit()
            return False
        return True

    if not login():
        return

    def add_password():
        website = simpledialog.askstring("Website", "Enter the website:")
        username = simpledialog.askstring("Username", "Enter the username:")
        password = simpledialog.askstring("Password", "Enter the password:")
        description = simpledialog.askstring("Description", "Enter any description (optional):")
        logic.add_password(website, username, password, description)
        messagebox.showinfo("Success", "Password added successfully!")

    def view_password():
        website = simpledialog.askstring("Website", "Enter the website to view:")
        password = logic.view_password(website)
        if password:
            messagebox.showinfo("Password", f"Password for {website}: {password}")
        else:
            messagebox.showerror("Error", "Password not found for that website.")

    def delete_password():
        website = simpledialog.askstring("Website", "Enter the website to delete:")
        logic.delete_password(website)
        messagebox.showinfo("Success", "Password deleted successfully.")

    tk.Button(window, text="Add Password", command=add_password).pack(pady=10)
    tk.Button(window, text="View Password", command=view_password).pack(pady=10)
    tk.Button(window, text="Delete Password", command=delete_password).pack(pady=10)
    
    window.mainloop()
