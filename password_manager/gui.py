import tkinter as tk
from tkinter import simpledialog, messagebox
from password_manager import logic, security, database
import webbrowser

def start():
    window = tk.Tk()
    window.title("Password Manager")
    window.geometry("600x400")  # Set window size

    # Create a master password if none exists
    if not security.master_password_exists():
        master_password = simpledialog.askstring("Master Password", "Create a Master Password", show="*")
        if master_password:
            security.set_master_password(master_password)
            messagebox.showinfo("Success", "Master password created!")
        else:
            messagebox.showerror("Error", "No master password set. Exiting...")
            window.quit()
            return
    
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
        if website and username and password:
            logic.add_password(website, username, password, description)
            messagebox.showinfo("Success", "Password added successfully!")
        else:
            messagebox.showerror("Error", "All fields except description are required.")

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

    # Add buttons for password management
    tk.Button(window, text="Add Password", command=add_password, width=20).pack(pady=10)
    tk.Button(window, text="View Password", command=view_password, width=20).pack(pady=10)
    tk.Button(window, text="Delete Password", command=delete_password, width=20).pack(pady=10)

    # Footer with copyright and GitHub link
    footer_frame = tk.Frame(window)
    footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

    footer_label = tk.Label(footer_frame, text="© 2024 Kuriakos Antoniadis")
    footer_label.pack(side=tk.LEFT, padx=10)

    def open_github():
        webbrowser.open("https://github.com/kuriakosant")

    github_icon = tk.PhotoImage(file="github_icon.png")  # You need a GitHub icon PNG in your directory
    github_button = tk.Button(footer_frame, image=github_icon, command=open_github)
    github_button.image = github_icon  # Keep reference to the image
    github_button.pack(side=tk.RIGHT, padx=10)

    window.mainloop()
