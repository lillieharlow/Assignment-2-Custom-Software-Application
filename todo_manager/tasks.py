# Task management stuff - this is where the actual task magic happens!

import json
import os
from styling import print_error, print_success, print_info
from emoji import emoji_complete_task, emoji_incomplete_task
from rich.console import Console
from rich.table import Table
from tabulate import tabulate
import colorama
from colorama import Fore, Style
import requests
from base_classes import BaseTask, TaskCounter

# Set up the fancy console output
colorama.init()
console = Console()

class Task(BaseTask):  # INHERITANCE - Task inherits from BaseTask
    """A single task - simple and easy"""
    def __init__(self, title):
        BaseTask.__init__(self)      # Call parent class
        self.title = title           # What's the task about?
        self.completed = False       # Start as not done

    def mark_complete(self):
        """Mark this task as finished - feels good!"""
        self.completed = True

    def get_info(self):
        """Override parent method"""
        return f"I'm a task called: {self.title}"

class TaskList:
    """Manages all tasks for one user - this is where the real work happens"""
    def __init__(self, username):
        self.username = username
        self.counter = TaskCounter()     # COMPOSITION - TaskList contains TaskCounter
        
        # Create data folder and set filename
        os.makedirs("data", exist_ok=True)
        self.filename = f"data/{username}_tasks.json"  # Each user gets their own file
        
        self.tasks = []              # COMPOSITION - TaskList contains Task objects
        self.load_tasks()            # Load any existing tasks

    def save_tasks(self):
        """Save all tasks to the user's file - happens automatically"""
        try:
            # Convert all tasks to simple dictionaries
            task_data = []
            for task in self.tasks:
                task_data.append({
                    "title": task.title,
                    "completed": task.completed
                })
            
            # Write to file with nice formatting
            with open(self.filename, 'w') as file:
                json.dump(task_data, file, indent=2)
            
        except:
            print_error("Couldn't save your tasks! That's not good...")

    def load_tasks(self):
        """Load tasks from the user's file when they log in"""
        try:
            with open(self.filename, 'r') as file:
                task_data = json.load(file)
            
            # Clear the list and rebuild from file
            self.tasks = []
            for data in task_data:
                task = Task(data["title"])
                task.completed = data["completed"]
                self.tasks.append(task)
                    
            print_info(f"Loaded {len(self.tasks)} tasks for {self.username}")
            
        except FileNotFoundError:
            pass
        except:
            print_error("Something went wrong... let's just start with an empty list.")

    def add_task(self, task):
        """Add a new task to the list"""
        try:
            self.tasks.append(task)
            self.counter.add_one()  # Use composition object
            self.save_tasks()
            print_success(f"Added task: {task.title}")
            print_info("Here's your updated task list:")
            self.display_tasks()
        except:
            print_error("Couldn't add that task. Try again!")

    def remove_task(self, index):
        """Delete a task by its number"""
        try:
            if 0 <= index < len(self.tasks):
                task = self.tasks[index]
                self.tasks.remove(task)
                self.save_tasks()
                print_success(f"Deleted: {task.title}")
            else:
                print_error("That task number doesn't exist!")
        except:
            print_error("Something went wrong deleting that task.")

    def mark_complete(self, index):
        """Mark a task as done by its number"""
        try:
            if 0 <= index < len(self.tasks):
                task = self.tasks[index]
                task.mark_complete()
                self.save_tasks()
                print_success(f"Nice! You completed: {task.title}")
            else:
                print_error("That task number doesn't exist!")
        except:
            print_error("Couldn't mark that task as complete.")

    def get_tasks(self):
        """Just returns the list of tasks - simple getter"""
        return self.tasks

    def display_tasks(self):
        """Show all tasks in a nice table using Rich"""
        if not self.tasks:
            print_info("No tasks yet! Add some to get started.")
            return

        # Create a simple table
        table = Table(title=f"📋 {self.username}'s Tasks")
        table.add_column("#", width=3, style="bold blue")
        table.add_column("Status", width=8)
        table.add_column("Task", style="cyan")

        # Add each task to the table
        for i, task in enumerate(self.tasks):
            status = emoji_complete_task if task.completed else emoji_incomplete_task
            task_style = "dim" if task.completed else "white"
            
            table.add_row(
                str(i + 1), 
                status, 
                f"[{task_style}]{task.title}[/{task_style}]"
            )

        console.print(table)
        
        # Show simple progress
        completed = len([task for task in self.tasks if task.completed])
        total = len(self.tasks)
        console.print(f"📊 Progress: {completed}/{total} tasks done", style="bold cyan")

    def display_tasks_tabulate(self):
        """Alternative way to show tasks using the tabulate library"""
        if not self.tasks:
            print_info("No tasks to show!")
            return

        # Create simple table data
        headers = ["#", "Status", "Task"]
        table_data = []
        
        for i, task in enumerate(self.tasks):
            status = "✓" if task.completed else "○"
            table_data.append([i + 1, status, task.title])

        # Print with colorama colors
        table = tabulate(table_data, headers=headers, tablefmt="grid")
        print(f"\n{Fore.CYAN}{self.username}'s Tasks:{Style.RESET_ALL}")
        print(table)

    def get_motivational_quote(self):
        """Get an inspiring quote from the internet - because everyone needs motivation!"""
        try:
            print_info("🌐 Getting you some inspiration...")
            response = requests.get("https://api.quotable.io/random", timeout=5)
            
            if response.status_code == 200:
                quote_data = response.json()
                quote = quote_data.get('content', 'Stay motivated!')
                author = quote_data.get('author', 'Someone wise')
                
                # Pretty print with colors
                print(f"\n{Fore.YELLOW}💪 Here's some motivation for you:{Style.RESET_ALL}")
                print(f"{Fore.GREEN}'{quote}'{Style.RESET_ALL}")
                print(f"{Fore.BLUE}- {author}{Style.RESET_ALL}\n")
            else:
                print_info("💪 Stay focused and keep going! You've got this!")
                
        except:
            print_info("💪 Couldn't get a quote right now, but you're still awesome!")