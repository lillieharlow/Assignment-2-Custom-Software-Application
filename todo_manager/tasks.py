# Task and TaskList classes for managing to-do items

import json
import os
import requests
import random
from emoji import emoji_complete_task, emoji_incomplete_task, emoji_motivation, emoji_delete_task, emoji_not_found
from styling import print_error, print_success, print_info, create_task_table, print_table

# ========= Task class =========
class Task:
    """A single task with title and completion status"""
    
    def __init__(self, title):
        """Set up a new task with a title"""
        self.title = title
        self.completed = False
    
    def mark_complete(self):
        """Mark this task as done"""
        self.completed = True
    
    def mark_incomplete(self):
        """Mark this task as not done"""
        self.completed = False

# ========= TaskList class =========
class TaskList:
    """Manages a list of tasks for a specific user"""

    def __init__(self, username):
        """Set up a new task list for this user"""
        self.username = username
        self.tasks = []
        self.filename = f"data/{username}_tasks.json"
        self.load_tasks()
    
    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append(task)
        self.save_tasks()
        print_success(f"NICE CACHE! '{task.title}' was added to your tasks!")
    
    def remove_task(self, index):
        """Remove a task by its number"""
        if self._is_valid_index(index):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print_success(f"{emoji_delete_task} A clean space is an organised space! '{removed_task.title}' has been removed from your tasks!")
        else:
            self._show_invalid_number_error()
    
    def mark_complete(self, index):
        """Mark a task as done by its number"""
        if self._is_valid_index(index):
            self.tasks[index].mark_complete()
            self.save_tasks()
            print_success(f"GREAT JOB! '{self.tasks[index].title}' is now complete! {emoji_complete_task}")
        else:
            self._show_invalid_number_error()

    def get_tasks(self):
        """Return the list of tasks"""
        return self.tasks
    
    def display_tasks(self):
        """Show all tasks in a nice table"""
        if not self.tasks:
            print_info(f"You haven't added any tasks yet - let's get started! {emoji_motivation}")
            return
        
        table = create_task_table(self.username)
        
        for i, task in enumerate(self.tasks, 1):
            status = emoji_complete_task if task.completed else emoji_incomplete_task
            table.add_row(str(i), status, task.title)
        
        print_table(table)
    
    def save_tasks(self):
        """Save all tasks to the user's file"""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        
        task_data = [{"title": task.title, "completed": task.completed} for task in self.tasks]
        
        try:
            with open(self.filename, 'w') as file:
                json.dump(task_data, file, indent=2)
        except Exception as e:
            print_error(f"Could not save tasks: {e}")
    
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
                
            if self.tasks:
                print_info(f"Loaded {len(self.tasks)} tasks for {self.username}")
                
        except FileNotFoundError:
            pass  # No file yet - that's fine
        except Exception as e:
            print_error(f"Error loading tasks: {e}. Starting with empty list.")
    
    def get_motivational_quote(self):
        """Get an inspiring quote to motivate the user"""
        try:
            print_info(f"Getting you some inspiration... {emoji_motivation}")
            response = requests.get("https://api.quotable.io/random?tags=motivational", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                quote = data.get('content', '')
                author = data.get('author', 'Unknown')
                self._display_quote(quote, author, "Daily Motivation")
                return
                
        except (requests.exceptions.RequestException, Exception) as e:
            print_info("No internet connection available." if isinstance(e, requests.exceptions.RequestException) else f"Error getting quote: {e}")
        
        # Only one call to fallback
        self._show_fallback_motivation()
    
    # ========== Helper methods =========
    def _is_valid_index(self, index):
        """Check if task number is valid"""
        return 0 <= index < len(self.tasks)
    
    def _show_invalid_number_error(self):
        """Show error message for invalid task numbers"""
        print_error(f"Naughty! {emoji_not_found} That's not a valid number. Please pick a number from the list!")
    
    def _display_quote(self, quote, author, title):
        """Display a quote with consistent formatting"""
        print_info(f"\n{emoji_motivation} {title} {emoji_motivation}")
        print_info(f'"{quote}"')
        print_info(f"— {author}")
    
    def _show_fallback_motivation(self):
        """Show offline motivational message"""
        quotes = [
            "You're doing amazing! Keep pushing forward!",
            "Every step counts! You've got this!",
            "Progress over perfection! Believe in yourself!",
            "Stay focused and keep going! You're unstoppable!"
        ]
        
        quote = random.choice(quotes)
        self._display_quote(quote, "Your Task Manager", "Offline Motivation")