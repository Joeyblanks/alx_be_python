# daily_reminder.py

# Prompt for task details
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a valid task.")

# Get and validate priority
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Please enter a valid priority: high, medium, or low.")

# Get and validate time sensitivity
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ["yes", "no"]:
        break
    print("Please enter 'yes' or 'no'.")

# Match-case to handle different priorities
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"

# Modify message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority == "low":
        message += ". Consider completing it when you have free time."
    else:
        message += " and can be scheduled accordingly."

# Print final message
print("\n" + message)

