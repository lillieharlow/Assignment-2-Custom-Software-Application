# Main file for "TO DO." task manager app
# This is where everything starts and the main menu lives

import time
import sys
from user import User
from tasks import TaskList, Task
from styling import print_error, print_success, print_info, print_welcome, show_app_title
from emoji import emoji_add_task, emoji_list_task, emoji_complete_task, emoji_delete_task, emoji_quit

# Global user object - this handles login and signup
u = User()

def pause_and_continue():
    """Waits for user to press Enter - gives them time before menu re-appears"""
    try:
        input("\nPress enter to continue...")
    except KeyboardInterrupt:
        print_info("\nOkay, moving on...")

def welcome_user(username, is_returning=False):
    """Says hi to the user in a friendly way - makes them feel welcome!"""
    try:
        if is_returning:
            message = f"Hey {username}! Welcome back to your task manager!"
        else:
            message = f"Hi {username}! Welcome to your new task manager!"
        print_success(message)
        time.sleep(1)  # Just a little pause to let them see the message
    except:
        print_info("Welcome! Something went wrong but you're still awesome!")

def get_task_input():
    """Asks the user what task they want to add - keeps it simple!"""
    try:
        title = input("What task do you want to add? ").strip()
        
        if not title:
            print_error("Come on, you gotta tell me what the task is!")
            return None
            
        if len(title) > 100:
            print_error("Whoa! That's way too long. Keep it under 100 characters!")
            return None
            
        return title
        
    except KeyboardInterrupt:
        print_info("\nNever mind then!")
        return None

def get_task_number(task_list, action):
    """Asks which task number they want to work with - with some basic error checking"""
    if not task_list.get_tasks():
        print_error("You don't have any tasks yet! Add some first.")
        return None
    
    try:
        max_num = len(task_list.get_tasks())
        index = int(input(f"\nWhich task do you want to {action}? (1-{max_num}): ")) - 1
        
        if 0 <= index < max_num:
            return index
        else:
            print_error(f"Pick a number between 1 and {max_num}!")
            return None
            
    except ValueError:
        print_error("That's not a number! Try again with just numbers.")
        return None
    except KeyboardInterrupt:
        print_info("\nOkay, cancelling that...")
        return None

def show_motivational_quote(task_list):
    """Gets a nice motivational quote to keep the user going - because everyone needs encouragement!"""
    try:
        print_info("Getting you some motivation... 🌟")
        task_list.get_motivational_quote()
    except:
        print_info("💪 You're doing great! Keep up the awesome work!")

def task_menu(task_list):
    """This is the main task menu where users do all their task stuff"""
    while True:
        try:
            # Show the menu - nice and clean
            print("\n" + "="*60)
            print(f"{emoji_list_task} {u.get_current_user()}'s Task Manager")
            print("="*60)
            print(f"1. {emoji_add_task} Add a new task")
            print(f"2. {emoji_list_task} See all my tasks")
            print(f"3. {emoji_complete_task} Mark a task as done")
            print(f"4. {emoji_delete_task} Delete a task")
            print(f"5. 💪 Get some motivation")
            print(f"6. 📊 Show tasks differently")
            print(f"7. {emoji_quit} Exit the app")
            print("="*60)
            
            choice = input("\nWhat would you like to do? (1-7): ")
            
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
                # Alternative view
                print_info("\n📊 Here's a different way to see your tasks:")
                task_list.display_tasks_tabulate()
                pause_and_continue()
                
            elif choice == "7":
                # Exit
                print_info(f"See you later, {u.get_current_user()}! You're awesome! 👋")
                break
                
            else:
                print_error("Pick a number between 1 and 7, please!")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print_info("\nAlright, heading back to the main menu...")
            break
        except:
            print_error("Something weird happened, but let's keep going!")

def handle_signup():
    """Handles when someone wants to create a new account - pretty straightforward"""
    try:
        print_welcome("\n📝 Let's get you set up with a new account!")
        username = u.register_user()
        if username:
            task_list = TaskList(username)
            welcome_user(username)
            task_menu(task_list)
    except:
        print_error("Oops! Something went wrong with signup. Try again!")

def handle_login():
    """Handles when someone wants to log into their existing account"""
    try:
        print_welcome("\n🔑 Welcome back! Let's log you in.")
        username = u.login_user()
        if username:
            task_list = TaskList(username)
            welcome_user(username, is_returning=True)
            task_menu(task_list)
    except:
        print_error("Login didn't work. Double check your details!")

def main_menu():
    """This is the very first menu people see - keeps things simple"""
    while True:
        try:
            print("\n" + "="*50)
            print("🔐 Welcome to TO DO.")
            print("="*50)
            print("1. 📝 Create new account")
            print("2. 🔑 Log into existing account") 
            print("3. 🚪 Exit")
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
                
        except KeyboardInterrupt:
            print_info("\nThanks for trying TO DO! Goodbye! 👋")
            break
        except:
            print_error("Something went wrong, but we're still here!")

# ============ THIS IS WHERE THE MAGIC STARTS ============

if __name__ == "__main__":
    try:
        show_app_title()  # Show that cool rainbow title
        main_menu()       # Start the main menu
    except KeyboardInterrupt:
        print_info("\nThanks for using TO DO! Goodbye! 👋")
        sys.exit(0)
    except:
        print_error("Oh no! Something really bad happened. Sorry about that!")
        sys.exit(1)