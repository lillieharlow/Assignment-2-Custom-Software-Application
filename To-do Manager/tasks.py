'''Functions for task inputs / outputs
Here you will find the functions for all task input / output'''

import emoji
tasks = []

def add_task():
  task = input("Please enter your new task: ")
  tasks.append(task)
  print(f"TASK: '{task}' WAS added to your list.")


def list_tasks():
  if not tasks:
    print("Oh-oh this is awkward... your task list is empty! Let's add a task!")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"Task #{index}. {task}")


def delete_task():
  listTasks()
  try:
    taskToDelete = int(input("Enter the # to delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task #{taskToDelete} was not found.")
  except:
    print("Invalid input.")