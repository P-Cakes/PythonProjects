from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # Insert the generated password into the password entry box
    password_entry.insert(0, password)
    # This copies the password to your clipboard so you can put it into the website
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    # We don't want to save empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops",
                            message = "Please don't leave any fields empty!")
    # If not empty, begin to save the data
    else:
        try:
            # Open the file in read mode to see what is already there
            with open("data.json", mode = "r") as file:
                existing_data = json.load(file)
        # If it's the first time running the program, file doesn't exist
        # create the file and write the new data
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        # This else block could have just been done in the try block
        # But this is theoretically nicer
        else:
            # Update old data with new data
            existing_data.update(new_data)
            # Open the file in write mode to write the new data
            with open("data.json", mode = "w") as file:
                json.dump(existing_data, file, indent = 4)
        # Finally, no matter what, clear our entry boxes
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def search():
    """" Search for the website in the data.json file and return the email and password if it exists."""
    # Get the website from the entry box
    website = website_entry.get()
    # If the file doesn't exist, show an error message
    try:
        with open("data.json", mode = "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No Data File Found")
    # Assuming we opened the file, check if the website exists in the data
    else:
        # If the website exists, show the email and password
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")
            # Copy the password to the clipboard
            pyperclip.copy(password)
        # If the website doesn't exist, show an error message
        else:
            messagebox.showinfo(title = "Error", message = f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady = 50)

canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)
email_label = Label(text = "Email/Username:")
email_label.grid(row = 2, column = 0)
password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)

website_entry = Entry(width = 21)
website_entry.grid(row = 1, column = 1, columnspan = 1)
search_button = Button(text = "Search", width = 14, command = search)
search_button.grid(row = 1, column = 2)
email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, columnspan = 2)
password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1)
gen_pass_button = Button(text = "Generate Password", command = generate_password)
gen_pass_button.grid(row = 3, column = 2)
add_button = Button(text = "Add", width = 36, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)

# put your cursor in the entry box on open
website_entry.focus()
# prefill the email entry box
email_entry.insert(0,"my_email@gmail.com")


window.mainloop()


