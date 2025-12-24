import json

file_name = "tasks.json"

def load_task():
    try: 
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_task(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent = 4)

tasks = load_task()

while True:
    print ("\n-----------TO DO APP----------\n")
    print ("1. Add Task.")
    print ("2. View Tasks.")
    print ("3. Mark a Task as Done.")
    print ("4. Delete a Task.")
    print ("5. Edit Tasks.")
    print ("6. Exit.")

    choice = input ("Choose an option: ")
    if choice == "1":
        while True:
            print ("\nAdd Task selected\n")
            title = input("Enter a task title or Enter a '0' to go back: ")
            if title == "0":
                print ("No Task is Added.")
                break
            else:
                task = {
                    "title": title, "done": False
                }
                tasks.append(task)
                save_task(tasks)
                print("Task Added Successfully")

    elif choice == "2":
        print ("\nView Tasks selected\n")
        if not tasks:
            print ("Task not found!")
        else:
            print ("\n Your Tasks: ")
            for i , task in enumerate(tasks):
                status = "Done" if task["done"] else "Pending!!"
                print (f"{i+1}. {task['title']} - {status}")
        input ("Press Enter to go back.")

    elif choice == "3":
        while True:
            print ("\nMarking Task is selected:\n")
            if not tasks:
                print ("No Task to Mark.")
                break
            else:
                for i, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Pending!!"
                    print (f"{i+1}. {task['title']} - {status}")
                try:
                    num = int(input("Enter a Task Number to Mark as Done or Enter '0' to go back: "))
                    if num == 0:
                        break
                    elif 1 <= num <= len(tasks):
                        tasks[num - 1]["done"] = True
                        save_task(tasks)
                        print ("Task Marked as Done!!")
                    else:
                        print ("Invalid Task Number.")
                except:
                    print ("Enter a Valid Task Number.")
    elif choice == "4":
        while True:
            print ("\nDelete Task is selected:\n")
            if not tasks:
                print ("No Tasks to Delete.")
                break
            else:
                for i, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Pending!!"
                    print (f"{i+1}. {task['title']} - {status}")
                try:
                    num = int(input("Enter a Task Number to Delete or Enter '0' to go back: "))
                    if num == 0:
                        break
                    elif 1 <= num <= len(tasks):
                        remove = tasks.pop(num - 1)
                        save_task(tasks)
                        print (f"Deleted: {remove['title']}")
                    else:
                        print ("Invalid Task Number.")
                except ValueError:
                    print ("Enter a Valid Task Number.")
    elif choice == "5":
        while True:
            print ("\nEdit Task is selected: \n")
            if not tasks:
                print ("No Tasks to Edit.")
                break
            else:
                for i, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Pending!!"
                    print (f"{i+1}. {task['title']} - {status}")
                try:
                    num = int(input("Enter a Task Number to Edit or Enter '0' to go back: "))
                    if num == 0:
                        break
                    elif 1 <= num <= len(tasks):
                        old_title = tasks[num - 1]["title"]
                        new_title = input(f"Enter a New Title or (Leave Empty to Cancel): ").strip()
                        if new_title == "":
                            print ("Edit Cancelled.")
                        else:
                            tasks[num - 1]["title"] = new_title
                            save_task(tasks)
                            print (f"Task Updated From: '{old_title}' To: '{new_title}'")
                    else:
                        print ("Invalid Task Number.")
                except ValueError:
                    print ("Enter a Valid Task Number.")
    elif choice == "6":
        print ("Goodbye!!")
        break
    else:
        print("Invalid Choice. Try again .")

