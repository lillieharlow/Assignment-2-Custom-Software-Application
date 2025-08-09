""" Main application file for the TO DO. app
Features:
Global objects: u for user management
welcome_user(): Prints welcome message (new/returning)
get_task_input(): Gets and validates task input, returns Task/PriorityTask
get_task_number(): Gets and validates task number input
task_menu(): Main task menu (add, view, complete, delete, exit app)
handle_signup(): User signup flow
handle_login(): User login flow
handle_guest(): Guest user flow (tasks not saved)
main_menu(): Main menu (signup, login, guest, exit app)
App start: Shows rainbow art, title and runs main_menu()
->: type hinting for better clarity"""

from user import User, GuestUser
from tasks import Task, PriorityTask, TaskList
from utils import print_no_tasks
from styling import * # Import all styling functions
from emoji_library import person, key, door, smile, add, list, complete, delete, quit, interesting, cross, high, medium, low

# ========== Global user objects =========
u = User()

# ========== User Welcome =========
def welcome_user(username: str, is_returning: bool = False) -> None:
    """Welcome message for user/guest"""
    if username == "Guest":
        return  # Don't print the welcome message for guest
    if is_returning:
        message = f"Hey {username}, welcome back!"
    else:
        message = f"Hey {username}, welcome to TO DO. {smile} Let's get started!"
    print_success(message)

# ========== Task Input =========
def get_task_input():
    """Get task input from user"""
    title = input("\nWhat task do you want to add? ").strip()
    if not title:
        print_error("\nCome on, you gotta tell me what the task is!")
        return None
    if len(title) > 100:
        print_error("\nWhoah! That's a very long task. Let's keep it short and snappy!\n(less than 100 characters please)")
        return None
        
    while True:  # Loop until user enters 'y' or 'n' for priority task input
        is_priority = input("\nIs this task important? (y/n): ").strip().lower()
        if is_priority == "y":
            while True:
                print(f"\nHow important?")
                print(f"\n1. {high} High")
                print(f"2. {medium} Medium")
                print(f"3. {low} Low")
                priority_choice = input("\nPlease enter a number (1-3): ").strip()
                if priority_choice == "1":
                    priority = "High"
                    clear_screen()
                    break
                elif priority_choice == "2":
                    priority = "Medium"
                    clear_screen()
                    break
                elif priority_choice == "3":
                    priority = "Low"
                    clear_screen()
                    break
                else:
                    print_error(f"\nPlease enter 1, 2, or 3.")
            return PriorityTask(title, priority)
        elif is_priority == "n":
            return Task(title)
        else:
            print_error(f"\n {interesting} Please type 'y' or 'n'.")

# ========== Task Number Input =========
def get_task_number(task_list, action):
    """Get task number from user for completing/deleting a task"""
    if not task_list.get_tasks():
        return None
    max_num = len(task_list.get_tasks())
    
    while True:
        user_input = input(f"\nWhich task do you want to {action}? (1-{max_num}): ").strip()
        try:
            index = int(user_input) - 1
            if 0 <= index < max_num:
                return index
            else:
                print_error(f"\n{cross} Cheeky! That task number isn't there!")
        except ValueError:
            print_error(f"\n{interesting} That's not a number!")
        again = input(f"\nTry again? Press 'y' to retry or anything else to return to menu: ").strip().lower()
        if again != "y":
            clear_screen
            return None
    
