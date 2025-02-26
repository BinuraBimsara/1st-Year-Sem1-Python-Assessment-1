#Author : Binura
#Date : 25th Feb 2025

#a program to store tasks, including details like task name, description, priority, and due date.
tasks = []
def main():

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
    print("1. Create a task")
    print("2. Read a task ")
    print("3. Update a task")
    print("4. Delete a task ")
    print("5. Exit")
    print()

    while True:
        try:
            choice = int(input("Enter your choice : "))

        except ValueError:
            print("Invalid input. Please enter a number  ")
            print()
            continue
        else:
            break

    if choice == 1:
        create_task()
    if choice == 2:
        read_task()
    # if choice == 3:
    #     update_task()
    # if choice == 4:
    #     delete_task()
    while True:
        if choice == 5:
            x=input("\nAre you sure you want to exit the program? (yes/no): ")
            if x.lower() == "yes":
                exit()
            elif x.lower() == "no":
                main()
            else:
                print("\nInvalid input. Please enter a valid response (yes/no)")
                continue
            break
    if choice > 5:
        print("Invalid input. Please enter a number between 1 and 5")
        print()
        main()


#-------Create a Task Function----------------Create a Task Function----------------Create a Task Function----------------Create a Task Function---------
def create_task():
    print("\n       Create a task\n")
    task_name = input("Enter the task name          : ")
    task_description = input("Enter the task description   : ")
    task_priority = input("Enter the task priority      : ")
    task_due_date = input("Enter the task due date      : ")

    task = {            "name":task_name,
                        "description": task_description,
                        "priority": task_priority,
                        "due_date": task_due_date
                        }

    tasks.append(task)
    print(task)
    print("\nTask created successfully")

    while True:
        choice = input("\nDo you want to create another task? (yes/no): ")
        if choice.lower() == "yes":
            create_task()
        elif choice.lower() == "no":
            main()
        else:
            print("Invalid input. Please enter a valid response (yes/no)")
            continue
        break


def read_task():
    print("\n       Read a task\n")
    task_name = input("Enter the task name: ")
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
            read_task()
        elif choice.lower() == "no":
            main()
        else:
            print("Invalid input. Please enter a valid response (yes/no)")
            continue
        break



main()