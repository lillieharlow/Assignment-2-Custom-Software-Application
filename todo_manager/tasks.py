""" Task management functions
Features:
Task class: Represents a single task
__init__: Create new task, sets title and completed status
mark_complete(): Marks task as complete
mark_incomplete(): Marks task as incomplete
PriorityTask class: Inherits Task, can add priority to task title
TaskList class: Manages a user's tasks
__init__: Sets up task list, load, save tasks
add_task(): Adds and saves task
delete_task(): Deletes and saves task
mark_complete(): Marks task as done
get_tasks(): Returns task list
display_tasks(): Shows tasks in table
save_tasks(): Saves tasks to file
load_tasks(): Loads tasks from file
Helpers: Validates task numbers, shows errors
->: type hinting for better clarity"""

import json
import os
from emoji_library import complete, incomplete, interesting, high, medium, low
from styling import *
from utils import print_no_tasks

# ========= Task class =========
class Task:
    
    # ===== Create new task =====
    def __init__(self, title: str) -> None:
        self.title = title
        self.completed = False
    
    # ===== Task complete =====
    def mark_complete(self) -> None:
        self.completed = True
    
    # ===== Task incomplete =====
    def mark_incomplete(self) -> None:
        self.completed = False

    def __str__(self) -> str:
        return self.title

    # ===== task UPPERCASE (TDD 1 feature) =====
    def title_upper(self) -> str:
        return self.title.upper()
    
    # ===== Check if task is high priority (TDD 2 feature) =====
    def is_high_priority(self) -> bool:
        return False

# ========= Task priority =========
class PriorityTask(Task):
    """Inherits from Task and adds priority level to users tasks if they choose"""
    def __init__(self, title: str, priority: str) -> None:
        super().__init__(title) # Call parent Task constructor
        self.priority: str = priority  # "High", "Medium", "Low" 

    def __str__(self) -> str:  # Priority level mapped as emoji
        if self.priority == "High":
            prio_emoji = high
        elif self.priority == "Medium":
            prio_emoji = medium
        elif self.priority == "Low":
            prio_emoji = low
        else:
            prio_emoji = ""
        return f"{prio_emoji} {self.title}" # Adds priority emoji to task title
        
    def is_high_priority(self) -> bool: # TDD 2 - Return True if this PriorityTask is High.
        return self.priority == "High"

# ========= TaskList class =========
class TaskList:
    """Manages a user's tasks: add, delete, complete, display, and save/load tasks."""

    # ===== Setup task list =====
    def __init__(self, username: str) -> None:
        """Create new task list for this user, load, save task list"""
        self.username: str = username
        self.tasks: list[Task] = []
        self.filename: str = f"data/{username}_tasks.json"
        self.load_tasks()
    
    # ===== Add new task =====
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        self.save_tasks()
        clear_screen()
        print_success(f"Nice cache! {task.title} was added to your tasks!")

    # ===== Delete task by index =====
    def delete_task(self, index: int) -> None:
        if self.is_valid_task_number(index):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
        else:
            self.show_invalid_number_error()
            return None
    
    # ===== Complete task by index =====
    def mark_complete(self, index: int) -> None:
        if self.is_valid_task_number(index):
            self.tasks[index].mark_complete()
            self.save_tasks()
            print_success(f"Great job! {self.tasks[index].title} is now complete!")
        else:
            self.show_invalid_number_error()

    # ===== Get/return task list to user =====
    def get_tasks(self) -> list[Task]:
        return self.tasks
    
    # ===== Display tasks =====
    def display_tasks(self) -> None:
        """Show all tasks, task number, completion status, uppercase title, and high priority flag in Rich table"""
        if not self.tasks:
            print_no_tasks()
            return

        table = create_task_table(self.username)

        # TDD testing implementation code - makes high priority tasks bold, red and uppercase
        for i, task in enumerate(self.tasks, 1):
            status = complete if task.completed else incomplete
            # High priority PriorityTask: uppercase and red, keep original emoji
            if isinstance(task, PriorityTask) and task.is_high_priority():
                base = task.__str__()
                prio_emoji = base.replace(task.title, '').strip()
                display_title = f"{prio_emoji} {task.title_upper()}"
                display_title = red_text(display_title)
            elif isinstance(task, PriorityTask):
                display_title = task.__str__()
            else:
                display_title = str(task)
            table.add_row(str(i), display_title, status)

        print_table(table)
    
    # ===== Save tasks to users file =====
    def save_tasks(self) -> None:
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        task_data = []
        for task in self.tasks:
            task_info = {
                "title": task.title,
                "completed": task.completed,
                "type": task.__class__.__name__
            }
            if isinstance(task, PriorityTask):
                task_info["priority"] = task.priority
            task_data.append(task_info)
        try:
            with open(self.filename, 'w') as file:
                json.dump(task_data, file, indent=2)
        except Exception as e:
            print_error(f"\nThis is awkward {interesting}. JaSON couldn't save tasks because {e}")

    # ===== Load tasks from users file =====
    def load_tasks(self) -> None:
        try:
            with open(self.filename, 'r') as file:
                task_data = json.load(file)
            self.tasks = []
            for data in task_data:
                if data.get("type") == "PriorityTask":
                    task = PriorityTask(data["title"], data.get("priority", "Medium"))
                else:
                    task = Task(data["title"])
                task.completed = data["completed"]
                self.tasks.append(task)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []  # No tasks file yet or file is empty/corrupted - start new list
        except Exception:
            print_error("\nOh no! JaSON says... I don't like that one, start again!")
            self.tasks = []

    # ========== Helper methods =========
    
    # ===== Check if task number is valid =====
    def is_valid_task_number(self, index: int) -> bool:
        return 0 <= index < len(self.tasks)
    
    # ===== Show message when user does not input valid number =====
    def show_invalid_number_error(self) -> None:
        print_error(f"\nCheeky! That's not a valid number. Please pick a number from the list!")