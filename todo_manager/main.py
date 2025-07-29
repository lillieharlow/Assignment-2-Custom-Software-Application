import pyfiglet
from user import User
from tasks import TaskList, Task
from styling import print_error, print_success, print_info, print_warning, print_welcome, print_menu
from emoji import *

u = User()

def task_menu(task_list):
    """Display task management menu for logged-in users."""
    while True:
        print_info(f"\n{emoji_list_task} Task Manager - Welcome {u.get_current_user()}!")
        print("\nWhat would you like to do?")
        print(f"1. {emoji_add_task} Add Task")
        print(f"2. {emoji_list_task} View Tasks") 
        print(f"3. {emoji_complete_task} Mark Task Complete")
        print(f"4. {emoji_delete_task} Delete Task")
        print(f"5. {emoji_quit} Logout")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            complete_task(task_list)
        elif choice == "4":
            delete_task(task_list)
        elif choice == "5":
            u.logout_user()
            break
        else:
            print_error("Please enter a number between 1-5!")

def add_task(task_list):
    """Add a new task."""
    print_welcome(f"\n{emoji_add_task} Add New Task")
    title = input("Enter task title: ").strip()
    if not title:
        print_error("Task title cannot be empty!")
        return
    
    print("\nPriority levels:")
    print("1. Low")
    print("2. Medium") 
    print("3. High")
    
    priority_choice = input("Choose priority (1-3, default=2): ").strip()
    priority_map = {"1": "low", "2": "medium", "3": "high"}
    priority = priority_map.get(priority_choice, "medium")
    
    task = Task(title, priority)
    task_list.add_task(task)
    print_success(f"{emoji_complete_task} Task '{title}' added with {priority} priority!")

def view_tasks(task_list):
    """Display all tasks."""
    tasks = task_list.get_tasks()
    if not tasks:
        print_warning(f"{emoji_list_task} No tasks yet! Add some tasks to get started.")
        return
    
    print_info(f"\n{emoji_list_task} Your Tasks:")
    for i, task in enumerate(tasks):
        status = emoji_complete_task if task.completed else emoji_edit_task
        priority_emoji = {"high": emoji_priority_high, "medium": emoji_edit_task, "low": emoji_list_task}
        emoji_priority = priority_emoji.get(task.priority, emoji_edit_task)
        
        print(f"{i+1}. {status} {emoji_priority} {task.title} ({task.priority})")

def complete_task(task_list):
    """Mark a task as complete."""
    view_tasks(task_list)
    tasks = task_list.get_tasks()
    if not tasks:
        return
    
    try:
        index = int(input("\nEnter task number to complete: ")) - 1
        if 0 <= index < len(tasks):
            if not tasks[index].completed:
                task_list.mark_complete(index)
                print_success(f"{emoji_complete_task} Task '{tasks[index].title}' marked as complete!")
            else:
                print_warning("This task is already completed!")
        else:
            print_error("Invalid task number!")
    except ValueError:
        print_error("Please enter a valid number!")

def delete_task(task_list):
    """Delete a task."""
    view_tasks(task_list)
    tasks = task_list.get_tasks()
    if not tasks:
        return
    
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            task_title = tasks[index].title
            task_list.remove_task(index)
            print_success(f"{emoji_delete_task} Task '{task_title}' deleted!")
        else:
            print_error("Invalid task number!")
    except ValueError:
        print_error("Please enter a valid number!")

# Main program
print(pyfiglet.figlet_format("FOR YOU!"))
print("Your personal to-do manager that cares about you!")

# Main authentication loop
while True:
    print_menu()  # Your existing menu function
    choice = input("\nPlease enter your choice (1-4): ")

    if choice == "1":
        username = u.register_user()
        if username:  # If registration successful
            task_list = TaskList(username)
            task_menu(task_list)
            
    elif choice == "2":
        username = u.login_user()
        if username:  # If login successful
            task_list = TaskList(username)
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