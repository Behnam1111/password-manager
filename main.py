from tkinter import *
WHITE = '#FFFFFF'
FONT_NAME = "Hourier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=WHITE)

website_label = Label(text='Website:', bg=WHITE)
website_label.grid(row=1, column=0)

website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text='Email/Username:', bg=WHITE)
email_label.grid(row=2, column=0)

email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(row=3, column=0)

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

password_generator_button = Button(text="Generate Password", bg=WHITE, font=(FONT_NAME, 5, 'bold'), width=15)
password_generator_button.grid(row=3, column=2)

add_button = Button(text="Add Password", bg=WHITE, width=46, font=(FONT_NAME, 6, 'bold'))
add_button.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
password_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

window.mainloop()
