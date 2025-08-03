# Task and TaskList classes for managing to-do items

import json
import os
import requests
from rich.table import Table
from rich.console import Console
from emoji import emoji_complete_task, emoji_incomplete_task, emoji_motivation
from styling import print_error, print_success, print_info

console = Console()

class Task:
    """A single task with title and completion status"""
    
    def __init__(self, title):
        self.title = title
        self.completed = False
    
    def mark_complete(self):
        """Mark this task as completed"""
        self.completed = True
    
    def mark_incomplete(self):
        """Mark this task as incomplete"""
        self.completed = False

class TaskList:
    """Manages a list of tasks for a specific user"""
    
    def __init__(self, username):
        self.username = username
        self.tasks = []
        self.filename = f"data/{username}_tasks.json"
        self.load_tasks()
    
    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append(task)
        self.save_tasks()
        print_success(f"Added '{task.title}' to your tasks!")
    
    def remove_task(self, index):
        """Remove a task by index"""
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print_success(f"Deleted '{removed_task.title}' from your tasks!")
        else:
            print_error("Invalid task number!")
    
    def mark_complete(self, index):
        """Mark a task as complete by index"""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            self.save_tasks()
            print_success(f"Great job! '{self.tasks[index].title}' is now complete!")
        else:
            print_error("Invalid task number!")
    
    def get_tasks(self):
        """Return the list of tasks"""
        return self.tasks
    
    def display_tasks(self):
        """Display all tasks in a beautiful table"""
        if not self.tasks:
            print_info("No tasks yet! Add some to get started.")
            return
        
        table = Table(title=f"[bold cyan]{self.username}'s Task Manager[/bold cyan]", show_header=True, header_style="bold magenta")
        table.add_column("#", style="cyan", width=4, justify="center")
        table.add_column("Status", style="magenta", width=8, justify="center")
        table.add_column("Task", style="green", min_width=20)
        
        for i, task in enumerate(self.tasks, 1):
            status = emoji_complete_task if task.completed else emoji_incomplete_task
            table.add_row(str(i), status, task.title)
        
        console.print()
        console.print(table)
        console.print()
    
    def save_tasks(self):
        """Save tasks to file"""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        
        task_data = []
        for task in self.tasks:
            task_data.append({
                "title": task.title,
                "completed": task.completed
            })
        
        try:
            with open(self.filename, 'w') as file:
                json.dump(task_data, file, indent=2)
        except Exception as e:
            print_error(f"Could not save tasks: {e}")
    
    def load_tasks(self):
        """Load tasks from file"""
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
            pass
        except Exception as e:
            print_error(f"Error loading tasks: {e}. Starting with empty list.")
    
    def get_motivational_quote(self):
        """Get a motivational quote from API"""
        try:
            print_info(f"Getting you some inspiration... {emoji_motivation}")
            response = requests.get("https://api.quotable.io/random?tags=motivational", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                quote = data.get('content', '')
                author = data.get('author', 'Unknown')
                
                console.print()
                console.print("=" * 60, style="cyan")
                console.print(f"{emoji_motivation} [bold cyan]Daily Motivation[/bold cyan] {emoji_motivation}")
                console.print("=" * 60, style="cyan")
                console.print()
                console.print(f"[italic bright_cyan]\"{quote}\"[/italic bright_cyan]")
                console.print(f"[bold yellow]— {author}[/bold yellow]")
                console.print()
                console.print("=" * 60, style="cyan")
                console.print()
            else:
                self._show_fallback_motivation()
                
        except requests.exceptions.RequestException:
            print_info("No internet connection available.")
            self._show_fallback_motivation()
        except Exception as e:
            print_error(f"Error getting quote: {e}")
            self._show_fallback_motivation()
    
    def _show_fallback_motivation(self):
        """Show offline motivational message"""
        fallback_quotes = [
            "You're doing amazing!",
            "Keep pushing forward!",
            "Every step counts!",
            "You've got this!",
            "Progress over perfection!",
            "Believe in yourself!",
            "Stay focused and keep going!",
            "You're unstoppable!"
        ]
        
        import random
        quote = random.choice(fallback_quotes)
        
        console.print()
        console.print("=" * 60, style="cyan")
        console.print(f"{emoji_motivation} [bold cyan]Offline Motivation[/bold cyan] {emoji_motivation}")
        console.print("=" * 60, style="cyan")
        console.print()
        console.print(f"[italic bright_green]{quote}[/italic bright_green]")
        console.print()
        console.print("=" * 60, style="cyan")
        console.print()