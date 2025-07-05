tasks = [] ## List to store all tasks

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():     ## This function add a new task on the list
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, t in enumerate(tasks):
            status = "✔" if t["done"] else "✘"
            print(f"{i+1}. [{status}] {t['task']}")  #Display task number and description
def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as done!")
    except:
        print("Invalid input.")

def delete_task():   ## This function remove a task by name
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        print(f"Deleted: {removed['task']}")
    except:
        print("Invalid input.")

# Main loop
while True:
    show_menu()    # This function is to show all current tasks
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_task()  #Call add function
    elif choice == "2":
        view_tasks() 
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break     #Exit loop and program
    else:
        print("Please choose a valid option.")
        #Handle invalid input

