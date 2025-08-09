""" Utility functions for the TO DO app.
Created to avoid circular imports between main.py and tasks.py.
Features:
print_no_tasks(): Message when user wants to action a task but has no tasks listed"""

from styling import print_info
from emoji_library import interesting

# ========== print_no_tasks() =========
def print_no_tasks() -> None:
    """Message shown to user when there are no tasks listed"""
    print_info(f"{interesting} You don't have any tasks listed, let's add some!")