# ========== Task Menu =========
def task_menu(task_list: TaskList, username: str) -> None:
    """Main task menu for adding, seeing, completing, deleting tasks"""
    while True:
        print("\n" + "="*50)
        print(f"{smile} {username}'s TO DO.")
        print("="*50)
        print(f"1. {add} Add a new task")
        print(f"2. {list} See all my tasks")
        print(f"3. {complete} Mark a task as done")
        print(f"4. {delete} Delete a task")
        print(f"5. {quit} Exit TO DO. app")
        print("="*50)

        choice = input("\nWhat would you like to do? (1-5): ")

        if choice == "1": # Add a new task
            clear_screen()
            print_info(f"{smile} Yay! Let's add a new task!")
            while True:
                task = get_task_input() 
                if task:
                    task_list.add_task(task) # add task object directly
                    break  # Only break if a valid task was added

        elif choice == "2": # See all tasks
            clear_screen()
            if task_list.get_tasks():
                task_list.display_tasks()
            else:
                print_no_tasks()

        elif choice == "3": # Mark a task as done/complete
            clear_screen()
            if task_list.get_tasks():
                print_info(f"{complete} Let's mark a task as done!\n")
                task_list.display_tasks()
                index = get_task_number(task_list, "mark complete")
                if index is not None:
                    task_list.mark_complete(index)
                    clear_screen()
                    print_info("\nHere's your updated list:")
                    task_list.display_tasks()
            else:
                print_no_tasks()
            
        elif choice == "4": # Delete a task
            clear_screen()
            if not task_list.get_tasks():
                task_list.display_tasks()
            else:
                print_info(f"{delete} What task do you want to delete?\n")
                task_list.display_tasks()
                while True:
                    index = get_task_number(task_list, "delete")
                    if index is not None:
                        clear_screen()
                        task_list.delete_task(index)
                        if task_list.get_tasks():
                            print_info("\nHere's what's left:")
                            task_list.display_tasks()
                        else:
                            print_no_tasks() # no tasks left
                        break
                    else:
                        again = input(f"Try again?\nPress 'y' to retry or enter anything else to return to menu: ").strip().lower()
                        if again != "y":
                            break

        elif choice == "5": # Exit the app
            print_rainbow_text("GOODBYE!")
            print_info(f"\nTHANKS FOR USING TO DO. - SEE YOU NEXT TIME!")
            return True  # Exit loop to end task and main menu
        
        else:
            clear_screen()
            print_error(f"{cross} Cheeky, that's not a valid number!")

# ========== User Signup =========
def handle_signup():
    username = u.register_user()
    if username:
        clear_screen() # clear screen after signup
        task_list = TaskList(username)
        welcome_user(username)
        return task_menu(task_list, username)
    return False

# ========== User Login =========
def handle_login():
    username = u.login_user()
    if username:
        clear_screen() # clear screen after login
        task_list = TaskList(username)
        welcome_user(username, is_returning=True)
        return task_menu(task_list, username)
    return False

# ========== Guest user / doesn't save tasks =========
def handle_guest() -> None:
    guest = GuestUser()
    username = "Guest"
    clear_screen()
    print_info("Welcome to TODO. Please note: your tasks will NOT be saved after you exit.")
    task_list = TaskList(username)
    task_list.save_tasks = lambda: None # Disable saving
    task_list.load_tasks = lambda: None # Disable loading
    welcome_user(username)
    return task_menu(task_list, username)

        
# ========== Main Menu =========
def main_menu() -> None:
    """Main menu for user to create account, login, guest or exit"""
    while True:
        print("\n" + "="*50)
        print(f"\n1. {person} Create new account")
        print(f"2. {key} Log into existing account")
        print(f"3. {smile} Guest user")
        print(f"4. {door} Exit")
        print("\n" + "="*50)

        choice = input("\nWhat would you like to do? (Enter a number 1-4): ")

        if choice == "1": # Create new account
            should_exit = handle_signup()
            if should_exit:
                break  # Breaks under the 'if' statements exit both main and task menus
        elif choice == "2": # Log into existing account
            should_exit = handle_login()
            if should_exit:
                break
        elif choice == "3": # Guest user
            should_exit = handle_guest()
            if should_exit:
                break
        elif choice == "4": # Exit the app
            print_rainbow_text("GOODBYE!")
            print_info(f"\nTHANKS FOR USING TO DO.\n")
            break
        else:
            clear_screen()
            print_error(f"{cross} Naughty! Please pick a number!")

# ========= App Starting point / Shows title, runs main menu. =========
if __name__ == "__main__":
    clear_screen()
    print_info("A TASK MANAGEMENT APP THAT HELPS YOU STAY ON TRACK")
    main_menu()