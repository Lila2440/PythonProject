from fitness_tracker import User, Exercise, Workout, Tracker
import ui

def initialize_tracker():
    return Tracker()

def add_user(tracker):
    name = ui.get_user_input("Enter user's name: ")
    age = ui.get_user_input("Enter user's age: ")
    height = ui.get_user_input("Enter user's height: ")
    weight = ui.get_user_input("Enter user's weight: ")
    goal = int(ui.get_user_input("Enter user's weekly workout goal in minutes: "))  # Convert goal to integer
    tracker.add_user(User(name, age, height, weight, goal))

def create_and_add_workout(tracker):
    user_name = ui.get_user_input("Enter user's name: ")
    user = tracker.get_user(user_name)
    if user:
        workout = Workout()
        while True:
            exercise_name = ui.get_user_input("Enter an exercise name (or 'q' to quit): ")
            if exercise_name == 'q':
                break
            exercise_duration = int(ui.get_user_input("Enter the exercise duration in minutes: "))
            workout.add_exercise(Exercise(exercise_name, exercise_duration))
        tracker.add_workout(user_name, workout)
    else:
        ui.show_message("User not found.")

def show_progress(tracker):
    user_name = ui.get_user_input("Enter user's name: ")
    user_progress = tracker.get_user_progress(user_name)
    if user_progress:
        ui.show_message(user_progress)
    else:
        ui.show_message("User not found.")

def show_weekly_report(tracker):
    user_name = ui.get_user_input("Enter user's name: ")
    report = tracker.goal_report(user_name)
    if report:
        ui.show_message(report)
    else:
        ui.show_message("User not found.")

def main():
    tracker = initialize_tracker()

    while True:
        print("1. Add user")
        print("2. Add workout")
        print("3. Show progress")
        print("4. Get weekly report")
        print("5. Quit")
        option = ui.get_user_input("Enter an option: ")

        if option == '1':
            add_user(tracker)
        elif option == '2':
            create_and_add_workout(tracker)
        elif option == '3':
            show_progress(tracker)
        elif option == '4':
            show_weekly_report(tracker)
        elif option == '5':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

