import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from password_manager import logic, security, database
import webbrowser
import os

def start():
    window = tk.Tk()
    window.title("Simple Python-SQL Password Manager")
    window.geometry("600x500")  # Adjust size

    # Welcome Label
    welcome_label = tk.Label(window, text="Welcome to my Simple Python SQL Password Manager", font=("Helvetica", 14))
    welcome_label.pack(pady=20)

    def add_password_window():
        add_window = tk.Toplevel(window)
        add_window.title("Add New Password")
        add_window.geometry("400x300")

        tk.Label(add_window, text="Website").pack(pady=5)
        website_entry = tk.Entry(add_window)
        website_entry.pack()

        tk.Label(add_window, text="Username").pack(pady=5)
        username_entry = tk.Entry(add_window)
        username_entry.pack()

        tk.Label(add_window, text="Password").pack(pady=5)
        password_entry = tk.Entry(add_window, show="*")
        password_entry.pack()

        tk.Label(add_window, text="Description").pack(pady=5)
        description_entry = tk.Entry(add_window)
        description_entry.pack()

        def submit_password():
            website = website_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            description = description_entry.get()

            if website and username and password:
                # Call the logic to add the password, including encryption and database insertion
                logic.add_password(website, username, password, description)
                messagebox.showinfo("Success", "Password added successfully!")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill all fields!")

        tk.Button(add_window, text="Submit", command=submit_password).pack(pady=20)

    def view_passwords_window():
        view_window = tk.Toplevel(window)
        view_window.title("View Passwords")
        view_window.geometry("400x300")

        passwords = logic.get_all_passwords()

        if not passwords:
            messagebox.showinfo("Info", "No passwords stored!")
            return

        tree = ttk.Treeview(view_window, columns=("Website", "Username"), show="headings")
        tree.heading("Website", text="Website")
        tree.heading("Username", text="Username")

        for pwd in passwords:
            tree.insert("", "end", values=(pwd[1], pwd[2]))

        tree.pack(fill=tk.BOTH, expand=True)

        def on_password_select(event):
            selected_item = tree.selection()[0]
            website = tree.item(selected_item, "values")[0]
            show_password_window(website)

        tree.bind("<Double-1>", on_password_select)

    def show_password_window(website):
        show_window = tk.Toplevel(window)
        show_window.title(f"View Password - {website}")
        show_window.geometry("400x200")

        master_password = simpledialog.askstring("Master Password", "Enter Master Password", show="*")
        if not security.check_master_password(master_password):
            messagebox.showerror("Error", "Incorrect master password!")
            show_window.destroy()
            return

        password_info = logic.view_password(website)
        if password_info:
            tk.Label(show_window, text=f"Website: {password_info['website']}").pack(pady=5)
            tk.Label(show_window, text=f"Username: {password_info['username']}").pack(pady=5)
            tk.Label(show_window, text=f"Password: {password_info['password']}").pack(pady=5)
            tk.Label(show_window, text=f"Description: {password_info['description']}").pack(pady=5)

            def delete_password():
                logic.delete_password(website)
                messagebox.showinfo("Success", "Password deleted successfully!")
                show_window.destroy()

            tk.Button(show_window, text="Delete Password", command=delete_password).pack(pady=10)

        else:
            messagebox.showerror("Error", "Password not found!")

    # Buttons for operations
    tk.Button(window, text="Add Password", command=add_password_window, width=20).pack(pady=10)
    tk.Button(window, text="View Passwords", command=view_passwords_window, width=20).pack(pady=10)

    # Footer with copyright and GitHub link
    footer_frame = tk.Frame(window)
    footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

    footer_label = tk.Label(footer_frame, text="© 2024 Kuriakos Antoniadis")
    footer_label.pack(side=tk.LEFT, padx=10)

    def open_github():
        webbrowser.open("https://github.com/kuriakosant")

    github_icon = tk.PhotoImage(file="assets/github_icon.png")  # You need a GitHub icon PNG in your directory
    github_button = tk.Button(footer_frame, image=github_icon, command=open_github)
    github_button.image = github_icon  # Keep reference to the image
    github_button.pack(side=tk.RIGHT, padx=10)

    window.mainloop()
