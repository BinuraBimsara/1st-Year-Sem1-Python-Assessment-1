#Author : Binura
#Date : 25th Feb 2025

#a program to store tasks(including details like task name, description, priority, and due date), read tasks, update tasks and delete tasks.

tasks = []
def add_task():
    print("\n       Add a task\n")
    task_name = input("Enter the task name: ")
    for task in tasks:
        if task["name"] == task_name: #validation to check if the task name already exists
            print("\nTask name already exists")
            main()
    task_description = input("Enter the task description: ")
    while True:
        task_priority = input("Enter the task priority (high/medium/low): ")
        if task_priority.lower() not in ["high", "medium", "low"]:
            print("Invalid priority. Please enter a valid priority (high/medium/low)")  #Validating if the user inputs the correct priority
            continue
        break
    task_due_date = input("Enter the task due date (YYYY-MM-DD): ")

    task = {                 #Stores all the user data
        "name": task_name,
        "description": task_description,
        "priority": task_priority,
        "due_date": task_due_date
    }
    tasks.append(task)
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
    task_name = input("Enter the task name: ") #to check if the task name exists
    for task in tasks:
        if task["name"] == task_name:
            print("\nTask Found")
            print(f"\nTask name   : {task['name']}")
            print(f"Description : {task['description']}")
            print(f"Priority    : {task['priority']}")
            print(f"Due Date    : {task['due_date']}")
            break
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
    for task in tasks:
        if task["name"] == task_name:   #to check if the task name exists and displays it to the user for updating
            print("\nTask Found")
            print(f"\nTask name   : {task['name']}")
            print(f"Description : {task['description']}")
            print(f"Priority    : {task['priority']}")
            print(f"Due Date    : {task['due_date']}")

            while True:
                choice = input("\nDo you want to update this task? (yes/no) : ")
                if choice.lower() == "yes":
                    print("\nPress Enter to skip an update field")
                    task["description"] = input("\nEnter the task description   : ") or task["description"]  #to skip if the user press "Enter"
                    task["priority"] = input("Enter the task priority      : ") or task["priority"]
                    task["due_date"] = input("Enter the task due date      : ") or task["due_date"]

                    save_tasks()
                    print("\nTask updated successfully")
                    break
                elif choice.lower() == "no":
                    print("\nTask not updated")
                    break
                else:
                    print("Invalid input. Please enter a valid response (yes/no)")
            break
    else:
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

#-------Delete a Task Function----------------Delete a Task Function----------------Delete a Task Function---------
def delete_task():
    print("\n       Delete a task\n")
    task_name = input("Enter the task name you want to delete : ")
    for task in tasks:
        if task["name"] == task_name:   #checks if the task exists
            print("\nTask found \n")
            print(f"\nTask name   : {task['name']}")
            print(f"Description : {task["description"]}")
            print(f"Priority    : {task["priority"]}")
            print(f"Due Date    : {task["due_date"]}\n")
            choice = input("Do you want to delete this task? (yes/no) : ")
            if choice.lower() == "yes":
                tasks.remove(task)
                save_tasks()
                print("\nTask deleted successfully")
                break
            elif choice.lower() == "no":
                print("\nTask not deleted")
                break
            else:
                    print("Invalid input. Please enter a valid response (yes/no)")
                    break
    else:
        print("Task not found")
    while True:
        choice = input("\nDo you want to delete another task? (yes/no): ")
        if choice.lower() == "yes":
            delete_task()
        elif choice.lower() == "no":
            main()
        else:
            print("Invalid input. Please enter a valid response (yes/no)")
            continue

def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r") as f:
            tasks = []
            for line in f:
                parts = line.strip().split("|")  # Use "|" as a delimiter
                if len(parts) == 4:
                    task = {
                            "name": parts[0],
                            "description": parts[1],
                            "priority": parts[2],
                            "due_date": parts[3]
                            }
                    tasks.append(task)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open("tasks.txt", "w") as f:  # "w" mode overwrites the file
        for task in tasks:
            f.write(f"{task['name']}|{task['description']}|{task['priority']}|{task['due_date']}\n")

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
