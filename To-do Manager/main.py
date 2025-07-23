# import necessary modules

import tasks
import emoji
import sys
import os

if __name__ == "__main__":
  ### Create a loop to run the app
  print("Welcome to FOR YOU  :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      deleteTask()
    elif (choice == "3"):
      listTasks()
    elif (choice == "4"):
      break
    else:
      print("Invalid input. Please try again.")

  print("Goodbye 👋👋")