import tabulate

class Task:
    def __init__(self, title, priority="medium", completed=False):
        self.title = title
        self.priority = priority.lower()
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(d):
        return Task(d["title"], d["priority"], d["completed"])

class TaskList:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def get_tasks(self):
        return self.tasks