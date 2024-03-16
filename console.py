"""
Defines the console entry point.
"""
import csv
import inquirer
from Helpers import select_menu_options, block_user, show_logged_user
from Auth import login, authenticate
from General import view_user_profile, view_modules, view_user_modules, change_password
from Student import register_module, withdraw_module
from Lecturer import create_module, update_student_record


def main():
    """
    Main entry point of the Console App
    """
    print("Welcome to the Module and Student System (MSS)")
    attempts = 0
    userData = None
    while attempts < 3:
        username, password = login()
        data, success, isBlocked = authenticate(username, password)
        userData = username
        if success:
            show_logged_user(data)
            while True:
                choice_list = []
                if data['UserType'] == 'Student':
                    choice_list = [
                            '1. View user profile',
                            '2. View all modules',
                            '3. Change password',
                            '4. View my modules',
                            '5. Register a module',
                            '6. Withdraw from a module',
                            '9. Exit'
                            ]
                elif data['UserType'] == 'Lecturer':
                    choice_list = [
                            '1. View user profile',
                            '2. View all modules',
                            '3. Change password',
                            '4. View my modules',
                            '7. Create a module',
                            '8. Update student records',
                            '9. Exit'
                            ]
                selected_option = select_menu_options(
                        "Select from the menu below",
                        choice_list
                        )
                
                if selected_option == 1:
                    exit_option = view_user_profile(data)
                    if exit_option == 1:
                        continue
                elif selected_option == 2:
                    exit_option = view_modules()
                    if exit_option == 1:
                        continue
                elif selected_option == 3:
                    exit_option = change_password(data['UserName'])
                    if exit_option == 1:
                        continue
                elif selected_option == 4:
                    exit_option = view_user_modules(data['UserName'])
                    if exit_option == 1:
                        continue
                elif selected_option == 5:
                    exit_option = register_module(data['UserName'])
                    if exit_option == 1:
                        continue
                elif selected_option == 6:
                    exit_option = withdraw_module(data['UserName'])
                    if exit_option == 1:
                        continue
                elif selected_option == 7:
                    create_module()
                elif selected_option == 8:
                    update_student_record()
                elif selected_option == 9:
                    break # Exit the inner loop
                else:
                    print(selected_option)
                    break
            break
        else:
            if isBlocked:
                print("Your account is blocked, You can't login!")
                break
            print(data["message"])
            attempts += 1
    else:
        if userData:
            block_user(userData)
            print("You've exceeded the maximum number of login attempts. Your account is blocked.")

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print()
