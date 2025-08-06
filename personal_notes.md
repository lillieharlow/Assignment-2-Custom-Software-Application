Assignment Check List:

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

# main.py

1. App starts → Show title
2. Main menu → Choose signup/login/exit
3. If signup/login successful → Task menu
4. Task menu → Add/view/complete/delete tasks or get motivation
5. When done → Back to main menu or exit

### Global setup
- u handles all login/signup
- console creates a console for pretty text
- both used throughout the app that's why they are global objects

### Functions

- welcome_user()
    - welcome message (different for new vs returning)
- get_task_input()
    - asks you to type a task
    - checks it's not blank/empty
    - checks length
    - returns task or None if invalid
- get_task_number()
    - asks which task number you want/what you want to do
    - converts answer to number
    - checks validity
    - returns task index or none if invalid

### Task Menu Function

- task_menu()
    - Choice 1: Add a new task to your list
    - Choice 2: Show all your current tasks
    - Choice 3: Mark a task as completed
    - Choice 4: Delete a task from your list
    - Choice 5: Get a motivational quote
    - Choice 6: Exit back to main menu

### User Management Functions

- handle_signup()
    - create new user account

- handle_login()
    - login existing user account

### Main Menu Function

- the first thing user sees, asks input to signup, login, exit app

### App startup

- shows TO DO. title in rainbow
- starts main_menu()

<hr>

# user.py

Blueprint for handling all user accounts - class User
Manages sign up, log in and who is using the app

- __init__()
    - sets up where the user accounts will be stored - in a file called users.json
    - remembers who is currently logged in

### File management
- load_users()
    - opens file where all usernames and apsswords are stored
    - if there isn't a matching file then creates new one, empty list
    - catch issues by providing an empty list as default so app doesn't crash

- save_users()
    - writes usernames and passwords
    - ensures folder exists first - creates if needed
    - shows success and error message with an error asking input again

### Creating new accounts
- Step 1:
    - ask for a username
    - check it's not empty/blank
    - check nobody else already has that name
    - if taken, prompt to pick different username
    - keep asking until valid username is picked

- Step 2:
    - ask for password, len > 5 char
    - ask user to re-type
    - check both inputs match
    - keeps asking user until matched

- Step 3:
    - Saves new username and password to file
    - logs in automatically
    - returns your username

### Logging into existing account

Gives you three tires, stops an infite loop/unlimited for security reasons

after three tries is reached, new message says too many attempts and takes user back to main menu

### Extra functionality

- get_current_user()
    - tells who is currently logged into the app
    - saying goodbye when someone exits

<hr>

# styling.py
Makes everything look pretty! Handles all the colors, fancy text.
Creates an amazing first impression with rainbow title
- Keeps users engaged with colorful, friendly interface
- Shows attention to detail and professional presentation
- Makes the command line app feel modern and polished

### Setup
- Creates a console object using Rich library for fancy terminal colors
- Imports pyfiglet for creating big ASCII art text
- Console is used by all the color functions to display styled messages

### Basic Color Functions

- print_error()
    - red
    - impossible to miss - grabs attention immediately
    - used for validation errors, failed logins, etc.

- print_success()
    - green
    - makes users feel good about completing actions
    - used for successful logins, saved tasks, confirmations

- print_info()
    - pink
    - eye-catching but friendly - not scary like errors
    - used for instructions, general messages, app descriptions

- print_warning()
    - yellow
    - gets noticed but not as alarming as errors
    - used for important notices that aren't quite errors

- print_welcome()
    - blue
    - calm and inviting feeling
    - used for greeting messages and friendly notifications

### ASCII Art Magic

- print_rainbow_text()
    - takes any text and turns it into HUGE rainbow-colored ASCII art
    - uses 6 carefully chosen colors that look amazing together
    - cycles through colors character by character for rainbow effect
    - adds proper padding above and below for clean presentation
    - calculates exact spacing to eliminate ugly white gaps
    - creates professional-looking title that makes app stand out

- show_app_title()
    - displays the complete app startup screen
    - combines rainbow ASCII art with borders and tagline
    - shows "TO DO." in massive rainbow letters
    - adds description line explaining what the app does
    - first thing users see - sets the tone for whole experience

### Table styling
- Makes task lists look professional vs boring text
- Colors help users scan tasks quickly  
- Shows completed (✅) vs incomplete (⬜) clearly
- Clean, readable format that's easy to understand

- create_task_table()
    - creates styled table for tasks
    - sets user's name in cyan as title
    - three columns: #, status, task (different colors)
    - returns empty table ready for data

- print_table()
    - displays table with proper spacing
    - uses Rich formatting for clean output
    - keeps all tables looking consistent

<hr>


# tasks.py

Manages all task-related operations - creating, storing, displaying tasks
Two main classes: Task (individual task) and TaskList (collection of tasks)

### Task Class

- __init__()
    - creates a new task with title
    - sets completed status to False by default

- mark_complete()
    - changes task status to completed (True)

- mark_incomplete()
    - changes task status back to not completed (False)

### TaskList Class Setup

- __init__()
    - creates new task list for specific user
    - sets up filename for saving user's tasks
    - automatically loads existing tasks from file

### Task Management Functions

- add_task()
    - adds new task to the list
    - saves updated list to file
    - shows success message

- remove_task()
    - deletes task by number if valid
    - saves updated list
    - shows confirmation message or error

- mark_complete()
    - marks specific task as done by number
    - saves changes to file
    - celebrates completion with success message

- get_tasks()
    - returns the current list of tasks
    - used by other functions to access tasks

- display_tasks()
    - shows all tasks in colorful table format
    - displays message if no tasks exist yet
    - uses create_task_table() for styling

### File Operations

- save_tasks()
    - writes all tasks to user's JSON file
    - creates data folder if needed
    - handles file errors gracefully

- load_tasks()
    - reads tasks from user's file on startup
    - creates Task objects from saved data
    - handles missing files (new users)

### Motivation System

- get_motivational_quote()
    - tries to fetch inspiring quote from internet API
    - displays quote with author attribution
    - falls back to offline quotes if no internet

- show_backup_motivation()
    - provides offline motivational quotes
    - randomly selects from built-in collection
    - user doesn't know it's offline mode

### Helper Functions

- is_valid_task_number()
    - checks if user entered valid task number
    - prevents crashes from invalid input

- show_invalid_number_error()
    - displays friendly error for wrong numbers
    - guides user to pick valid option

- display_quote()
    - formats and displays quotes consistently
    - adds emoji decorations and proper spacing
    - used for both online and offline quotes