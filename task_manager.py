# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

# Programmer notes:
# 1. Remember if you make a change to any task, for this to show up in the statistics, you must first generate the reports.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

#=====defining functions============

def reg_user():
    # restrict permissions
    if curr_user != 'admin':
        print("Sorry, you do not have permission to execute this action.")
    
    else:
        # - Request input of a new username
        new_username = input("New Username: ")

        # - prevent duplicate usernames
        while new_username in username_password.keys():
            new_username = input("Sorry. That username is already taken. Please choose another: ")

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
                
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
        
        else:
            print("Passwords do not match. Unable to add new user. Enter 'r' to try again.") # improved output message

def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task
    '''

    # refactoring to a function, removing the if / continue commands and replacing with a while loop
    task_username = input("Name of person assigned to task: ")
    while task_username not in username_password.keys():
        task_username = input("User does not exist. Please enter a valid username: ")

    # gathering all other input required to complete information about the task
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # every time a task is generated, the following code writes it in the required format into the task file
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.") # user friendly confirmatory message


def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
    '''
    personal_task_count = 0 # adding a task number as a unique task list for each user
    personal_task_dict = {} # populate a personal task dictionary with all tasks assigned to current user
    print(f"Tasks assigned to {curr_user}:\n")
    for t in task_list:
        if t['username'] == curr_user:
            personal_task_count += 1 # every task assigned to curr_user is counted
            disp_str = f"Task: {personal_task_count} - "
            disp_str += str(t['title']) + "\n"
            disp_str += f"Notes: {t['description']}\n"
            disp_str += f"Date Assigned: {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\t"
            disp_str += f"Due Date: {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            personal_task_dict[personal_task_count] = t['title']
            print(disp_str)

    # managing the tasks assigned to curr_user
    try:
        task_manager = int(input(f"Please enter task number in order to manage {curr_user}'s tasks or enter -1 to return to the main menu: "))
        while task_manager not in personal_task_dict.keys() and task_manager != -1:
            task_manager = int(input(f"Please enter a valid task number currently assigned to {curr_user}: "))

    # input is left as strings here as use of integers is not required and validating the input is simpler with strings
        if task_manager in personal_task_dict.keys():
            task_manager_option = input(f'''
            \tEnter 1 to mark Task {task_manager} as complete.
            \tEnter 2 to edit assignation of Task {task_manager}.
            \tEnter 3 to edit due date of Task {task_manager}.
            ''')

            while task_manager_option != '1' and task_manager_option != '2' and task_manager_option != '3':
                task_manager_option = input("Please enter 1-3 as prompted above: ")
            
            # calling mark_task_completed function
            if task_manager_option == '1':
                mark_task_completed(curr_user, personal_task_dict[task_manager])
    
            # calling edit_assignation function
            elif task_manager_option == '2':
                edit_assignation(curr_user, personal_task_dict[task_manager])
            
            # preventing any value errors from input providing invalid date format
            else:
                dummy = 1
                while dummy == 1:
                    try:
                        edit_due_date(curr_user, personal_task_dict[task_manager])
                        dummy = 2
                    except ValueError:
                        print("Invalid date format. Try again.")

        else:
            return

    except ValueError:
        print("Invalid input. Returning to main menu.")

