import pyfiglet
import time  # Add this import for pauses
from user import User
from tasks import TaskList, Task
from styling import print_error, print_success, print_info, print_warning, print_welcome, print_menu
from emoji import *

u = User()

def task_menu(task_list):
    """Show the task management menu after user logs in"""
    while True:
        # Display menu options (removed the welcome message)
        print("\n" + "="*50)  # Visual separator
        print(f"📋 Task Menu for {u.get_current_user()}")
        print("="*50)
        print(f"1. {emoji_add_task} Add Task")
        print(f"2. {emoji_list_task} View Tasks") 
        print(f"3. {emoji_complete_task} Mark Task Complete")
        print(f"4. {emoji_delete_task} Delete Task")
        print(f"5. {emoji_quit} Logout")
        print("="*50)
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            add_task(task_list)
            pause_and_continue()  # Add pause
        elif choice == "2":
            view_tasks(task_list)
            pause_and_continue()  # Add pause
        elif choice == "3":
            complete_task(task_list)
            pause_and_continue()  # Add pause
        elif choice == "4":
            delete_task(task_list)
            pause_and_continue()  # Add pause
        elif choice == "5":
            u.logout_user()
            break
        else:
            print_error("Please enter a number between 1-5!")
            time.sleep(1)  # Brief pause for errors

def pause_and_continue():
    """Add a pause so user can see the result before menu shows again"""
    input("\nPress Enter to continue...")

def add_task(task_list):
    """Let user add a new task to their list"""
    print_welcome(f"\n{emoji_add_task} Add New Task")
    title = input("Enter task title: ").strip()
    
    if not title:
        print_error("Task title cannot be empty!")
        return
    
    task = Task(title)
    task_list.add_task(task)

def view_tasks(task_list):
    """Show all the user's tasks in a nice table"""
    task_list.display_tasks()

def complete_task(task_list):
    """Let user mark a task as completed"""
    task_list.display_tasks()
    tasks = task_list.get_tasks()
    if not tasks:
        return
    
    try:
        index = int(input("\nEnter task number to complete: ")) - 1
        task_list.mark_complete(index)
    except ValueError:
        print_error("Please enter a valid number!")

def delete_task(task_list):
    """Let user delete a task from their list"""
    task_list.display_tasks()
    tasks = task_list.get_tasks()
    if not tasks:
        return
    
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        task_list.remove_task(index)
    except ValueError:
        print_error("Please enter a valid number!")

# ============ MAIN PROGRAM STARTS HERE ============

print(pyfiglet.figlet_format("FOR YOU!"))
print("Your personal to-do manager that cares about you!")

while True:
    print_menu()
    choice = input("\nPlease enter your choice (1-4): ")

    if choice == "1":
        username = u.register_user()
        if username:
            task_list = TaskList(username)
            print_success(f"Welcome to your task manager, {username}!")
            time.sleep(1)  # Brief welcome pause
            task_menu(task_list)
            
    elif choice == "2":
        username = u.login_user()
        if username:
            task_list = TaskList(username)
            print_success(f"Welcome back, {username}!")
            time.sleep(1)  # Brief welcome pause
            task_menu(task_list)
            
    elif choice == "3":
        if u.is_logged_in():
            u.logout_user()
        else:
            print_warning("No user is currently logged in!")
            
    elif choice == "4":
        print_info("Goodbye! Thanks for using FOR YOU!")
        break
        
    else:
        print_error("Ugh, this is awkward. Please enter a number between 1 - 4. Let's try again!")