from app import add_user, create_and_add_workout, show_progress, show_weekly_report, Tracker

def main():
    tracker = Tracker()

    while True:
        print("1. Add user")
        print("2. Add workout")
        print("3. Show progress")
        print("4. Get weekly report")
        print("5. Quit")
        option = input("Enter an option: ")

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


