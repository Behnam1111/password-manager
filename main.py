from tkinter import *
from tkinter import messagebox

WHITE = '#FFFFFF'
FONT_NAME = "Hourier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website and email and password:
        is_ok = messagebox.askokcancel(title='website', message=f'the email you have entered is {email}\nthe password you '
                                                                f'have entered is {password}\n are you sure you want to '
                                                                f'save?')
        if is_ok:
            with open('data.txt', 'a') as data:
                record = f"{website} | {email} | {password}\n"
                data.write(record)
                website_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
    else:
        messagebox.showwarning(title='empty', message='please do not leave any fields empty')


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

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

password_generator_button = Button(text="Generate Password", bg=WHITE, font=(FONT_NAME, 5, 'bold'), width=15)
password_generator_button.grid(row=3, column=2)

add_button = Button(text="Add Password", bg=WHITE, width=46, font=(FONT_NAME, 6, 'bold'), command=save)
add_button.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
password_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

window.mainloop()
