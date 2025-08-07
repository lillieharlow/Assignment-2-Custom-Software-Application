# Assignment Check List:

- [ ] README.md file
    - [ ] help or set up documentation - explain how to install any files & start the app
    - [ ] hardware requirements
    - [ ] features of the app
    - [ ] dependencies required by the app
    - [ ] list required files (third party)
        - [ ] explaining the legal and ethical impacts of their license (+/-)
        - [ ] security impact
        - [ ] purpose
        - [ ] not conflict with each other
- [ ] uses 4+ third party libraries/packages
- [ ] handle all errors - catch errors with error handling techniques
- [ ] use DRY principles across whole app
- [ ] functions
    - [ ] imported from third party libraries (extensive use)
    - [ ] 6+ functions written by myself
- [ ] 3+ classes
    - [ ] uses inheritance and composition in at least two
- [ ] variable scope & access declarations
- [ ] loops and conditional statements
    - [ ] for multiple paths
    - [ ] nested structures that handle multiple contingencies
- [ ] 2+ input and output
    - [ ] retrieving user input and displaying output
    - [ ] reading from files and writing to files
<hr>

# main.py
### Flow:
1. App starts -> Show title
2. Main menu -> Choose signup/login/guest/exit
3. If signup/login successful -> Task menu
4. Task menu -> Add/view/complete/delete task
5. Finished -> Exit app

### Global setup
- u = User() handles all login/signup

### Functions
- Welcome message (different for new vs returning)
- If user is new, def to show "no tasks yet" message
- Task - input asks user what task they want to add
    - check input isn't empty or too long
- Store task as index/number to easily mark task as complete or delete
    - User input selects index/task
    - check valid input
    - str to int conversion

### Task Menu Function
- One of two main menus - Task Menu
    - Choice 1: Add
    - Choice 2: Show
    - Choice 3: Complete
    - Choice 4: Delete
    - Choice 5: Exit app

### User Management Functions
- sign up new user, login existing user, guest can use app but don't save data if they exit.

### Main Menu Function
- Main menu, first thing user sees on app
    - 1. Signup
    - 2. Login
    - 3. Guest
    - 4. Exit app

### App startup
- shows TO DO. app banner/title art (large, rainbow text)
- starts Main menu

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
- console object using Rich library for fancy terminal colors
- Imports pyfiglet for creating big ASCII art text
- Console is used by all the color functions to display styled messages

### Basic Color Functions
- Error message
    - red
    - impossible to miss - grabs attention immediately
    - used for validation errors, failed logins, etc.

- Success message
    - green
    - makes users feel good about completing actions
    - used for successful logins, saved tasks, confirmations

- Normal info message
    - yellow
    - eye-catching but friendly - not scary like errors
    - used for instructions, general messages, app descriptions

### ASCII Art Magic
- Rainbow banner
    - cycles through colors character by character for rainbow effect
    - adds proper padding above and below for clean presentation
    - calculates exact spacing to eliminate ugly white gaps
    - creates professional-looking title that makes app stand out
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
- three columns: #, status, task (different colors)

### Clear terminal
- os import clears terminal screen, neat and tidy display not lines and lines of input, output

<hr>

# tasks.py
Manages all task-related operations - creating, storing, displaying tasks
Two main classes: Task (individual task) and TaskList (collection of tasks)

### Task Class
- creates a new task with title
- task starts out as incomplete but changes to complete when done

### Priority Class
- inherits from Task class and shows tasks as high, medium, low priority or none

### TaskList Class Setup
- creates new task list for specific user
- sets up filename for saving user's tasks
- automatically loads existing tasks from file

### Task Management Functions

- Add task
    - adds new task to the list
    - saves updated list to file
    - shows success message

- Delete task
    - deletes task by number if valid
    - saves updated list
    - shows confirmation message or error

- Complete task
    - marks specific task as done by number
    - saves changes to file
    - celebrates completion with success message

- Get task
    - returns the current list of tasks
    - used by other functions to access tasks

- Display task
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

### Helper Functions
So there isn't duplicate code - call helper function instead

- Valid task number/index
    - checks if user entered valid task number
    - prevents crashes from invalid input

- If input is invalid/not in the number range or outside of 'y/n'
    - displays friendly error for wrong numbers
    - guides user to pick valid option