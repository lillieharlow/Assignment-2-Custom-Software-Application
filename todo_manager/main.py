# Main file for "TO DO." task manager app
# This is where everything starts and the main menu lives

import time
import sys
from user import User
from tasks import TaskList, Task
from styling import print_error, print_success, print_info, print_welcome, show_app_title
from emoji import emoji_add_task, emoji_list_task, emoji_complete_task, emoji_delete_task, emoji_quit, emoji_motivation, emoji_door, emoji_key, emoji_lock, emoji_person

# Global user object - this handles login and signup
u = User()

def pause_and_continue():
    """Waits for user to press Enter - gives them time before menu re-appears"""
    input("\nPress enter to continue...")

def welcome_user(username, is_returning=False):
    """Says hi to the user in a friendly way - makes them feel welcome!"""
    if is_returning:
        message = f"Hey {username}! Welcome back to your task manager!"
    else:
        message = f"Hi {username}! Welcome to your new task manager!"
    print_success(message)
    time.sleep(1)

def get_task_input():
    """Asks the user what task they want to add - keeps it simple!"""
    title = input("What task do you want to add? ").strip()
    
    if not title:
        print_error("Come on, you gotta tell me what the task is!")
        return None
        
    if len(title) > 100:
        print_error("Whoa! That's way too long. Keep it under 100 characters!")
        return None
        
    return title

def get_task_number(task_list, action):
    """Asks which task number they want to work with - with some basic error checking"""
    if not task_list.get_tasks():
        print_error("You don't have any tasks yet! Add some first.")
        return None
    
    max_num = len(task_list.get_tasks())
    try:
        index = int(input(f"\nWhich task do you want to {action}? (1-{max_num}): ")) - 1
        
        if 0 <= index < max_num:
            return index
        else:
            print_error(f"Pick a number between 1 and {max_num}!")
            return None
    except ValueError:
        print_error("That's not a number! Try again with just numbers.")
        return None

def show_motivational_quote(task_list):
    """Gets a nice motivational quote to keep the user going - because everyone needs encouragement!"""
    print_info(f"Getting you some motivation... {emoji_motivation}")
    task_list.get_motivational_quote()

def task_menu(task_list):
    """This is the main task menu where users do all their task stuff"""
    while True:
        # Show the menu - nice and clean
        print("\n" + "="*60)
        print(f"{emoji_list_task} {u.get_current_user()}'s Task Manager")
        print("="*60)
        print(f"1. {emoji_add_task} Add a new task")
        print(f"2. {emoji_list_task} See all my tasks")
        print(f"3. {emoji_complete_task} Mark a task as done")
        print(f"4. {emoji_delete_task} Delete a task")
        print(f"5. {emoji_motivation} Get some motivation")
        print(f"6. {emoji_quit} Exit the app")
        print("="*60)

        choice = input("\nWhat would you like to do? (1-6): ")

        if choice == "1":
            # Add a new task
            print_welcome(f"\n{emoji_add_task} Let's add a new task!")
            title = get_task_input()
            if title:
                task = Task(title)
                task_list.add_task(task)
            pause_and_continue()
            
        elif choice == "2":
            # Show all tasks
            print_info(f"\n{emoji_list_task} Here are all your tasks:")
            task_list.display_tasks()
            pause_and_continue()
            
        elif choice == "3":
            # Mark task as complete
            print_info(f"\n{emoji_complete_task} Let's mark a task as done!")
            task_list.display_tasks()
            index = get_task_number(task_list, "mark complete")
            if index is not None:
                task_list.mark_complete(index)
                print_info("\nHere's your updated list:")
                task_list.display_tasks()
            pause_and_continue()
            
        elif choice == "4":
            # Delete a task
            print_info(f"\n{emoji_delete_task} Which task do you want to delete?")
            task_list.display_tasks()
            index = get_task_number(task_list, "delete")
            if index is not None:
                task_list.remove_task(index)
                print_info("\nHere's what's left:")
                task_list.display_tasks()
            pause_and_continue()
            
        elif choice == "5":
            # Show motivation
            show_motivational_quote(task_list)
            pause_and_continue()

        elif choice == "6":
            # Exit
            print_info(f"See you later {u.get_current_user()}! {emoji_quit}")
            break
            
        else:
            print_error("Please pick a number between 1 and 6:")
            time.sleep(1)

def handle_signup():
    """Handles when someone wants to create a new account - pretty straightforward"""
    username = u.register_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username)
        task_menu(task_list)

def handle_login():
    """Handles when someone wants to log into their existing account"""
    print_welcome(f"\n{emoji_key} Welcome back!")
    username = u.login_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username, is_returning=True)
        task_menu(task_list)

def main_menu():
    """First menu user sees - login, signup, or exit"""
    while True:
        print("\n" + "="*50)
        print(f"{emoji_lock} Welcome to TO DO.")
        print("="*50)
        print(f"1. {emoji_person} Create new account")
        print(f"2. {emoji_key} Log into existing account") 
        print(f"3. {emoji_door} Exit")
        print("="*50)
        
        choice = input("\nWhat would you like to do? (1-3): ")

        if choice == "1":
            handle_signup()
        elif choice == "2":
            handle_login()
        elif choice == "3":
            print_info("Thanks for checking out TO DO! Come back soon! 😊")
            break
        else:
            print_error("Just pick 1, 2, or 3 please!")

# ============ THIS IS WHERE THE MAGIC STARTS ============

if __name__ == "__main__":
    show_app_title()
    main_menu()