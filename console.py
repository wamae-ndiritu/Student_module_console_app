#!/usr/bin/python3

import cmd
import csv

class MSS(cmd.Cmd):
    """
    Command Interpreter for the Module and Student System (MSS)
    """
    prompt = '(MSS) '

    def do_quit(self, line):
        """Quit command to exit the program

        """
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_EOF(self, line):
        """
        Handle end of file
        """
        print()
        return True

# Dataset containing usernames and passwords
user_data = {
        'student1': 'password1',
        'student2': 'password2',
        'lecturer1': 'password3',
        'lecturer2': 'password4'
        }

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

def main():
    welcome()
    attempts = 0
    while attempts < 3:
        username, password = login()
        data, success = authenticate(username, password)
        if success:
            print("Login successful!")
            print(data)
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
