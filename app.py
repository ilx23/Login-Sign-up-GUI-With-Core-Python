import json
from tkinter import *
from tkinter import messagebox


def login_form_setup():
    """Display the login form."""
    global login_email_entry, login_password_entry

    # Delete widgets from the previous page
    for widget in app.winfo_children():
        widget.destroy()

    # Set up the UI for the login form
    login_label = Label(app, text="Login Form", font=("nectar bold", 17, "bold"))
    login_label.pack()

    # Add underline for separation
    underline_login_text = Label(app, text="_______________________________________________________________________")
    underline_login_text.pack()

    # Labels and Entry widgets for email and password
    login_email_label = Label(app, text="Enter Your Email Address", font=("aria", 12))
    login_email_label.pack(pady=20)
    login_email_entry = Entry(app, width=31, borderwidth=2, relief=GROOVE)
    login_email_entry.pack()

    login_password_label = Label(app, text="Enter Your Password", font=("aria", 12))
    login_password_label.pack(pady=20)
    login_password_entry = Entry(app, width=31, borderwidth=2, relief=GROOVE)
    login_password_entry.pack()

    # Login and signup buttons
    login_button = Button(app, text="Login", font=("aria", 13), borderwidth=2, relief=GROOVE, command=login)
    login_button.pack(side='left', pady=20, padx=87)
    signup_button = Button(app, text="New Account", font=("aria", 13), borderwidth=2, relief=GROOVE,
                           command=signup_form_setup)
    signup_button.pack(side='left')


def signup_form_setup():
    """Display the signup form."""
    global signup_email_entry, signup_password_entry, signup_repeat_entry

    # Delete widgets from the previous page
    for widget in app.winfo_children():
        widget.destroy()

    # Set up the UI for the signup form
    signup_label = Label(app, text="Sign Up Form", font=("nectar bold", 17, "bold"))
    signup_label.pack()
    underline_text = Label(app, text="_______________________________________________________________________")
    underline_text.pack()

    # Labels and Entry widgets for email, password, and password confirmation
    signup_email_label = Label(app, text="Enter Your Email Address: ", font=("aria", 12))
    signup_email_label.pack(pady=20)
    signup_email_entry = Entry(width=31, borderwidth=2, relief=GROOVE)
    signup_email_entry.pack()

    signup_password_label = Label(app, text="Enter Your Password: ", font=("aria", 12))
    signup_password_label.pack(pady=10)
    signup_password_entry = Entry(width=31, borderwidth=2, relief=GROOVE)
    signup_password_entry.pack()

    signup_repeat_label = Label(app, text="Repeat Your Password: ", font=("aria", 12))
    signup_repeat_label.pack(pady=20)
    signup_repeat_entry = Entry(width=31, borderwidth=2, relief=GROOVE)
    signup_repeat_entry.pack()

    # Signup and login buttons
    signup_submit_button = Button(app, text="Sign Up", borderwidth=2, font=("aria", 13), relief=GROOVE,
                                  command=create_account)
    signup_submit_button.pack(pady=20, padx=87, side='left')
    login_button = Button(app, text="Login", borderwidth=2, font=("aria", 13), relief=GROOVE, command=login_form_setup)
    login_button.pack(side='left')


def create_account():
    """Create a new user account."""
    email = signup_email_entry.get()
    password = signup_password_entry.get()
    repeated_password = signup_repeat_entry.get()

    # Validate email, password, and password confirmation
    if email == "":
        messagebox.showerror("Error", "Please Enter Your Email Address")
    elif password == "":
        messagebox.showerror("Error", "Please Enter Your Password")
    elif repeated_password != password:
        messagebox.showerror("Error", "Please Repeat Your Password Correctly")
    else:
        new_user = {email: password}
        try:
            # Read existing data from JSON file
            with open('data.json', 'r') as data_value:
                data = json.load(data_value)
                # Check if email already exists
                if email in data:
                    messagebox.showerror("Error", "Email already registered")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # If file doesn't exist or is empty, create a new one with the new user
            with open('data.json', 'w') as data_value:
                json.dump(new_user, data_value, indent=4)
        else:
            # Update data with the new user and write to JSON file
            data.update(new_user)
            with open('data.json', 'w') as data_value:
                json.dump(data, data_value, indent=4)
        finally:
            # Clear the signup form after submission
            signup_email_entry.delete(0, END)
            signup_password_entry.delete(0, END)
            signup_repeat_entry.delete(0, END)


def login():
    """Handle user login."""
    email = login_email_entry.get()
    password = login_password_entry.get()
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
        if email == "":
            messagebox.showerror("Error", "Please enter your email")
        elif password == "":
            messagebox.showerror("Error", "Please enter your password")
        else:
            try:
                user_password = data[email]
                if user_password == password:
                    messagebox.showinfo("Success", "You are now logged in")
                    signup_form_setup()
                else:
                    messagebox.showerror("Error", "Wrong password")
            except KeyError:
                messagebox.showerror("Error", "The email is not registered")


# UI setup
app = Tk()
app.title("Login & Sign up Form")
app.geometry("400x400")
app.config(padx=10, pady=10)

# Start the program with the signup form
signup_form_setup()

# Start the Tkinter event loop
app.mainloop()
