# Main file for "TO DO." task manager app

from user import User
from tasks import *
from styling import *
from emoji import *

# ========== Global user objects =========
u = User()

# ========== User Welcome =========

def welcome_user(username, is_returning=False):
    if is_returning:
        message = f"\nHey {username}, welcome back!"
    else:
        message = f"\nHey {username}, welcome to TO DO. {emoji_wink_face} Let's get started!"
    print_success(message)

# ========== Task Input =========

def get_task_input():
    """Get task input from user"""
    title = input("\nWhat task do you want to add? ").strip()
    
    if not title:
        print_error("\nCome on, you gotta tell me what the task is!")
        return None
        
    if len(title) > 100:
        print_error("\nWhoah! That's a very long task. Let's keep it under 100 characters!")
        return None
        
    return title

# ========== Task Number Input =========
def get_task_number(task_list, action):
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

# ========== Show Motivational Quote =========
def show_motivational_quote(task_list):
    print_info(f"{emoji_motivation} Motivation incoming...")
    task_list.get_motivational_quote()

# ========== Task Menu =========
def task_menu(task_list):
    while True:
        print("\n" + "="*60)
        print(f"{emoji_welcome} {u.get_current_user()}'s TO DO.")
        print("="*60)
        print(f"1. {emoji_edit_task} Add a new task")
        print(f"2. {emoji_list_task} See all my tasks")
        print(f"3. {emoji_complete_task} Mark a task as done")
        print(f"4. {emoji_delete_task} Delete a task")
        print(f"5. {emoji_motivation} Get some motivation")
        print(f"6. {emoji_quit} Exit TO DO. app")
        print("="*60)

        choice = input("\nWhat would you like to do? (1-6): ")

        if choice == "1":
            print_info(f"\nYay! Let's add a new task!")
            title = get_task_input()
            if title:
                task = Task(title)
                task_list.add_task(task)
            
        elif choice == "2":
            print_info(f"\nHere are all your tasks:")
            task_list.display_tasks()
            
        elif choice == "3":
            print_info(f"\nLet's mark a task as done!")
            task_list.display_tasks()
            index = get_task_number(task_list, "mark complete")
            if index is not None:
                task_list.mark_complete(index)
                print_info("\nHere's your updated list:")
                task_list.display_tasks()
            
        elif choice == "4":
            print_info(f"\nWhat task do you want to delete? ")
            task_list.display_tasks()
            index = get_task_number(task_list, "delete")
            if index is not None:
                task_list.remove_task(index)
                print_info("\nHere's what's left:")
                task_list.display_tasks()
            
        elif choice == "5":
            show_motivational_quote(task_list)

        elif choice == "6":
            print_info(f"\nSee you later {u.get_current_user()}!")
            break
            
        else:
            print_error("\nNaughty, that's not a valid number.\nPlease, pick a number between 1 and 6.")

# ========== User Signup =========

def handle_signup():
    username = u.register_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username)
        task_menu(task_list)

# ========== User Login =========

def handle_login():
    username = u.login_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username, is_returning=True)
        task_menu(task_list)
        
# ========== Main Menu - login, signup or exit =========

def main_menu():
    while True:
        print("\n" + "="*50)
        print(f"\n1. {emoji_person} Create new account")
        print(f"2. {emoji_key} Log into existing account")
        print(f"3. {emoji_door} Exit")
        print("\n" + "="*50)

        choice = input("\nWhat would you like to do? (Enter a number 1-3): ")

        if choice == "1":
            handle_signup()
        elif choice == "2":
            handle_login()
        elif choice == "3":
            print_rainbow_text("TA TA!")
            print_info(f"\nThanks for stopping by!\n")
            break
        else:
            print_error(f"\nNaughty! Please pick a number!")

# ========= App Start =========
if __name__ == "__main__":
    terminal_black()
    clear_screen()
    show_app_title()
    main_menu()