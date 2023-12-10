class User:
    def __init__(self, name, age, height, weight, goal=300):  # Default goal set to 300
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.goal = goal

class Exercise:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Workout:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def total_duration(self):
        return sum(exercise.duration for exercise in self.exercises)

class Tracker:
    def __init__(self):
        self.users = {}
        self.user_workouts = {}

    def add_user(self, user):
        if user.name in self.users:
            print(f"User {user.name} already exists.")
        else:
            self.users[user.name] = user
            self.user_workouts[user.name] = []

    def get_user(self, name):
        if name in self.users:
            return self.users[name]
        else:
            raise ValueError(f"User {name} does not exist.")

    def add_workout(self, name, workout):
        if name in self.users:
            self.user_workouts[name].append(workout)
        else:
            print(f"User {name} does not exist.")

    def get_user_progress(self, name):
        user_workouts = self.user_workouts.get(name, None)
        if user_workouts is not None:
            total_workouts = len(user_workouts)
            total_duration = sum(workout.total_duration() for workout in user_workouts)
            return f"{name} has completed {total_workouts} workouts for a total of {total_duration} minutes."
        else:
            return f"User {name} does not exist."

    def goal_report(self, name):
        try:
            user = self.get_user(name)
            user_workouts = self.user_workouts[name]
            total_duration = sum(workout.total_duration() for workout in user_workouts)
            remaining = max(user.goal - total_duration, 0)
            return f"{name} has worked out for {total_duration} minutes this week. {remaining} minutes left to reach the weekly goal."
        except ValueError as e:
            print(e)
