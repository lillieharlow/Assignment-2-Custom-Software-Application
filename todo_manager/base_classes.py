# Simple base classes for inheritance - keeps it easy!

class BaseTask:
    """Simple base class that all tasks inherit from"""
    def __init__(self):
        self.created = True  # Just a simple property
    
    def get_info(self):
        """Every task can tell us about itself"""
        return "I'm a task!"

class TaskCounter:
    """Simple helper class for counting tasks"""
    def __init__(self):
        self.count = 0
    
    def add_one(self):
        """Count up by one"""
        self.count += 1
    
    def get_count(self):
        """Tell us how many we have"""
        return self.count