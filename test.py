tasks = []  # Ensure 'tasks' is defined globally

def create_task():
    print("\n       Create a task\n")

    task_name = input("Enter the task name          : ")
    task_description = input("Enter the task description   : ")
    task_priority = input("Enter the task priority      : ")
    task_due_date = input("Enter the task due date      : ")

    # Check if task already exists
    for task in tasks:
        if task["name"] == task_name:
            print("\nTask already exists")
            return  # Stop execution if task is found

    # If task is not found, create it
    task = {
        "name": task_name,
        "description": task_description,
        "priority": task_priority,
        "due_date": task_due_date
    }

    tasks.append(task)
    print("\nTask created successfully")

    # Ask user if they want to add another task
    while True:
        choice = input("\nDo you want to create another task? (yes/no): ").strip().lower()
        if choice == "yes":
            create_task()  # Call function again
        elif choice == "no":
            return  # Exit function
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

create_task()