def mark_task_completed(username, task_title):
# function performed on tasks that relies on username and task_title as its identifiers and marks the task complete.

    with open('tasks.txt', 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        parts = lines[i].split(';')
        if parts[0] == username and parts[1] == task_title:
            lines[i] = f"{parts[0]};{parts[1]};{parts[2]};{parts[3]};{parts[4]};Yes\n"

    with open('tasks.txt', 'w') as file:
        file.writelines(lines)
        print(f"Task: \"{task_title}\" marked as complete.")

def edit_assignation(username, task_title):
# function performed on tasks that relies on username and task_title as its identifiers and gives the option to the user to change who the task is assigned to.

    with open('tasks.txt', 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        parts = lines[i].split(';')
        if parts[0] == username and parts[1] == task_title:

            # ensuring task can't be edited if it is marked as complete.
            if parts[0] == username and parts[1] == task_title and parts[5][0:3] == "Yes":
                print("Sorry, this task cannot be edited since it has been marked as complete.")

            else:
                print(f"Enter username below to assign \"{task_title}\" to the user.")
                new_username = input("")

                # iterating over keys rather than whole dictionary to preclude any passwords set as the intended new username
                while new_username not in username_password.keys():
                    new_username = input("Sorry. Username not recognised. Please try again. ")
                lines[i] = f"{new_username};{parts[1]};{parts[2]};{parts[3]};{parts[4]};{parts[5]}"
    
                with open('tasks.txt', 'w') as file:
                    file.writelines(lines)
                    print(f"Task: \"{task_title}\" successfully assigned to {new_username}.")


def edit_due_date(username, task_title):
# function performed on tasks that relies on username and task_title as its identifiers and gives the option to the user to edit the due date of a task.

    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
    
    for i in range(len(lines)):
        parts = lines[i].split(';')
        if parts[0] == username and parts[1] == task_title:

            # ensuring task can't be edited if it is marked as complete.
            if parts[0] == username and parts[1] == task_title and parts[5][0:3] == "Yes":
                print("Sorry, this task cannot be edited since it has been marked as complete.")

            else:
                print(f"Current due date of task is {parts[3]}. Please enter new desired due date in format [YYYY-MM-DD].")
                new_due_date = input("")
                due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)

                lines[i] = f"{parts[0]};{parts[1]};{parts[2]};{new_due_date};{parts[4]};{parts[5]}"

                with open('tasks.txt', 'w') as file:
                    file.writelines(lines)
                    print(f"Task: \"{task_title}\" due date successfully changed to {new_due_date}.")

def tasks_completed(status):
# function to be called to count the amount of tasks based on their completion status. Status should be "Yes" or "No".

    with open('tasks.txt', 'r') as file:
        lines = file.readlines()

    count = 0
    for i in range(len(lines)):
        parts = lines[i].split(';')
        if parts[5].strip() == status:
            count += 1
    return count

def tasks_overdue():
# function to be called to count the amount of tasks that are overdue.

    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
    
    count = 0
    for i in range(len(lines)):
        parts = lines[i].split(';')
        if parts[5].strip() == "No":
            due_date = datetime.strptime(parts[3], DATETIME_STRING_FORMAT)
            if datetime.today() > due_date:
                count += 1
    return count

def percentage(x, y):
# function to be called to calculate the percentage of x and y, and return with '%' character.

    if float(y) == 0:
        return "0.0%\t"
    percent = round(100 * float(x) / float(y), 1)
    return str(percent) + "%"

def user_completed(user, status):
# function similar to tasks_completed, but this time specific to a user

    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
    
    count = 0
    for i in range(len(lines)):
        parts = lines[i].split(';')
        if user == parts[0] and parts[5].strip() == status:
            count += 1
    
    return count

def user_overdue(user):
# function similar to tasks_overdue, but this time specific to a user

    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
    
    count = 0
    for i in range(len(lines)):
        parts = lines[i].split(';')
        if parts[5].strip() == "No" and user == parts[0]:
            due_date = datetime.strptime(parts[3], DATETIME_STRING_FORMAT)
            if datetime.today() > due_date:
                count += 1
    return count

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        task_count = (len(task_list))

        # writing the file task_overview.txt as this will contain one of the reports that we are generating
        with open("task_overview.txt", "w") as file:
            file.write(f"Number of tasks generated: {task_count}\n")
            file.write(f"Number of completed tasks: {tasks_completed("Yes")}\n")
            file.write(f"Number of uncompleted tasks: {tasks_completed("No")}\n")
            file.write(f"Number of overdue tasks: {tasks_overdue()}\n")
            file.write(f"Percentage of tasks that are incomplete: {percentage(tasks_completed("No"), task_count)}\n")
            file.write(f"Percentage of tasks that are overdue: {percentage(tasks_overdue(), task_count)}\n")

        # writing the file user_overview.txt as this will contain the other report that we are generating
        with open("user_overview.txt", 'w') as file:
            file.write(f"Total number of users registered: {len(username_password)}\n")
            file.write(f"Number of tasks generated: {task_count}\n")
            
            with open('tasks.txt', 'r') as task_file:
                lines = task_file.readlines()

        # create a list of all users with tasks assigned to them, generating a new item for each task (so usernames can be repeated as many times as they are in tasks.txt)
            user_list = []
            for i in range(len(lines)):
                parts = lines[i].split(';')
                user_list.append(parts[0])

            for user in username_password.keys():
                user_overview_str = (f'''Username: {user} \tAssigned tasks: {user_list.count(user)}\n\
    \t% of all tasks assigned to user: {percentage(user_list.count(user), task_count)}\t% Completed: {percentage(user_completed(user, "Yes"), user_list.count(user))}\t\
    % To be completed: {percentage(user_completed(user, "No"), user_list.count(user))}\t% Overdue: {percentage(user_overdue(user), user_list.count(user))}\n''')
                file.write(user_overview_str)
                

    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''

        # creating task_overview if it doesn't exist
        if not os.path.exists('task_overview.txt'):
            with open("task_overview.txt", 'w') as file:
                pass
    
        # creating user_overview if it doesn't exist
        if not os.path.exists('user_overview.txt'):
            with open("user_overview.txt", 'w') as file:
                pass

        print("--------------Task Overview Report--------------\n")
        with open('task_overview.txt', 'r') as file:
            print(file.read())
        print("------------------------------------------------\n")

        print("--------------User Overview Report--------------\n")
        with open('user_overview.txt', 'r') as file:
            print(file.read())
        print("------------------------------------------------\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
