# Main file for "FOR YOU" task manager app

# Import libraries needed for functionality
import pyfiglet
import time
from user import User
from tasks import TaskList, Task
from styling import print_error, print_success, print_info, print_warning, print_welcome, print_menu
from emoji import *
from rich.console import Console
from termcolor import colored

# Create objects needed for the app
u = User()
console = Console()

def print_rainbow_text(text, font='ANSI Shadow'):
    """Prints the given text in ASCII art with a rainbow color effect"""
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    figlet_text = pyfiglet.figlet_format(text, font=font)
    
    lines = figlet_text.splitlines()
    for i, line in enumerate(lines):
        colored_line = ""
        for j, char in enumerate(line):
            color_index = (j + i) % len(colors)  # Cycle through colors
            colored_line += colored(char, colors[color_index])
        print(colored_line)

def pause_and_continue():
    """Add a pause so user can see the result before menu shows again"""
    input("\nPress Enter to continue...")

def welcome_user(username, is_returning=False):
    """Show welcome message for new or returning users"""
    message = f"Welcome {'back' if is_returning else 'to your task manager'}, {username}!"
    print_success(message)
    time.sleep(1)

def show_title():
    """Display the app title with rainbow styling"""
    print("\n" + "="*60)
    print_rainbow_text("FOR YOU!", font='ANSI Shadow')  # Rainbow colored title
    print("="*60 + "\n")
    print_info("Your personal to-do manager that cares about you!")

def get_task_input():
    """Get task title from user with validation"""
    title = input("Enter task title: ").strip()
    if not title:
        print_error("Task title cannot be empty!")
        return None
    return title

def get_task_number(task_list, action):
    """Get task number from user with validation"""
    if not task_list.get_tasks():
        return None
    
    try:
        index = int(input(f"\nEnter task number to {action}: ")) - 1
        return index
    except ValueError:
        print_error("Please enter a valid number!")
        return None

def task_menu(task_list):
    """Show the task management menu after user logs in"""
    while True:
        print("\n" + "="*50)
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
            print_welcome(f"\n{emoji_add_task} Add New Task")
            title = get_task_input()
            if title:
                task = Task(title)
                task_list.add_task(task)
            pause_and_continue()
            
        elif choice == "2":
            task_list.display_tasks()
            pause_and_continue()
            
        elif choice == "3":
            task_list.display_tasks()
            index = get_task_number(task_list, "complete")
            if index is not None:
                task_list.mark_complete(index)
            pause_and_continue()
            
        elif choice == "4":
            task_list.display_tasks()
            index = get_task_number(task_list, "delete")
            if index is not None:
                task_list.remove_task(index)
            pause_and_continue()
            
        elif choice == "5":
            u.logout_user()
            break
        else:
            print_error("Please enter a number between 1-5!")
            time.sleep(1)

def handle_signup():
    """Handle user registration"""
    username = u.register_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username)
        task_menu(task_list)

def handle_login():
    """Handle user login"""
    username = u.login_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username, is_returning=True)
        task_menu(task_list)

def handle_logout():
    """Handle user logout"""
    if u.is_logged_in():
        u.logout_user()
    else:
        print_warning("No user is currently logged in!")

def main_menu():
    """Main application loop with authentication menu"""
    while True:
        print_menu()
        choice = input("\nPlease enter your choice (1-4): ")

        if choice == "1":
            handle_signup()
        elif choice == "2":
            handle_login()
        elif choice == "3":
            handle_logout()
        elif choice == "4":
            print_info("Goodbye! Thanks for using FOR YOU!")
            break
        else:
            print_error("Ugh, this is awkward. Please enter a number between 1 - 4. Let's try again!")

# ============ MAIN PROGRAM STARTS HERE ============

if __name__ == "__main__":
    show_title()
    main_menu()