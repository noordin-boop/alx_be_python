# daily_reminder.py

# Prompt the user for a task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Create a base reminder message
reminder_message = f"'{task}' is a {priority} priority task."

# Use Match Case to handle different priorities
match priority:
    case "high":
        reminder_message += " This requires immediate attention today!"
    case "medium":
        reminder_message += " Consider addressing it soon."
    case "low":
        reminder_message += " Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority level entered."

# Modify reminder based on time sensitivity
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder_message = f"'{task}' is a {priority} priority task that requires immediate attention today!"
    else:
        reminder_message += " You can handle it whenever you find time."

# Print the final reminder
print("Reminder:", reminder_message)
