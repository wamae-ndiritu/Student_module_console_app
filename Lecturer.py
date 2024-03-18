"""
Defines all the functions of the Lecturer in the MSS
"""
import csv
from Helpers import select_menu_options

def create_module():
    """
    Creates a new row in the Module.csv file
    """
    print("Create a new module")
    course_code = input("Enter the course code: ").strip()
    course_name = input("Enter the course name: ").strip()

    # Check for empty course code
    if not course_code or not course_name:
        print("Course code or name cannot be empty. Module creation failed.")
        return True

    modules = []

    with open('Datasets/Module.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        modules = list(reader)
    
    # Check for duplicates
    if any(module['ModuleID'] == course_code or module['ModuleName'] == course_name for module in modules):
        print("A module with that ModuleID or ModuleName already exists!")
        return True
    

    new_course = {"ModuleID": course_code, "ModuleName": course_name}
    modules.append(new_course)

    # Write the updated data back to the CSV file
    try:
        with open('Datasets/Module.csv', 'w', newline='') as csvfile:
            fieldnames = ['ModuleID', 'ModuleName']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(modules)
            print("Module created successfully!")
    except:
        print("An error occurred trying to create module!")


def update_student_record():
    """
    Updates a certain row in the User.csv where the UserType column
    value is Student
    """
    print("Update Students Record")
    student_name = input("Enter student's UserName: ")
    student_name = student_name.strip()
    users = []
    user_to_update = None
    with open('Datasets/User.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        users = list(reader)

        for user in users:
            if user['UserName'] == student_name and user['UserType'] == 'Student':
                user_to_update = user

    if user_to_update:
        # Update user
        while True:
            selected_option = select_menu_options("Choose what to update",
                    ['1. First Name', '2. Surname', '3. LoginStatus', '4. Save and Exit'])
            if selected_option == 1:
                new_first_name = input("Enter New First Name: ")
                user_to_update['First Name'] = new_first_name.strip()
            elif selected_option == 2:
                new_surname = input("Enter New Surname: ")
                user_to_update['Surname'] = new_surname.strip()
            elif selected_option == 3:
                loginStatus = user_to_update['LoginStatus']
                choices = ['0. Go Back']
                if loginStatus == 'Blocked':
                    choices.append('1. Unblock Student')
                selected_option = select_menu_options("Block/Unblock student", choices)
                if selected_option == 0:
                    continue # End the loop
                elif selected_option == 1:
                    user_to_update['LoginStatus'] = 'Active'
            elif selected_option == 4:
                for user in users:
                    if user['UserName'] == user_to_update['UserName']:
                        user = user_to_update
                try:
                    with open('Datasets/User.csv', 'w', newline='') as csvfile:
                        fieldnames = ['UserName', 'Password', 'First Name', 'Surname', 'UserType', 'LoginStatus']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(users)
                        print("Student records updated successfully!")
                        break
                except:
                    print("An error occured updating record!")
                    break
    else:
        print("No student found with that UserName!")
        return

