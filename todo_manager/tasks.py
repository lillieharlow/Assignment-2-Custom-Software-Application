""" Task management for the TO DO app.
Features:
Task class: Represents a single task.
__init__: Sets title, completed status.
mark_complete(): Marks as complete.
mark_incomplete(): Marks as incomplete.
PriorityTask class: Inherits Task, adds priority.
TaskList class: Manages a user's tasks.
__init__: Sets up task list, loads tasks.
add_task(): Adds and saves task.
delete_task(): Deletes and saves task.
mark_complete(): Marks task as done.
get_tasks(): Returns task list.
display_tasks(): Shows tasks in table.
save_tasks(): Saves tasks to file.
load_tasks(): Loads tasks from file.
Helpers: Validates task numbers, shows errors, displays quotes.
->: type hinting for better code clarity."""

import json
import os
from emoji_library import complete, incomplete, interesting, high, medium, low
from styling import *

# ========= Task class =========
class Task:
    """A single task with title and completion status"""
    
    # ===== Create new task =====
    def __init__(self, title: str) -> None:
        """Set up a new task with a title"""
        self.title = title
        self.completed = False
    
    # ===== Task complete =====
    def mark_complete(self) -> None:
        """Mark this task as done"""
        self.completed = True
    
    # ===== Task incomplete =====
    def mark_incomplete(self) -> None:
        """Mark this task as not done"""
        self.completed = False

    def __str__(self) -> str:
        return self.title

# ===== Task priority =====
class PriorityTask(Task):
    """Inherits from Task and adds priority level to user tasks if they choose"""
    def __init__(self, title: str, priority: str) -> None:
        super().__init__(title) # Call parent constructor
        self.priority: str = priority  # "High", "Medium", "Low" 

    def __str__(self) -> str:  # Map priority to an emoji
        if self.priority == "High":
            prio_emoji = high
        elif self.priority == "Medium":
            prio_emoji = medium
        elif self.priority == "Low":
            prio_emoji = low
        else:
            prio_emoji = ""
        return f"{prio_emoji} {self.title}" # Adds priority emoji to task title

# ========= TaskList class =========
class TaskList:
    """Manages a user's tasks: add, delete, complete, display, and save/load tasks."""

    # ===== Setup task list =====
    def __init__(self, username: str) -> None:
        """Set up a new task list for this user"""
        self.username: str = username
        self.tasks: list[Task] = []
        self.filename: str = f"data/{username}_tasks.json"
        self.load_tasks()
    
    # ===== Add new task =====
    def add_task(self, task: Task) -> None:
        """Add a new task to the list"""
        self.tasks.append(task)
        self.save_tasks()
        print_success(f"\nNice cache! {task.title} was added to your tasks!")

    # ===== Delete task =====
    def delete_task(self, index: int) -> None:
        """Delete a task by its number"""
        if self.is_valid_task_number(index):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print_success(f"\nOrganisation is key! {removed_task.title} has been removed from your tasks!")
        else:
            self.show_invalid_number_error()
    
    # ===== Complete task =====
    def mark_complete(self, index: int) -> None:
        """Mark a task as done by its index number/task number"""
        if self.is_valid_task_number(index):
            self.tasks[index].mark_complete()
            self.save_tasks()
            print_success(f"\nGreat job! {self.tasks[index].title} is now complete!")
        else:
            self.show_invalid_number_error()

    # ===== Get task list =====
    def get_tasks(self) -> list[Task]:
        """Return the list of tasks"""
        return self.tasks
    
    # ===== Display tasks =====
    def display_tasks(self) -> None:
        """Show all tasks, task number and completion status in a nice table"""
        if not self.tasks:
            print_no_tasks()
            return
        
        table = create_task_table(self.username)
        
        for i, task in enumerate(self.tasks, 1):
            status = complete if task.completed else incomplete
            table.add_row(str(i), str(task), status)
        
        print_table(table)
    
    # ===== Save tasks to file =====
    def save_tasks(self) -> None:
        """Save all tasks to the user's file"""
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
            print_error(f"\nThis is awkward {interesting}. JaSON couldn't save tasks: {e}")

    # ===== Load tasks from file =====
    def load_tasks(self) -> None:
        """Load tasks from the user's file"""
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
            print_error("\nOh no! JaSON says... Let's start again!")
            self.tasks = []

    # ========== Helper methods =========
    
    # ===== Check valid task number =====
    def is_valid_task_number(self, index: int) -> bool:
        """Check if task number is valid"""
        return 0 <= index < len(self.tasks)
    
    # ===== Show error for invalid number =====
    def show_invalid_number_error(self) -> None:
        """Show message when user does not input valid number"""
        print_error(f"\nCheeky! That's not a valid number. Please pick a number from the list!")