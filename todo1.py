import json

file_name = "tasks.json"

def show_menu():
    print ("\n---------TO-DO APP---------")
    print ("1. Add Task")
    print ("2. View Task")
    print ("3. Mark Task as Done")
    print ("4. Delete Task")
    print ("5. Edit Task")
    print ("6. Search / Filter Task")
    print ("7. Exit")

def load_task():
    try: 
        with open(file_name, "r") as file:
            tasks =  json.load(file)
        for task in tasks:
                task.setdefault("due", None)
                task.setdefault("priority", "Normal")
        return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_task(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent = 4)

def show_task(tasks):
    if not tasks:
        print ("No tasks Found.")
        return False
    pending_tasks = [task for task in tasks if not task.get ("done", False)]
    done_tasks = [task for task in tasks if task.get("done", False)]
    ordered_tasks = pending_tasks + done_tasks
    for i, task in enumerate(ordered_tasks,1):
        status = "Done" if task.get("done") else "pending!!"
        due = task.get("due") or "No due Date"
        priority = task.get("priority", "Normal")
        print (f"{i}. {task['title']} | {status} | {due} | Priority: {task['priority']}")
    return True


def add_task(tasks):
    title = input ("Enter a task title: ").strip()
    if title== "":
        print ("Task title cannot be empty: ")
        return 
    
    due = input ("Due date (YYYY-MM-DD or leave empty): ").strip()
    priority = input ("Priority (Low/High/Normal) if needed or press 'Enter': ").strip().capitalize()

    if priority not in ["Low", "Normal", "High"]:
        priority = "Normal"

    task = {
        "title": title,
        "done": False,
        "due" : due if due else None,
        "priority": priority
    }
    tasks.append(task)
    save_task(tasks)
    print ("Task added.")

def view_task(tasks):
    print ("\nView Task Selected: \n")
    show_task(tasks)
    input ("Press 'Enter' to go back")

def mark_task_as_done(tasks):
        while True:
            print ("\nMark done is selected: \n")
            if not show_task(tasks):
                return
            user = input("Enter a Task Number to Mark as Done or Press 'Enter to go back: ").strip()
            if user == "":
                return
            try:
                num = int(user)
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    save_task(tasks)
                    print ("Task Marked as Done!!")
                else:
                    print ("Invalid Task Number.")
            except ValueError:
                print ("Enter a Valid Task Number.")

def delete_task(tasks):
    while True:
        print ("\nDelete task is selected: \n")
        if not show_task(tasks):
            return
        user = input("Enter a Task Number to Delete or Press 'Enter to go back: ").strip()
        if user == "":
            return
        try:
            num = int(user)
            if 1 <= num <= len(tasks):
                remove = tasks.pop(num - 1)
                save_task(tasks)
                print (f"Deleted: {remove['title']}")
            else:
                print ("Invalid Task Number.")
        except ValueError:
            print ("Enter a Valid Task Number.")    

def edit_task(tasks):
    while True:
        print ("\nEdit Task is selected: \n")
        if not show_task(tasks):
            return
        user = input("Enter a Task Number to Edit or Press 'Enter to go back: ").strip()
        if user == "":
            return
        try:
            num = int(user)
            if 1 <= num <= len(tasks):
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

def search_task(tasks):
    if not tasks:
        print("No tasks available.")
        return 
    query = input ("Search keyword (Leave empty to skip): ").strip().lower()
    print ("1. All")
    print ("2. Pending only")
    print ("3. Done only")

    choice = input ("Filter Choice: ")
    result = []

    for task in tasks:
        if query and query not in task["title"].lower():
            continue
        if choice == "2" and task["done"]:
            continue
        if choice =="3" and not task["done"]:
            continue
        result.append(task)

    if not result:
        print ("No matching tasks.")
        return
    print ("\nResults: ")
    for i, task in enumerate(result, 1):
        status = "Done" if task["done"] else "Pending!!"
        print (f"{i}. {task['title']} - {status}")
    input("\nPress Enter to go back")



def main():
    tasks = load_task()

    while True:
        show_menu()
        choice = input("Choose a Option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            mark_task_as_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            search_task(tasks)
        elif choice == "7":
            print ("Goodbye!!")
            break
        else:
            print ("Invalid Choice.")

if __name__ == "__main__":
    main()