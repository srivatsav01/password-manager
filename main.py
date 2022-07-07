from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# -----------------------------------------PASSWORD GENERATOR ---------------------- #
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
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ------------------------------------------SAVE PASSWORD ----------------------- #

def saving_password():
    password = password_entry.get()
    website = website_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(password) == 0 or len(website) == 0:

        messagebox.showinfo(title= "Oops!", message="Don't leave any of the boxes empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file)

        else:
            with open("data.json", "w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


#-----------------------------------searching password -----------------------------------#

def search():
    searching_website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="add a website ",message="Currently your password manager is empty")
    else:
        if searching_website in data:
            email_assoc = data[searching_website]["email"]
            password_assoc = data[searching_website]["password"]
            messagebox.showinfo(title=searching_website, message=f"email:{email_assoc}\npassword:{password_assoc}")
        elif len(searching_website) != 0:
            messagebox.showinfo(title="website not found in manager",message="Check if there is any spelling mistake")
        else:
            messagebox.showinfo(title= "website field",message="website field cannot be empty")








# -------------------------------------------UI SETUP -------------------------- #
window = Tk()
window.minsize(550,550)
window.config(padx = 20,pady = 0)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0,padx = 10 , pady =10)


#label website
website_text = Label(text = "Website:")
website_text.grid(column = 0,row = 1)

#input of website
website_entry = Entry(width = 35)
website_entry.grid(column =1 , row = 1 ,columnspan =2,padx = 10 , pady =10 )
website_entry.focus()

#search button
search_btn = Button(text = "Search",width = 10,command = search)
search_btn.grid(column = 3, row = 1,padx = 2)


#label email
email_text = Label(text = "Email/Username:")
email_text.grid(column= 0,row =2 ,padx = 10 , pady =10)

#input email
email_entry = Entry(width = 35)
email_entry.grid(column = 1, row = 2,columnspan = 2,padx = 10 , pady =10)
email_entry.insert(0,"srivatsav@gmail.com")

#label password
password_text = Label(text = "Password:")
password_text.grid(column = 0,row = 3,padx = 10 , pady =10)

#input password
password_entry = Entry(width = 21)
password_entry.grid(column = 1 ,row = 3 ,padx = 10 , pady =10)

#buttons
generate_button = Button(text = "Generate",command = generate_password)
generate_button.grid(column = 2,row = 3,padx = 10 , pady =10)

add_button = Button(text = "Add",width =20,command = saving_password)
add_button.grid(column = 1,row = 4,columnspan =2,padx = 10 , pady =10)



















window.mainloop()