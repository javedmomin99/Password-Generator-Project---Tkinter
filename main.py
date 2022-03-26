# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip
import random 

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    number_letters = random.randint(8,10)
    number_numbers = random.randint(2,4)
    number_symbols = random.randint(2,4)
    password_list = []
    for password_letter in range(number_letters):
        password_letter = random.choice(letters)
        password_list.append(password_letter)
    for password_numbers in range(number_numbers):
        password_numbers = random.choice(numbers)
        password_list.append(password_numbers)
    for password_symbols in range(number_symbols):
        password_symbols = random.choice(symbols)
        password_list.append(password_symbols)
    #print(password_list)
    random.shuffle(password_list)
    #print(password_list)
    password = ""
    for char in password_list:
        password = password + char
    #print(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    #Join Method (The Above Password Generation can also be done using Join Method)
    #password = "".join(password_list)
    #print(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
import messagebox
def save():

    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please Make Sure You Haven't left any fields Empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered : \nEmail : {email}\nPassword : {password}\nIs it Okay to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file = file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
                #0 means starting from Initial Character and tkinter.End means uptil end of All Characters       

# ---------------------------- UI SETUP ------------------------------- #
import tkinter
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(200/2, 200/2, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = tkinter.Label(text="Website")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="E-mail ID")
email_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password")
password_label.grid(column=0, row=3)

#Entry
website_entry = tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"javedmomin99@gmail.com")
#0 means starting from character length 0 
password_entry = tkinter.Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)
password_entry.focus()



#Buttons

generate_password_button = tkinter.Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=3)
add_button = tkinter.Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
