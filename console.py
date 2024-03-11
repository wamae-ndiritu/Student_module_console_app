#!/usr/bin/python3

import csv
import inquirer
import subprocess

def welcome():
    print("Welcome to the Module and Student System (MSS)")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def authenticate(username, password):
    """
    Authenticates the username/password passed by the user.
    Return:
        An empty dict {}, if invalid credentials
        Or a dict with user info.
    """
    with open('./Datasets/User.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        error = {}
        user = {}
        for row in reader:
            if row['UserName'] == username:
                user = row
        if user:
            if user['Password'] == password:
                return user, True
            else:
                error['message'] = "Invalid password!"
        else:
            error['message'] = "Invalid username!"
        return error, False

import tkinter as tk

def view_user_profile(user):
    profile_window = tk.Toplevel(root)
    profile_window.title("User Profile")

    # Display user profile
    profile_frame = tk.Frame(profile_window, padx=20, pady=20)
    profile_frame.pack()

    tk.Label(profile_frame, text="User Profile", font=("Helvetica", 16, "bold")).grid(row=0, columnspan=2)

    user_info = [
            ("Username:", user['UserName']),
            ("First Name:", user['First Name']),
            ("Surname:", user['Surname']),
            ("User Type:", user['UserType']),
            ("Login Status:", user['LoginStatus'])
            ]

    for i, (label, value) in enumerate(user_info, start=1):
        tk.Label(profile_frame, text=label).grid(row=i, column=0, sticky="e")
        tk.Label(profile_frame, text=value).grid(row=i, column=1, sticky="w")

    tk.Button(profile_frame, text="Close", command=profile_window.destroy).grid(row=i+1, columnspan=2)

def main():
    root = tk.Tk()
    root.title("Main Page")

    # Main page widgets
    tk.Label(root, text="Main Page", font=("Helvetica", 16, "bold")).pack()
    tk.Button(root, text="View User Profile", command=lambda: view_user_profile(user_data)).pack()

    root.mainloop()
    welcome()
    attempts = 0
    while attempts < 3:
        username, password = login()
        data, success = authenticate(username, password)
        if success:
            print("Login successful!")
            print(data)
            questions = [
                    inquirer.List('option',
                        message="Select from the menu below:",
                        choices=['1. View user profile', '2. View all modules', '3. Change password', '4. Exit'],
                        carousel=True
                        ),
                    ]
            answer = inquirer.prompt(questions)
            selected_option = int(answer['option'][0])

            if selected_option == 1:
                view_user_profile(data)
            elif selected_option == 4:
                break # Exit the inner loop and return to login page
            break
        else:
            print(data["message"])
            attempts += 1
    else:
        print("You've exceeded the maximum number of login attempts. Your account is blocked.")

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print()
