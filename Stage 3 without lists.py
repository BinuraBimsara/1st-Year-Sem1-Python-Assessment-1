#Author : Binura
#Date : 25th Feb 2025
#a program to store tasks(including details like task name, description, priority, and due date), read tasks, update tasks and delete tasks.
import json
tasks={}
def add_task():
    print("\n       Add a task\n")
    task_name = input("Enter the task name: ")
    if task_name.lower() in tasks:
        print("\nTask name already exists!")
        add_task()
    task_description = input("Enter the task description: ")
    while True:
        task_priority = input("Enter the task priority (high/medium/low): ")
        if task_priority.lower() not in ["high", "medium", "low"]:
            print("Invalid priority. Please enter a valid priority (high/medium/low)")  #Validating if the user inputs the correct priority
            continue
        break
    task_due_date = input("Enter the task due date (YYYY-MM-DD): ")

    tasks[task_name.lower()] = {  # [task_name]is a unique identifier for each task
        "description": task_description,  #Stores all the user daat
        "priority": task_priority,
        "due_date": task_due_date
    }
    save_tasks()
    print("\nTask created successfully!")

    while True:
        choice = input("\nDo you want to create another task? (yes/no): ")
        if choice.lower() == "yes":
            add_task()
        elif choice.lower() == "no":
            main()
        else:
            print("Invalid input. Please enter a valid response (yes/no)")
            continue

#-------View a Task Function----------------View a Task Function----------------View a Task Function----------------View a Task Function---------
def view_task():
    print("\n       View a task\n")
    task_name = input("Enter the task name: ")
    if task_name.lower() in tasks:       #to check if the task name exists
        task = tasks[task_name.lower()]  # Retrieve task details
        print("\nTask Found")
        print(f"\nTask Name   : {task_name}")
        print(f"Description : {task['description']}")
        print(f"Priority    : {task['priority']}")
        print(f"Due Date    : {task['due_date']}")
    else:
        print("Task not found")

    while True:
        choice = input("\nDo you want to read another task? (yes/no): ")
        if choice.lower() == "yes":
            view_task()
        elif choice.lower() == "no":
            main()
        else:
            print("Invalid input. Please enter a valid response (yes/no)")
            continue

#-------Update a Task Function----------------Update a Task Function----------------Update a Task Function----------------Update a Task Function---------
def update_task():
    print("\n       Update a task\n")
    task_name = input("Enter the task name you want to update : ")
    if task_name.lower() in tasks:       #to check if the task name exists
        task = tasks[task_name.lower()]  # Retrieve task details
        print("\nTask Found")
        print(f"\nTask Name   : {task_name}")
        print(f"Description : {task['description']}")
        print(f"Priority    : {task['priority']}")
        print(f"Due Date    : {task['due_date']}")
        while True:
            choice = input("\nDo you want to update this task? (yes/no) : ")
            if choice.lower() == "yes":
                print("\nPress Enter to skip an update field")
                tasks[task_name.lower()]["description"] = input("Enter the task description : ") or tasks[task_name]["description"]  #to skip if the user press "Enter"
                tasks[task_name.lower()]["priority"] = input("Enter task priority        : ") or tasks[task_name]["priority"]
                tasks[task_name.lower()]["due_date"] = input("Enter task due date        : ") or tasks[task_name]["due_date"]
                save_tasks()
                print("\nTask updated successfully")
                break
            elif choice.lower() == "no":
                print("\nTask not updated")
                break
            else:
                print("Invalid input. Please enter a valid response (yes/no)")
    else: #Error
        print("Task not found")

    while True:
        choice = input("\nDo you want to update another task? (yes/no): ")
        if choice.lower() == "yes":
            update_task()
        elif choice.lower() == "no":
            main()
        else:
            print("Invalid input. Please enter a valid response (yes/no)")
            continue

# #-------Delete a Task Function----------------Delete a Task Function----------------Delete a Task Function---------
def delete_task():
    print("\n       Delete a task\n")
    task_name = input("Enter the task name you want to delete : ")
    if task_name.lower() in tasks:       #to check if the task name exists
        task = tasks[task_name.lower()]  # Retrieve task details
        print("\nTask Found")
        print(f"\nTask Name   : {task_name}")
        print(f"Description : {task['description']}")
        print(f"Priority    : {task['priority']}")
        print(f"Due Date    : {task['due_date']}")
        choice = input("Do you want to delete this task? (yes/no) : ")
        if choice.lower() == "yes":
            del(tasks[task_name.lower()])
            save_tasks()
            print("\nTask deleted successfully")
        elif choice.lower() == "no":
            print("\nTask not deleted")
        else:
                print("Invalid input. Please enter a valid response (yes/no)")
    else:
        print("Task not found") #Error

    while True:
        choice = input("\nDo you want to delete another task? (yes/no): ")
        if choice.lower() == "yes":
            delete_task()
        elif choice.lower() == "no":
            main()
        else:
            print("Invalid input. Please enter a valid response (yes/no)")
            continue

def save_tasks():
    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)  # Write JSON to file

def load_tasks():
    """Loads tasks from a JSON file if it exists"""
    global tasks
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}  # Initialize an empty dictionary if file doesn't exist

def main():
    load_tasks()
    ascii_art = """
     _____         _      __  __
    |_   _|_ _ ___| | __ |  \/  | __ _ _ __   __ _  __ _  ___ _ __
      | |/ _` / __| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
      | | (_| \__ \   <  | |  | | (_| | | | | (_| | (_| |  __/ |
      |_|\__,_|___/_|\_\ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|
                                                   |___/
    """
    print(ascii_art)
    print("Select an Option ")
    print()
    print("1. Add a task")
    print("2. View a task ")
    print("3. Update a task")
    print("4. Delete a task ")
    print("5. Exit")
    print()

    while True:
        try:
            choice = int(input("Enter your choice : "))

        except ValueError:
            print("Invalid input. Please enter a valid number  ")
            print()
            continue
        else:
            break

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        update_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        while True:
                x=input("\nAre you sure you want to exit the program? (yes/no): ")
                if x.lower() == "yes":
                    print("\nGoodbye")
                    exit()
                elif x.lower() == "no":
                    main()
                else:
                    print("\nInvalid input. Please enter a valid response (yes/no)")
                break
    else:
        print("Invalid input. Please enter a number between 1 and 5")
        print()
        main()

if __name__ == "__main__":
    main()
