# finalCapstone

## Overview
The Task Manager is a Python program designed to help users manage tasks efficiently. Users can add new tasks, view all tasks, and view tasks assigned to them. The program reads data from `tasks.txt` and `users.txt` files, allowing users to interact with tasks based on their roles. The administrator has additional features such as registering new users and generating reports.

## User Access
- To access admin rights, use the following credentials:
  - Username: admin
  - Password: password
- Ensure you open the entire folder in VS Code for the program to locate text files correctly.

## Programmer Notes
1. To reflect changes in statistics, generate reports after modifying tasks.
2. If changes are made to any task, generate reports for updated statistics.

## Features
- **Add Task:**
  - Allows users to add a new task with details such as assigned user, title, description, and due date.

- **View All Tasks:**
  - Displays all tasks in a formatted manner, including title, assigned user, due date, and task description.

- **View My Tasks:**
  - Displays tasks assigned to the current user, allowing management and updates.

- **Admin Features:**
  - Register new users.
  - Generate reports on tasks and user statistics.

## Usage
1. **Run the Program:**
   - Execute the program in any Python interpreter.

2. **Login:**
   - Enter the provided admin credentials to access additional features.
   - Regular users can log in without admin rights.
<img width="318" alt="Screenshot 2024-01-19 at 17 57 17" src="https://github.com/loizoud94/finalCapstone/assets/152619396/0ffc0c16-9597-4279-8bd8-b76a54324da1">

3. **Choose Options:**
   - Add tasks, view all tasks, or view tasks assigned to you based on your role.
   - Admins can also register new users and generate reports.
<img width="598" alt="Screenshot 2024-01-19 at 17 59 36" src="https://github.com/loizoud94/finalCapstone/assets/152619396/a9de763c-7882-49c9-97fd-b6b0a03e7344">
<img width="746" alt="Screenshot 2024-01-19 at 18 00 36" src="https://github.com/loizoud94/finalCapstone/assets/152619396/d53596bc-e28b-4fe8-befc-3d22f7651d98">
<img width="379" alt="Screenshot 2024-01-19 at 18 01 57" src="https://github.com/loizoud94/finalCapstone/assets/152619396/91e9237d-cea4-47dc-83fd-f23ebf24cdf5">


4. **Generate Reports (Admin Only):**
   - Choose the "gr" option to generate reports, providing insights into task and user statistics.
<img width="960" alt="Screenshot 2024-01-19 at 18 02 39" src="https://github.com/loizoud94/finalCapstone/assets/152619396/5d0fd766-370e-435e-84e2-d55178a97e6f">

5. **Exit:**
   - Choose the "e" option to exit the program.

## Data Files
- `tasks.txt`: Stores task information, including user assignment, title, description, due date, and completion status.
- `users.txt`: Contains user credentials for authentication.

## Report Files
- `task_overview.txt`: Provides statistics on the number of tasks, completed tasks, uncompleted tasks, overdue tasks, and percentages.
- `user_overview.txt`: Offers insights into the total number of registered users, tasks generated, and user-specific task statistics.

## Contributing
If you have ideas for improvements or would like to contribute to the Task Manager, feel free to fork the repository and open a pull request.

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

Feel free to customize and enhance the program to better suit your needs. Happy task managing!
