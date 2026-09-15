def assign(list_of_items, task_to_be_added, item_type, item_type_plural):
    #user prompt
    print(f"\nEnter {item_type_plural} assigned to the task, or press Enter with no input to skip:")

    items_to_assign = []

    while True:

        item_to_append = input()

        if not item_to_append:
            task_to_be_added[item_type_plural] = items_to_assign
            break

        elif item_to_append.strip().lower() not in list_of_items:
            print(f"The {item_type} entered has not yet been saved in this session.")

        elif item_to_append.strip().lower() in items_to_assign:
            print(f"That {item_type} has already been assigned to this task")

        else:
            items_to_assign.append(item_to_append.strip().lower())

def toggle_status(tasks_in_session, current_status):
    matching_tasks = [task.get("name") for task in tasks_in_session if task.get("status") == current_status]

    status = "completed" if current_status else "uncompleted"
    action = "reverted to uncompleted" if current_status else "marked as completed"

    if not matching_tasks:
        print(f"There are no {status} tasks as of now\n")
        return

    print(f"\nHere are your {status} tasks: ")

    #display matching tasks
    for task in matching_tasks:
        print(task)

    task_to_toggle = input(f"\nEnter the name of the task which you wish to have {action}: ").strip().lower()

    if not task_to_toggle in matching_tasks:
        print(f"The input you entered is invalid. It is not a task that can be {action}\n")
        return

    else:
        #toggle status
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

def add_items(item_list, item_type, item_type_plural):
    #user prompt
    print(f"\nEnter {item_type_plural} you wish to add, or press Enter alone to finish:")

    added_items = []

    #validate input
    while True:
        item = input()

        if item:
            if item.isspace():
                print(f"This is all whitespaces and isn't a valid {item_type}\n"
                      f"Enter valid {item_type_plural}, or press Enter to stop:")
                continue
            if item.strip().lower() not in item_list:
                item_list.append(item.strip().lower())
                added_items.append(item.strip().lower())
            elif item.strip().lower() in item_list:
                print(f"This {item_type} is already saved in this session. Be mindful of spelling. Casing is irrelevant")
                print("You may continue, or press Enter to finish:")
                continue

        else:
            break

    label = item_type if len(added_items) == 1 else item_type_plural
    verb = "was" if len(added_items) == 1 else "were"
    print(f"{len(added_items)} {label} {verb} added")

    #display added items
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

    #user prompt
    print(f"\nEnter {item_type_plural} you wish to remove, or press Enter alone to finish:")

    removed_items = []

    #validate input
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

def list_items(list_of_items, list_item_plural):
    if not list_of_items:
        print(f"There are no {list_item_plural} saved yet\n")

    #display all items
    else:
        print(f"\nHere are the {list_item_plural} saved in your session:")
        for item in list_of_items:
            print(item)
        print()