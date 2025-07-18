# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    message = f"Reminder: '{task}' is a high priority task"
elif priority == "medium":
    message = f"Reminder: '{task}' is a medium priority task"
elif priority == "low":
    message = f"Reminder: '{task}' is a low priority task"
else:
    message = f"Reminder: '{task}' has an unrecognized priority"

if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

print(message)



































































