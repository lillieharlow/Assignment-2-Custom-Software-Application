# Main file for "TO DO." task manager app

import time
from user import User
from tasks import TaskList, Task
from styling import print_error, print_success, print_info, print_welcome, show_app_title
from emoji import emoji_add_task, emoji_list_task, emoji_complete_task, emoji_delete_task, emoji_quit, emoji_motivation, emoji_door, emoji_key, emoji_lock, emoji_person
from rich.console import Console

# Global user object
u = User()
console = Console()

def pause_and_continue():
    """Wait for user to press Enter"""
    input("\nPress enter to continue...")

def welcome_user(username, is_returning=False):
    """Welcome message for users"""
    if is_returning:
        message = f"Hey {username}! Welcome back to your task manager!"
    else:
        message = f"Hi {username}! Welcome to your new task manager!"
    print_success(message)
    time.sleep(1)

def get_task_input():
    """Get task input from user"""
    title = input("What task do you want to add? ").strip()
    
    if not title:
        print_error("Come on, you gotta tell me what the task is!")
        return None
        
    if len(title) > 100:
        print_error("Whoa! That's way too long. Keep it under 100 characters!")
        return None
        
    return title

def get_task_number(task_list, action):
    """Get task number from user with error checking"""
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
    """Show motivational quote"""
    print_info(f"Getting you some motivation... {emoji_motivation}")
    task_list.get_motivational_quote()

def task_menu(task_list):
    """Main task menu"""
    while True:
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
            print_welcome(f"\n{emoji_add_task} Let's add a new task!")
            title = get_task_input()
            if title:
                task = Task(title)
                task_list.add_task(task)
            pause_and_continue()
            
        elif choice == "2":
            print_info(f"\n{emoji_list_task} Here are all your tasks:")
            task_list.display_tasks()
            pause_and_continue()
            
        elif choice == "3":
            print_info(f"\n{emoji_complete_task} Let's mark a task as done!")
            task_list.display_tasks()
            index = get_task_number(task_list, "mark complete")
            if index is not None:
                task_list.mark_complete(index)
                print_info("\nHere's your updated list:")
                task_list.display_tasks()
            pause_and_continue()
            
        elif choice == "4":
            print_info(f"\n{emoji_delete_task} Which task do you want to delete?")
            task_list.display_tasks()
            index = get_task_number(task_list, "delete")
            if index is not None:
                task_list.remove_task(index)
                print_info("\nHere's what's left:")
                task_list.display_tasks()
            pause_and_continue()
            
        elif choice == "5":
            show_motivational_quote(task_list)
            pause_and_continue()

        elif choice == "6":
            print_info(f"See you later {u.get_current_user()}! {emoji_quit}")
            break
            
        else:
            print_error("Please pick a number between 1 and 6!")
            time.sleep(1)

def handle_signup():
    """Handle user signup"""
    username = u.register_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username)
        task_menu(task_list)

def handle_login():
    """Handle user login"""
    print_welcome(f"\n{emoji_key} Welcome back!")
    username = u.login_user()
    if username:
        task_list = TaskList(username)
        welcome_user(username, is_returning=True)
        task_menu(task_list)

def main_menu():
    """Main menu - login, signup, or exit"""
    while True:
        console.print("\n" + "="*50, style="cyan")
        console.print(f"[bold cyan]{emoji_lock} Welcome to TO DO.[/bold cyan]", justify="center")
        console.print("="*50, style="cyan")
        console.print()
        console.print(f"[bold green]1.[/bold green] {emoji_person} [cyan]Create new account[/cyan]")
        console.print(f"[bold green]2.[/bold green] {emoji_key} [cyan]Log into existing account[/cyan]") 
        console.print(f"[bold green]3.[/bold green] {emoji_door} [cyan]Exit[/cyan]")
        console.print()
        console.print("="*50, style="cyan")
        
        choice = input("\nWhat would you like to do? (1-3): ")

        if choice == "1":
            handle_signup()
        elif choice == "2":
            handle_login()
        elif choice == "3":
            print_info("Thanks for checking out TO DO! Come back soon!")
            break
        else:
            print_error("Just pick 1, 2, or 3 please!")

if __name__ == "__main__":
    show_app_title()
    main_menu()