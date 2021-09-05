from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

WHITE = '#FFFFFF'
FONT_NAME = "Hourier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website and email and password:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
    else:
        messagebox.showwarning(title='empty', message='please do not leave any fields empty')


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title=website, message='No data file found')
    else:
        if data.get(website):
            messagebox.showinfo(title=website, message=f'username is {data.get(website)["email"]} \n password is'
                                                       f' {data.get(website)["password"]}')
        else:
            messagebox.showwarning(title=website, message='there is no website with this email')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=WHITE)

website_label = Label(text='Website:', bg=WHITE)
website_label.grid(row=1, column=0)

website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text='Email/Username:', bg=WHITE)
email_label.grid(row=2, column=0)

email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'Behnam@gmail.com')

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(row=3, column=0)

password_entry = Entry(width=37)
password_entry.grid(row=3, column=1)

password_generator_button = Button(text="Generate Password", bg=WHITE, font=(FONT_NAME, 5, 'bold'), width=17,
                                   command=generate_password)
password_generator_button.grid(row=3, column=3)

add_button = Button(text="Add Password", bg=WHITE, width=46, font=(FONT_NAME, 6, 'bold'), command=save)
add_button.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
password_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

search_button = Button(text='Search', bg=WHITE, highlightthickness=0, font=(FONT_NAME, 6, 'bold'), width=14
                       , command=find_password)
search_button.grid(row=1, column=3)

window.mainloop()
