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

def tasks_by_status(list_of_tasks, status, label):
    matching_tasks = [task for task in list_of_tasks if task.get("status") == status]
    if not matching_tasks:
        print(f"You have no {label} tasks")
        return

    print(f"{label} tasks: ")
    for task in matching_tasks:
        print(task.get("name"))
    print()

def searchtask(tasks):
    if not tasks:
        print("You currently have no tasks yet\n")
        return

    task_to_search = input("\nWhich task are you looking for: ").strip().lower()

    for task in tasks:
        if task.get("name") == task_to_search:
            print(f"Task Name: {task.get("name")}")
            print("Assigned Players: ")
            if task.get("players"):
                for player in task.get("players"):
                    print(player)
            else:
                print("No assigned players")
            print("Task Locations:")
            if task.get("locations"):
                for location in task.get("locations"):
                    print(location)
            else:
                print("No assigned locations")
            print(f"Task Category: {task.get("category")}")
            print("Task Status: ", end="")
            if task.get("status"):
                print("Completed")
            else:
                print("Unfinished")
            break

    else:
        print("No such task of that name exists.\nPlease use the 'alltasks' command to view the tasks saved in your session\n")

def alltasks(tasks):
    if not tasks:
        print("\nNo tasks exist yet\n")
        return

    print("\nAll Tasks:")
    counter = 1
    for task in tasks:
        print(f"{counter}. {task.get("name")}: ", end="")
        if task.get("status"):
            print("Completed")
        else:
            print("Unfinished")
        counter += 1

    print()


def add_items(item_list, item_type, item_type_plural):
    print(f"\nEnter {item_type_plural} you wish to add, or press Enter alone to finish:")

    added_items = []
    while True:
        item = input()

        if item:
            if item.isspace():
                print(f"This is all whitespaces and isn't a valid {item_type}\n"
                      f"Enter valid {item_type_plural}, or press Enter to stop")
                continue
            if item.strip().lower() not in item_list:
                item_list.append(item.strip().lower())
                added_items.append(item.strip().lower())
            else:
                print(
                    f"This {item_type} is already saved in this session. Be mindful of spelling. Casing is irrelevant")
                print("You may continue, or press Enter to finish:")
                continue

        else:
            break

    label = item_type if len(added_items) == 1 else item_type_plural
    verb = "was" if len(added_items) == 1 else "were"
    print(f"{len(added_items)} {label} {verb} added")

    if added_items:
        print(f"Added {item_type_plural}:")
        for item in added_items:
            print(item)
    print()


def remove_items(item_list, item_type, item_type_plural, protected_item=None):
    min_length = 1 if protected_item else 0

    if len(item_list) == min_length:
        print(f"There aren't any {item_type_plural} saved in this session that can be deleted\n")
        return

    print(f"\nEnter {item_type_plural} you wish to remove, or press Enter alone to finish:")

    removed_items = []
    while True:
        item = input()

        if item and item.strip().lower() in item_list:
            if item.strip().lower() != protected_item:
                item_list.remove(item.strip().lower())
                removed_items.append(item.strip().lower())
            else:
                print(f"{protected_item} is a built-in {item_type} for tasks. It cannot be removed\n"
                      "You may continue, or press Enter to finish:")
                continue
        elif item and item.strip().lower() not in item_list:
            print(f"This {item_type} is not saved to the system. Be mindful of spelling. Casing is irrelevant")
            print("You may continue, or press Enter to finish:")
            continue
        elif not item:
            break

    label = item_type if len(removed_items) == 1 else item_type_plural
    verb = "was" if len(removed_items) == 1 else "were"
    print(f"{len(removed_items)} {label} {verb} removed")

    if removed_items:
        print(f"Removed {item_type_plural}:")
        for item in removed_items:
            print(item)
    print()
