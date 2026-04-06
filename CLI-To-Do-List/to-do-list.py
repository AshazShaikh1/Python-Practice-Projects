import os
import json

task = {}
tasks = []

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except:
    tasks = []


def saveTask():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def clear():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    clear()
    print("\n==============================")
    print("        TASK MANAGER")
    print("==============================")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task Complete")
    print("5. Exit")
    print("==============================")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        title = input("\nEnter the name of the task: ")

        task = {
            "id": len(tasks) + 1,
            "title": title,
            "status": False
        }

        tasks.append(task)
        saveTask()

        print("✅ Task added successfully.")
        input("\nPress Enter to continue...")

    elif choice == 2:

        try:
            RmId = int(input("\nEnter the task number to remove: "))
        except:
            print("Invalid input")
            continue

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

    elif choice == 3:

        print("\n----------- TASK LIST -----------")

        if not tasks:
            print("No tasks available.")
        else:
            for t in tasks:
                status = "✔" if t["status"] else "✘"
                print(f"{t['id']}. {t['title']} [{status}]")

        print("---------------------------------")
        input("\nPress Enter to continue...")

    elif choice == 4:

        try:
            taskId = int(input("\nEnter task Id: "))
        except:
            print("Invalid input")
            continue

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

    elif choice == 5:
        print("\nThank you for using Task Manager 👋")
        break

    else:
        print("Invalid option. Please choose between 1-5.")