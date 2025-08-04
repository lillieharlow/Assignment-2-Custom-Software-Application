# tasks.py
# Task and TaskList classes for managing task items

import json
import os
import requests
import random
from emoji import emoji_complete_task, emoji_incomplete_task, emoji_motivation, emoji_delete_task, emoji_not_found
from styling import print_error, print_success, print_info, create_task_table, print_table
from dateutil import parser
from datetime import datetime, timedelta

# ========= Task class =========
class Task:
    """A single task with title and completion status"""
    
    # ===== Create new task =====
    def __init__(self, title, due_date=None):
        """Set up a new task with a title"""
        self.title = title
        self.completed = False
        self.due_date = parser.parse(due_date) if due_date else None
        self.created_at = datetime.now()
    
    # ===== Mark task complete =====
    def mark_complete(self):
        """Mark this task as done"""
        self.completed = True
    
    # ===== Mark task incomplete =====
    def mark_incomplete(self):
        """Mark this task as not done"""
        self.completed = False

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
        print_success(f"\nNICE CATCH! '{task.title}' was added to your tasks!")

    # ===== Remove task =====
    def remove_task(self, index):
        """Remove a task by its number"""
        if self.is_valid_task_number(index):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print_success(f"\n{emoji_delete_task} A clean space is an organised space! '{removed_task.title}' has been removed from your tasks!")
        else:
            self.show_invalid_number_error()
    
    # ===== Complete task =====
    def mark_complete(self, index):
        """Mark a task as done by its number"""
        if self.is_valid_task_number(index):
            self.tasks[index].mark_complete()
            self.save_tasks()
            print_success(f"\nGREAT JOB! '{self.tasks[index].title}' is now complete! {emoji_complete_task}")
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
            print_info(f"\nYou haven't added any tasks yet - let's get started! {emoji_motivation}")
            return
        
        table = create_task_table(self.username)
        
        for i, task in enumerate(self.tasks, 1):
            status = emoji_complete_task if task.completed else emoji_incomplete_task
            table.add_row(str(i), task.title, status)
        
        print_table(table)
    
    # ===== Save tasks to file =====
    def save_tasks(self):
        """Save all tasks to the user's file"""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        
        # Create list of task data
        task_data = []
        for task in self.tasks:
            task_info = {"title": task.title, "completed": task.completed}
            task_data.append(task_info)
        
        try:
            with open(self.filename, 'w') as file:
                json.dump(task_data, file, indent=2)
        except Exception as e:
            print_error(f"\nCould not save tasks: {e}")
    
    # ===== Load tasks from file =====
    def load_tasks(self):
        """Load tasks from the user's file"""
        try:
            with open(self.filename, 'r') as file:
                task_data = json.load(file)
            
            self.tasks = []
            for data in task_data:
                task = Task(data["title"])
                task.completed = data["completed"]
                self.tasks.append(task)
                
        except FileNotFoundError:
            pass  # No file yet - that's okay
        except Exception:
            print_error("\nError loading tasks. Starting with empty list.")
    
    # ===== Get motivational quote =====
    def get_motivational_quote(self):
        """Get an inspiring quote to motivate the user"""
        print_info(f"\nGetting you some inspiration... {emoji_motivation}")
        
        try:
            response = requests.get("https://api.quotable.io/random?tags=motivational", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                quote = data.get('content', '')
                author = data.get('author', 'Unknown')
                self.display_quote(quote, author, "Daily Motivation")
                return
                
        except:
            # Silently fall back to offline quotes
            pass
        
        # Show backup motivation (user doesn't know it's offline)
        self.show_backup_motivation()
    
    # ========== Helper methods =========
    
    # ===== Check valid task number =====
    def is_valid_task_number(self, index):
        """Check if task number is valid"""
        return 0 <= index < len(self.tasks)
    
    # ===== Show error for invalid number =====
    def show_invalid_number_error(self):
        """Show error message for invalid task numbers"""
        print_error(f"\nNaughty! {emoji_not_found} That's not a valid number. Please pick a number from the list!")
    
    # ===== Display quote with formatting =====
    def display_quote(self, quote, author, title):
        """Display a quote with consistent formatting"""
        print_info(f"\n{emoji_motivation} {title} {emoji_motivation}")
        print_info(f"\n'{quote}'")
        print_info(f"\n— {author}")
    
    # ===== Show backup motivation =====
    def show_backup_motivation(self):
        """Show backup motivational message"""
        quotes = [
            "You're doing amazing!",
            "Keep pushing forward!",
            "Every step counts!",
            "You've got this!",
            "Progress over perfection!",
            "Believe in yourself!",
            "Stay focused and keep going!",
            "You're unstoppable!"
        ]
        
        quote = random.choice(quotes)
        self.display_quote(quote, "Your Task Manager", "Inspiration")