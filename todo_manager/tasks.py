# Tasks classes for "FOR YOU" to-do manager app

import tabulate  # For making tables pretty
from emoji import *  # Import emoji icons for better UX
from styling import print_error, print_success, print_info, print_warning, print_welcome  # Rich colors

# Task class represents one single task
class Task:
    def __init__(self, title, completed=False):
        """Create a new task."""
        self.title = title
        self.completed = completed

    def mark_complete(self):
        """Mark task as complete."""
        self.completed = True

    def to_dict(self):
        """Convert task to dictionary for saving."""
        return {
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(d):
        """Create task from dictionary."""
        return Task(d["title"], d["completed"])

# TaskList class manages many tasks
class TaskList:
    def __init__(self, username):
        """Create a task list for a user."""
        self.username = username
        self.tasks = []

    def add_task(self, task):
        """Add a task to the list."""
        self.tasks.append(task)
        print_success(f"Task '{task.title}' added successfully!")

    def remove_task(self, index):
        """Remove a task by index."""
        if 0 <= index < len(self.tasks):
            task_title = self.tasks[index].title
            del self.tasks[index]
            print_success(f"Task '{task_title}' deleted!")
        else:
            print_error("Invalid task number!")

    def mark_complete(self, index):
        """Mark a task as complete."""
        if 0 <= index < len(self.tasks):
            task_title = self.tasks[index].title
            self.tasks[index].mark_complete()
            print_success(f"Task '{task_title}' marked as complete!")
        else:
            print_error("Invalid task number!")

    def get_tasks(self):
        """Get all tasks."""
        return self.tasks

    def display_tasks(self):
        """Show all tasks in a beautiful table."""
        if not self.tasks:
            print_warning("No tasks yet! Add some to get started.")
            return

        # Prepare data for table
        table_data = []
        for i, task in enumerate(self.tasks):
            checkbox = "[✓]" if task.completed else "[ ]"
            table_data.append([
                i + 1,          # Task number
                task.title,     # Task description  
                checkbox        # Done checkbox (on the right)
            ])

        # Create table with headers
        headers = ["#", "Task", "Done"]
        table = tabulate.tabulate(
            table_data,
            headers=headers,
            tablefmt="grid"
        )

        print_info("Your Tasks:")
        print(table)