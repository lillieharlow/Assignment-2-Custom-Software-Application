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

- pause_and_continue()
    -wait for user to press enter before showing menu again
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