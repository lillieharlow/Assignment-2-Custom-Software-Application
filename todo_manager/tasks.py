# tasks.py
# Task and TaskList classes for managing task items

import json
import os
from emoji_library import complete, incomplete, interesting, high, medium, low
from styling import *

# ========= Task class =========
class Task:
    """A single task with title and completion status"""
    
    # ===== Create new task =====
    def __init__(self, title):
        """Set up a new task with a title"""
        self.title = title
        self.completed = False
    
    # ===== Mark task complete =====
    def mark_complete(self):
        """Mark this task as done"""
        self.completed = True
    
    # ===== Mark task incomplete =====
    def mark_incomplete(self):
        """Mark this task as not done"""
        self.completed = False

    def __str__(self):
        return self.title

# ===== Task priority =====
class PriorityTask(Task):
    """Inherits from Task and adds priority level"""
    def __init__(self, title, priority):
        super().__init__(title)
        self.priority = priority  # "High", "Medium", "Low" 

    def __str__(self):
        # Map priority to emoji
        if self.priority == "High":
            prio_emoji = high
        elif self.priority == "Medium":
            prio_emoji = medium
        elif self.priority == "Low":
            prio_emoji = low
        else:
            prio_emoji = ""
        return f"{self.title} {prio_emoji}"

# ========= TaskList class =========
class TaskList:
    """Manages a list of tasks for a specific user"""

    # ===== Setup task list =====
    def __init__(self, username):
        """Set up a new task list for this user"""
        self.username = username
        self.tasks = []
        self.filename = f"data/{username}_tasks.json"
        self.load_tasks()
    
    # ===== Add new task =====
    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append(task)
        self.save_tasks()
        print_success(f"\nNice cache! {task.title} was added to your tasks!")

    # ===== Delete task =====
    def delete_task(self, index):
        """Remove a task by its number"""
        if self.is_valid_task_number(index):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print_success(f"\nOrganisation is key! {removed_task.title} has been removed from your tasks!")
        else:
            self.show_invalid_number_error()
    
    # ===== Complete task =====
    def mark_complete(self, index):
        """Mark a task as done by its number"""
        if self.is_valid_task_number(index):
            self.tasks[index].mark_complete()
            self.save_tasks()
            print_success(f"\nGreat job! {self.tasks[index].title} is now complete!")
        else:
            self.show_invalid_number_error()

    # ===== Get task list =====
    def get_tasks(self):
        """Return the list of tasks"""
        return self.tasks
    
    # ===== Display tasks =====
    def display_tasks(self):
        """Show all tasks in a nice table"""
        if not self.tasks:
            print_info(f"\nYou haven't added any tasks yet, let's get started!")
            return
        
        table = create_task_table(self.username)
        
        for i, task in enumerate(self.tasks, 1):
            status = complete if task.completed else incomplete
            table.add_row(str(i), task.title, status)
        
        print_table(table)
    
    # ===== Save tasks to file =====
    def save_tasks(self):
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
    def load_tasks(self):
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
        except FileNotFoundError:
            pass  # No file yet
        except Exception:
            print_error("\nOh no! JaSON says... Let's start again!")

    # ========== Helper methods =========
    
    # ===== Check valid task number =====
    def is_valid_task_number(self, index):
        """Check if task number is valid"""
        return 0 <= index < len(self.tasks)
    
    # ===== Show error for invalid number =====
    def show_invalid_number_error(self):
        """Show error message when user does not input valid number"""
        print_error(f"\nCheeky! That's not a valid number. Please pick a number from the list!")