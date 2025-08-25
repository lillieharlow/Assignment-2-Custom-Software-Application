""" Utility functions to avoid circular imports between main.py and tasks.py.
Features:
print_no_tasks(): Message when user wants to action a task but has no tasks listed
get_task_number(): Gets and validates task number input
retry_task(): Prompt user to 'retry' task action (mark complete/delete)
"""

from styling import print_info, clear_screen, print_error
from emoji_library import interesting, cross

# ========== print_no_tasks() =========
def print_no_tasks() -> None:
    """Message shown to user when there are no tasks listed"""
    print_info(f"{interesting} You don't have any tasks listed, let's add some!")
    
# ========== Task Number Input =========
def get_task_number(task_list, action):
    """Get task number from user for completing/deleting a task"""
    if not task_list.get_tasks():
        return None
    max_num = len(task_list.get_tasks())
    
    user_input = input(f"\nWhich task do you want to {action}? (1-{max_num}): ").strip()
    try:
        index = int(user_input) - 1
        if 0 <= index < max_num:
            return index
        else:
            print_error(f"\n{cross} Cheeky! That task number isn't there!")
    except ValueError:
        print_error(f"\n{interesting} That's not a number!")
    return None
    
# ========== Retry task actions (delete/complete) ==========
def retry_task(task_list, action, action_func, after_success_msg=None, after_success_func=None):
    """Helper to retry a task action (mark complete/delete) with a retry prompt."""
    while True:
        task_list.display_tasks()
        index = get_task_number(task_list, action)
        if index is not None:
            action_func(index)
            clear_screen()
            if after_success_msg:
                print_info(after_success_msg)
            if after_success_func:
                after_success_func()
            break
        else:
            again = input("\nTry again?\n\nPress 'y' to retry or enter anything else to return to the main menu: ").strip().lower()
            if again == "y":
                clear_screen()
            else:
                clear_screen()
                break