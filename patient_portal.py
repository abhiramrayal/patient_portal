from tkinter import *
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="Abhi@123", database="test1")
cursor = db.cursor()

def close_window():
    global current_screen
    if current_screen:
        current_screen.destroy()

def signup_page():
    current_screen = Toplevel()
    current_screen.title("Sign Up")
    current_screen.geometry("350x350")

    def register_user():
        user_name = user_name_signup_entry.get()
        password = password_signup_entry.get()
        sql = "INSERT INTO patient (user_name,password) VALUES (%s, %s)"
        values = (user_name, password)
        cursor.execute(sql, values)
        db.commit()
        print("Registration successful")
        messagebox.showinfo("Success", "Registration successful")
    canvas = Canvas(current_screen, width=350, height=350)
    canvas.pack()
    global bg_image_signup 
    bg_image_signup = PhotoImage(file="image2.png")
    canvas.create_image(0, 0, image=bg_image_signup, anchor="nw", tags="background")
    canvas.tag_lower("background")

    Label(canvas, text="Please enter sign up details").place(x=150, y=50)
    Label(canvas, text="user_name").place(x=100, y=100)
    Label(canvas, text="Password").place(x=100, y=150)

    user_name_signup_entry = Entry(canvas)
    password_signup_entry = Entry(canvas, show='*')

    user_name_signup_entry.place(x=200, y=100)
    password_signup_entry.place(x=200, y=150)

    Button(canvas, text="Register", width=10, height=1, command=register_user).place(x=170, y=200)
    Button(canvas, text="Back", width=10, height=1, command=login_page).place(x=170, y=250)

    current_screen.mainloop()

def display_data(user_name):
    conn = mysql.connector.connect(host="localhost", user="root", password="Abhi@123", database="test1")
    cursor = conn.cursor()
    query = "SELECT * FROM `patient_data` WHERE user_name= %s"
    cursor.execute(query, (user_name,))
    data = cursor.fetchall()
    conn.close()

    window = Tk()
    window.geometry("350x350")


    canvas = Canvas(window, width=350, height=350)
    canvas.pack()
    for row_index, row_data in enumerate(data):
        for col_index, value in enumerate(row_data):
            label = Label(canvas, text=value)
            label.grid(row=row_index, column=col_index)

    window.mainloop()

def login_page():
    current_screen = Tk()
    current_screen.title("Login")
    current_screen.geometry("350x350")

    canvas = Canvas(current_screen, width=350, height=350)
    canvas.pack()

    global bg_image_login 
    bg_image_login = PhotoImage(file="image2.png")
    canvas.create_image(0, 0, image=bg_image_login, anchor="nw", tags="background")
    canvas.tag_lower("background")

    def authenticate_user():
        user_name = user_name_login_entry.get()
        password = password_login_entry.get()
        cursor.execute("SELECT * FROM patient WHERE user_name = %s AND password = %s", (user_name, password))
        row = cursor.fetchone()
        if row:
            print("Login successful")
            messagebox.showinfo("Success", "Login Successful!")
            display_data(user_name)
        else:
            print("Login failed")
            messagebox.showerror("Error", "Invalid Credentials")

    Label(canvas, text="Please enter login details").place(x=150, y=50)
    Label(canvas, text="user_name").place(x=100, y=100)
    Label(canvas, text="Password").place(x=100, y=150)

    user_name_login_entry = Entry(canvas)
    password_login_entry = Entry(canvas, show='*')

    user_name_login_entry.place(x=200, y=100)
    password_login_entry.place(x=200, y=150)

    Button(canvas, text="Login", width=10, height=1, command=authenticate_user).place(x=170, y=200)
    Button(canvas, text="Sign Up", width=10, height=1, command=signup_page).place(x=170, y=250)

    current_screen.mainloop()

login_page()
