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