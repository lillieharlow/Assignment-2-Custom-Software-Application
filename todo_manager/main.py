# Main file for "TO DO." task manager app

# Import only what we need in main.py
import time
from user import User
from tasks import TaskList, Task
from styling import print_error, print_success, print_info, print_warning, print_welcome, show_app_title
from emoji import emoji_add_task, emoji_list_task, emoji_complete_task, emoji_delete_task, emoji_quit

# Create user object
u = User()

def pause_and_continue():
    """Add a pause so user can see the result before menu shows again"""
    input("\nPress Enter to continue...")

def welcome_user(username, is_returning=False):
    """Show welcome message for new or returning users"""
    message = f"Welcome {'back' if is_returning else 'to your task manager'}, {username}!"
    print_success(message)
    time.sleep(1)

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
        print(f"{emoji_list_task} Task Menu for {u.get_current_user()}")
        print("="*50)
        print(f"1. {emoji_add_task} Add Task")
        print(f"2. {emoji_list_task} View Tasks")
        print(f"3. {emoji_complete_task} Mark Task Complete")
        print(f"4. {emoji_delete_task} Delete Task")
        print(f"5. {emoji_quit} Exit App")
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
                task_list.display_tasks()
            pause_and_continue()
            
        elif choice == "4":
            task_list.display_tasks()
            index = get_task_number(task_list, "delete")
            if index is not None:
                task_list.remove_task(index)
            pause_and_continue()
            
        elif choice == "5":
            print_info(f"Goodbye, {u.get_current_user()}! Thanks for using TO DO.")
            exit()
        else:
            print_error("Please enter a number between 1-5!")
            time.sleep(1)

def handle_signup():
    """Handle user registration and start task menu"""
    username = u.register_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username)
        task_menu(task_list)

def handle_login():
    """Handle user login and start task menu"""
    username = u.login_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username, is_returning=True)
        task_menu(task_list)

def main_menu():
    """Main application loop with authentication menu"""
    while True:
        print("\n" + "="*50)
        print("🔐 Welcome to TO DO.")
        print("="*50)
        print("1. 📝 Sign Up")
        print("2. 🔑 Log In") 
        print("3. 🚪 Exit")
        print("="*50)
        
        choice = input("\nPlease enter your choice (1-3): ")

        if choice == "1":
            handle_signup()
        elif choice == "2":
            handle_login()
        elif choice == "3":
            print_info("Goodbye! Thanks for using TO DO.")
            break
        else:
            print_error("Please enter a number between 1-3!")

# ============ MAIN PROGRAM STARTS HERE ============

if __name__ == "__main__":
    show_app_title()
    main_menu()