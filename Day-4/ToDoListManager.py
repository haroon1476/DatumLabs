import json

def loadTasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] # returning empty list indication file not found error


def saveTasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def addTask():

    tasks = loadTasks() # getting previous tasks

    newTask = input("Enter new task: ")
    tasks.append({"task": newTask})

    saveTasks(tasks)
    print(f" Task added: {newTask}")


def listTasks():
    tasks = loadTasks()
    if not tasks:
        print(" No tasks to show.")
        return
    
    print("\n Tasks are:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['task']}")


def deleteTask():

    tasks = loadTasks()
    if not tasks:
        print(" No tasks to delete.")
        return

    listTasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1) # getting that task from the list
            saveTasks(tasks)
            print(f" Deleted: {removed['task']}")
        else:
            print(" Invalid number.")
    except ValueError:
        print(" Please enter a valid number.")


def main():

    while True:
       
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            addTask()

        elif choice == "2":
            listTasks()

        elif choice == "3":
            deleteTask()

        elif choice == "4":
            print("\n Exited successfully!")
            break
        else:
            print(" Invalid choice. Try again.")

# main func call
main()
