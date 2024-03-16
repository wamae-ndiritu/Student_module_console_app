"""
Defines function to facilitate authentication
"""
import csv
import getpass


def login():
    """
    Prompts user to input username/password credentials
    Return:
        (str): The username input
        (str): The Password input
    """
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    return username, password

def authenticate(username, password):
    """
    Checks for the username/password passed in the User.csv.
    Return:
        (dict): For error messages, in case of invalid credentials
                For userInfo in case the record is found
        (boolean): Success status, True if success, False otherwise
        (boolean): True if user is blocked, False otherwise.
    """
    with open('Datasets/User.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        error = {}
        user = {}
        for row in reader:
            if row['UserName'] == username:
                user = row
        isBlocked = False
        if user:
            if user['Password'] == password:
                if user['LoginStatus'] == 'Blocked':
                    error['message'] = "Your account is blocked, You can't login!"
                    isBlocked = True
                    return user, False, isBlocked
                elif user['LoginStatus'] == 'Active':
                    return user, True, isBlocked
            else:
                error['message'] = "Invalid password!"
        else:
            error['message'] = "Invalid username!"
        return error, False, isBlocked
