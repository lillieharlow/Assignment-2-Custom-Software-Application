# Tasks classes for TO DO. task manager

import json
from styling import print_error, print_success, print_info
from emoji import emoji_complete_task, emoji_incomplete_task

# Task class represents one single task
class Task:
    def __init__(self, title):
        """Create a new task."""
        self.title = title
        self.completed = False

    def mark_complete(self):
        """Mark this task as complete."""
        self.completed = True

# TaskList class manages many tasks for one user
class TaskList:
    def __init__(self, username):
        """Create a task list for a user."""
        self.username = username
        self.filename = f"{username}_tasks.json"
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):
        """Save tasks to file."""
        try:
            task_data = []
            for task in self.tasks:
                task_data.append({
                    "title": task.title,
                    "completed": task.completed
                })
            
            with open(self.filename, 'w') as file:
                json.dump(task_data, file)
        except:
            print_error("Could not save tasks!")

    def load_tasks(self):
        """Load tasks from file."""
        try:
            with open(self.filename, 'r') as file:
                task_data = json.load(file)
                
            for data in task_data:
                task = Task(data["title"])
                task.completed = data["completed"]
                self.tasks.append(task)
                
        except FileNotFoundError:
            pass  # No file yet, start with empty list
        except:
            print_error("Could not load tasks!")

    def add_task(self, task):
        """Add a new task."""
        self.tasks.append(task)
        self.save_tasks()
        print_success(f"Added task: {task.title}")
        print_info("Here's your updated task list:")
        self.display_tasks()  # Show tasks after adding

    def remove_task(self, index):
        """Remove a task by number."""
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            self.tasks.remove(task)
            self.save_tasks()
            print_success(f"Deleted: {task.title}")
        else:
            print_error("Invalid task number!")

    def mark_complete(self, index):
        """Mark a task as complete."""
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.mark_complete()
            self.save_tasks()
            print_success(f"Completed: {task.title}")
        else:
            print_error("Invalid task number!")

    def get_tasks(self):
        """Get all tasks."""
        return self.tasks

    def display_tasks(self):
        """Show all tasks in a simple list."""
        if not self.tasks:
            print_info("No tasks yet! Add some to get started.")
            return

        print_info(f"\nTasks for {self.username}:")
        for i, task in enumerate(self.tasks):
            status = emoji_complete_task if task.completed else emoji_incomplete_task
            print(f"{i + 1}. {status} {task.title}")