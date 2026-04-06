import os
import json

task = {}
tasks = []


def loadTask():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except:
        tasks = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def taskCounter():
    completed = 0
    total = len(tasks)
    for i in tasks:
        if i["status"]:
            completed += 1
    pending = total - completed
    return total, completed, pending


def menu():
    total, completed, pending = taskCounter()

    print("\n====================================")
    print("           TASK MANAGER")
    print("====================================")
    print(f"Total: {total} | Completed: {completed} | Pending: {pending}")
    print("------------------------------------")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task Complete")
    print("5. Edit Task")
    print("6. Exit")
    print("====================================")


def saveTask():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


def addTask():
    print("\n--- ADD NEW TASK ---")
    title = input("Enter task name: ")

    task = {"id": len(tasks) + 1, "title": title, "status": False}

    tasks.append(task)
    saveTask()

    print("\n✅ Task added successfully.")
    input("\nPress Enter to continue...")


def removeTask():
    print("\n--- REMOVE TASK ---")
    try:
        RmId = int(input("Enter task ID to remove: "))
    except:
        print("Invalid input")
        found = False

    for t in tasks:
        if t["id"] == RmId:
            tasks.remove(t)
            found = True
            saveTask()
            print("\n🗑 Task removed.")
            break

    if not found:
        print("\nTask not found.")

    input("\nPress Enter to continue...")


def taskFilter(filter):

    print("\n----------- TASK LIST -----------")

    if filter == 1:

        if not tasks:
            print("No tasks available.")
        else:
            try:
                for t in tasks:
                    status = "✔" if t["status"] else "✘"
                    print(f"{t['id']}. {t['title']}  [{status}]")
            except:
                print("No tasks available.")

    elif filter == 2:
        try:
            for t in tasks:
                if t["status"] == True:
                    print(f"{t['id']}. {t['title']}  [✔]")
        except:
            print("No completed task")

    elif filter == 3:
        try:
            for t in tasks:
                if t["status"] == False:
                    print(f"{t['id']}. {t['title']}  [✘]")
        except:
            print("No pending task")

    print("---------------------------------")


def viewTask():

    print("\n======= VIEW TASKS =======")
    print("1. Show All Tasks")
    print("2. Show Completed Tasks")
    print("3. Show Pending Tasks")
    print("==========================")

    try:
        filter = int(input("Select filter: "))
    except:
        print("Enter valid input")

    if filter == 1:
        taskFilter(filter)
        input("\nPress Enter to continue...")

    elif filter == 2:
        taskFilter(filter)
        input("\nPress Enter to continue...")

    elif filter == 3:
        taskFilter(filter)
        input("\nPress Enter to continue...")


def markAsComplete():

    print("\n--- MARK TASK COMPLETE ---")

    try:
        taskId = int(input("Enter task ID: "))
    except:
        print("Invalid input")

    found = False

    for t in tasks:
        if t["id"] == taskId:
            t["status"] = True
            found = True
            saveTask()
            print("\n✔ Task marked as complete.")
            break

    if not found:
        print("\nTask not found.")

    input("\nPress Enter to continue...")


def editTask():

    print("\n--- EDIT TASK ---")

    try:
        id = int(input("Enter task ID to edit: "))
    except:
        print("Enter valid input")

    found = False

    for t in tasks:
        if t["id"] == id:
            newTitle = input("Enter new task name: ")
            t["title"] = newTitle
            saveTask()
            print("\n✏ Task updated.")
            found = True
            break

    if not found:
        print("\nTask not found.")

    input("\nPress Enter to continue...")


loadTask()

while True:
    clear()
    menu()

    try:
        choice = int(input("\nEnter your choice: "))
    except:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        addTask()
    elif choice == 2:
        removeTask()
    elif choice == 3:
        viewTask()
    elif choice == 4:
        markAsComplete()
    elif choice == 5:
        editTask()
    elif choice == 6:
        print("\nThank you for using Task Manager 👋")
        break
    else:
        print("Invalid option. Please choose between 1-6.")
