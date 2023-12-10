def show_menu():
    print("1. Add User")
    print("2. Create and Add Workout")
    print("3. Show Progress")
    print("4. Get Weekly Report")
    print("q. Quit")

def get_user_choice():
    return input("Enter your choice: ")

def get_user_input(prompt):
    return input(prompt).strip()  # Strip leading and trailing spaces from the input

def show_message(message):
    print(message)


