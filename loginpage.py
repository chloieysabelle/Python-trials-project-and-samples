import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector

connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="projectksksk"
   )

def create_signup_box():
    signup_box = tk.Frame(root, borderwidth=2, relief="ridge", padx=10, pady=10)
    signup_box.pack(padx=20, pady=20)

    First_name_label = tk.Label(signup_box, text="First Name:")
    First_name_label.pack(anchor="w")
    First_name_entry = tk.Entry(signup_box)  
    First_name_entry.pack(fill="x", padx=10, pady=5)

    Last_name_label = tk.Label(signup_box, text="Last Name:")
    Last_name_label.pack(anchor="w")
    Last_name_entry = tk.Entry(signup_box)  
    Last_name_entry.pack(fill="x", padx=10, pady=5)

    email_label = tk.Label(signup_box, text="Email Address:")
    email_label.pack(anchor="w")
    email_entry = tk.Entry(signup_box)
    email_entry.pack(fill="x", padx=10, pady=5)

    password_label = tk.Label(signup_box, text="Password:")
    password_label.pack(anchor="w")
    password_entry = tk.Entry(signup_box, show="*")  
    password_entry.pack(fill="x", padx=10, pady=5)

    entry_variable = tk.StringVar(signup_box, text="Create Account", command=signup)
    entry.pack(pady=10)

def signup(first_name_entry, last_name_entry, email_entry, password_entry):

   first_name = first_name_entry.get()
   last_name = last_name_entry.get()
   email = email_entry.get()
   password = password_entry.get()
   
   
   mycursor = connection.cursor()
   insert_query = "INSERT INTO user_account (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
   user_data = (first_name, last_name)  
   mycursor.execute(insert_query, user_data)
   
   connection.commit()

root = tk.Tk()
root.geometry("700x500")
root.title("Account Information")

image = Image.open("C:/Users/Chloie/Documents/project/hospitalpic.jpg")
image = image.resize((700, 500), Image.BOX)
photo = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=photo)
background_label.place(x=0,y=0, relwidth=1, relheight=1)


label = tk.Label(root,
                  text="Hospital Management System",
                  font=("Times", "24", "bold"),
                  fg="red"
                  )
label.pack(padx=50, pady=10)

label = tk.Label(root,
                  text="Sign up here:",
                  font=("Times", "14"),
                  fg="black"
                  )
label.pack(padx=50, pady=10)

create_signup_box()


root.mainloop()


