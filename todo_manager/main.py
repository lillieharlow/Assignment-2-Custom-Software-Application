import pyfiglet
from user import User
from styling import *

u = User()

print(pyfiglet.figlet_format("FOR YOU!"))
print("Your personal to-do manager that cares about you!")

# Initalize user login, sign up or logout
while True:
    print_menu()  # Use styled menu function
    choice = input("\nPlease enter your choice (1-4): ")

    if choice == "1":
        u.register_user()
    elif choice == "2":
        u.login_user()
    elif choice == "3":
        u.logout_user()
    elif choice == "4":
        print("Goodbye! Thanks for using FOR YOU!")
        break
    else:
        print("Ugh, this is awkward. Please enter a number between 1 - 4. Let's try again!")
