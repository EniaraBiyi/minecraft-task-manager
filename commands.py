import helpers as h
def addtask(tasks, players, locations, categories):
    task_to_add = {}

    #obtain task name
    print("\nEnter inputs for the prompts accordingly. Press Enter without input to skip or continue")
    while True:
        task_name = input("Enter task name: ")

        if not task_name or task_name.isspace():
            print("You must enter a valid task name")

        elif task_name.strip().lower() in [task.get("name") for task in tasks]:
            print("A task of the same name already exists")

        else:
            task_to_add["name"] = task_name.strip().lower()
            break

    #obtain task players
    h.assign(players, task_to_add, "player", "players")

    #obtain task locations
    h.assign(locations, task_to_add, "location", "locations")

    #obtain task category
    while True:
        task_category = input(
            "\nEnter the category for this task. Press Enter alone to put task in the default category: ")

        if not task_category:
            task_to_add["category"] = "default"
            break

        elif task_category.strip().lower() not in categories:
            print("The category entered has not yet been saved in the system.")

        else:
            task_to_add["category"] = task_category.strip().lower()
            break

    #set task status
    task_to_add["status"] = False

    #add task
    tasks.append(task_to_add)
    print("\nYour task was successfully added\n")

def remtask(tasks):
    deletable_tasks = [task.get("name") for task in tasks if not task.get("status")]

    if not deletable_tasks:
        print("There are currently no tasks in the system to delete\n")
        return

    else:
        print("\nCurrent pending tasks in system (You can only delete uncompleted tasks)\n:")
        for task in deletable_tasks:
            print(task)

    task_to_delete = input("\nEnter the name of the task which you wish to delete: ").strip().lower()

    if not task_to_delete in deletable_tasks:
        print("No such pending task exists\n")
        return

    else:
        for task in tasks:
            if task.get("name") == task_to_delete:
                tasks.remove(task)
                break
        print("\nThe task was successfully deleted\n")

def toggle_status(tasks_in_session, current_status):
    matching_tasks = [task.get("name") for task in tasks_in_session if task.get("status") == current_status]

    status = "completed" if current_status else "uncompleted"
    action = "reverted to uncompleted" if current_status else "marked as completed"

    if not matching_tasks:
        print(f"There are no {status} tasks as of now\n")
        return

    print(f"\nHere are your {status} tasks: ")

    for task in matching_tasks:
        print(task)

    task_to_toggle = input(f"\nEnter the name of the task which you wish to have {action}: ").strip().lower()

    if not task_to_toggle in matching_tasks:
        print(f"The input you entered is invalid. It is not a task that can be {action}\n")
        return

    else:
        for task in tasks_in_session:
            if task.get("name") == task_to_toggle:
                task["status"] = not current_status
                print(f"\nThe task was successfully {action}\n")
                break