# Assignment-2-Custom-Software-Application

Software application.
File IO
User input
Meaningful output
Accessing data from external sources
Design a functioning app - terminal (CLI) in python.

Check List:

[] README.md file
    [] help or set up documentation - explain how to install any files & start the app
    [] hardware requirements
    [] features of the app
    [] dependencies required by the app
    [] list required files (third party)
        [] explaining the legal and ethical impacts of their license (+/-)
        [] security impact
        [] purpose
        [] not conflict with each other
[] uses 4+ third party libraries/packages
[] handle all errors - catch erros with error handling teechniques
[] use DRY principles across whole app
[] functions
    [] imported from third party libraries (extensive use)
    [] 6+ functions written by myself
[] 3+ classes
    [] uses inheritance and composition in at least two
[] variable scope & access delarations
[] loops and condiitonal statements
    [] for multiple paths
    [] nested structures that handle multiple contingencies
[] 2+ input and output
    [] retrieving user input and displaying output
    [] reading from files and writing to files
    [] req data from an API and displaying output
















Workflow
App Launch: User is prompted for login or signup.

Login: Credentials are checked. On success, user’s task list is loaded.

Main Menu: Add, edit, remove, mark, or view tasks; fetch productivity tips; save/load.

Session End: Data is persisted; user can log out











Building a Fun & Colourful Terminal To-Do List Manager
Beginner-Friendly Step-by-Step Plan

Project Summary
Create a terminal-based To-Do List Manager app that:

Allows every user to sign up, log in, and save their own tasks.

Lets users add, view, complete, and delete tasks—returning to their list any time.

Makes the user interface engaging with colors, ASCII art, and emojis.

Organizes code into separate modules for easy understanding and improvements.

Incorporates robust error handling and best coding practices.














Project Workflow


1. Setup & Planning
Decide where to store your project (a folder with subfolders: e.g., /todo_manager).

List the features you want: user login, task handling, colorful interface, persistent task-saving.

Note all third-party Python libraries you’ll use:

- rich (colorful CLI output)

- pyfiglet (ASCII art text)

- pandas (for flexible data storage, optional)

- requests (optional, for API features)

- tabulate (pretty tables, optional)






2. Install Libraries
Open your terminal and run:

bash
pip install rich pyfiglet pandas requests tabulate
Step-by-Step Coding Plan
Step 1: Structure Your Project
Organize your project like this:

proper python convention - haveing '/' goes in frotn of directory to indicate folder hierachy and directory structure.

/todo_manager
  /auth
    - __init__.py          # Makes it a proper Python package
    - user.py
    - auth_manager.py
  /tasks
    - __init__.py          # Makes it a proper Python package
    - task.py
    - tasklist.py
  /cli
    - __init__.py          # Makes it a proper Python package
    - menu.py
    - theme.py
  /data                    # Optional: separate folder for data files
    - users.json
    - tasks_*.json
  /tests                   # Optional: unit tests
    - test_auth.py
    - test_tasks.py
  - storage.py
  - manager.py
  - main.py
  - requirements.txt
  - README.md
  - .gitignore            # Ignore data files, __pycache__, etc.


  📁 todo_manager/               ← Main project folder
├── 📁 auth/                   ← Authentication subfolder
│   ├── __init__.py
│   ├── user.py
│   └── auth_manager.py
├── 📁 tasks/                  ← Tasks subfolder
│   ├── __init__.py
│   ├── task.py
│   └── tasklist.py
├── 📁 cli/                    ← CLI interface subfolder
│   ├── __init__.py
│   ├── menu.py
│   └── theme.py
├── 📁 data/                   ← Data storage subfolder
│   ├── users.json
│   └── tasks_*.json
├── storage.py                 ← Files in main folder
├── manager.py
├── main.py
└── README.md


Each file/module will focus on a different piece of functionality.

first - create main files needed

📁 todo_manager/
├── main.py                    ← Start here (entry point)
├── user.py                    ← Move your existing user.py here
├── tasks.py                   ← Move your existing tasks.py here
├── emoji.py                   ← Move your existing emoji.py here
└── requirements.txt           ← List your dependencies





Step 2: Implement User Authentication
Create a User class (auth/user.py) to handle user data.

Write an AuthManager (auth/auth_manager.py):

Allow new users to sign up (choose username & password).

Store hashed passwords securely (you can use simple hashing for now, like Python’s hashlib).

Validate credentials on login.

Handle errors (e.g., username taken, wrong password).










Step 3: Build the Task System
Make a Task class in tasks/task.py to represent each to-do item.

Optionally add a RecurringTask subclass to try inheritance.

Build a TaskList class (tasks/tasklist.py) that contains a user’s list and functions to add, mark, remove, and list tasks.

Step 4: Develop the CLI Interface
In cli/theme.py, create functions for:

Colorful welcome banners (using rich and pyfiglet)

Menu options (styled and decorated with emojis)

Color-coded task display tables

In cli/menu.py, code the flow for:

Login/signup prompts

Main menu (add/view/delete/complete tasks, log out)

Repeatedly show menus based on user actions

Step 5: Handle Data Storage
Use storage.py to read/write users’ task data (JSON or CSV format, using pandas or built-in json module).

Save each user's tasks to a separate file (e.g., tasks_{username}.json).

Step 6: Connect Components in the Manager
In manager.py, link authentication, task logic, and the CLI menus:

After login, load user’s tasks

Route menu actions to add/view/delete/complete

On logout or exit, save tasks

Step 7: Entry Point
In main.py, start the app by showing theme banner, prompting login/signup, then letting users manage tasks.

Use loops and conditionals to allow users to repeat actions, handle errors, and navigate.

Step 8: Polish & Test
Add try/except error handling everywhere user input or files are accessed.

Make sure colors, ASCII art, and emojis display as you’d like.

Test each feature as you add it—fix bugs as you find them.

Recommendations for Beginners
Go module by module; treat each as a mini-project.

Start simple (single user, plain CLI), then add color, fun, and modularity step by step.

Use plenty of comments and docstrings to explain what your code does.

Try using version control (git) to save your progress as you learn.

Example “First Login” Screen Concept
text
██████████ To-Do Champ! ██████████

Welcome back, [username]! 🌟  
Ready to conquer your day?

1. 📝  Add Task
2. 👀  View Tasks
3. ✅  Mark Complete
4. ❌  Delete Task
5. 🚪  Logout