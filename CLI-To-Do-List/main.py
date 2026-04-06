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


def menu():
    print("\n==============================")
    print("        TASK MANAGER")
    print("==============================")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task Complete")
    print("5. Edit Task")
    print("6. Exit")
    print("==============================")


def saveTask():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


def addTask():
    title = input("\nEnter the name of the task: ")

    task = {"id": len(tasks) + 1, "title": title, "status": False}

    tasks.append(task)
    saveTask()

    print("✅ Task added successfully.")
    input("\nPress Enter to continue...")


def removeTask():
    try:
        RmId = int(input("\nEnter the task number to remove: "))
    except:
        print("Invalid input")
        found = False

    for t in tasks:
        if t["id"] == RmId:
            tasks.remove(t)
            found = True
            saveTask()
            print("🗑 Task removed.")
            break

    if not found:
        print("Task not found.")
    input("\nPress Enter to continue...")


def viewTask():
    print("\n----------- TASK LIST -----------")

    if not tasks:
        print("No tasks available.")
    else:
        for t in tasks:
            status = "✔" if t["status"] else "✘"
            print(f"{t['id']}. {t['title']} [{status}]")

    print("---------------------------------")
    input("\nPress Enter to continue...")


def markAsComplete():
    try:
        taskId = int(input("\nEnter task Id: "))
    except:
        print("Invalid input")

    found = False

    for t in tasks:
        if t["id"] == taskId:
            t["status"] = True
            found = True
            saveTask()
            print("✔ Task marked as complete.")
            break

    if not found:
        print("Task not found.")
    input("\nPress Enter to continue...")


def editTask():
    try:
        id = int(input("Enter ID of the task to rename: "))
    except:
        print("Enter valid input")

    found = False

    for t in tasks:
        if t["id"] == id:
            newTitle = input("Enter new task: ")
            t["title"] = newTitle
            saveTask()
            print("Task was edited")
            found = True
            break

    if not found:
        print("Task was not found")
    input("\nPress Enter to continue...")


loadTask()


while True:
    clear()
    menu()
    try:
        choice = int(input("Enter your choice: "))
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
        print("Invalid option. Please choose between 1-5.")
