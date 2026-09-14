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

def checktask(tasks):
    h.toggle_status(tasks, False)

def unchecktask(tasks):
    h.toggle_status(tasks, True)

def taskcomp(tasks):
    h.tasks_by_status(tasks, True, "Completed")

def taskluncomp(tasks):
    h.tasks_by_status(tasks, False, "Uncompleted")

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

def addplayers(players):
    h.add_items(players, "player", "players")

def remplayers(players):
    h.remove_items(players, "player", "players")

def listplayers(players):
    h.list_items(players, "players")

def addlocations(locations):
    h.add_items(locations, "location", "locations")

def remlocations(locations):
    h.remove_items(locations, "location", "locations")

def listlocations(locations):
    h.list_items(locations, "locations")

def addcategories(categories):
    h.add_items(categories, "category", "categories")

def remcategories(categories):
    h.remove_items(categories, "category", "categories", "default")

def listcategories(categories):
    h.list_items(categories, "categories")

def help_message():
    print("-The program manages all your TASKS. Tasks are the work you need to get done\n"
          "-They can have associated PLAYERS, designated LOCATIONS, and belong to a CATEGORY, all of which you predetermine.\n"
          "-A task can have only one name and fall under one category, but it can have multiple players and locations assigned\n"
          "-A task must not strictly have assigned players or locations, and belongs to a built-in default category if you do not assign one.\n"
          "-Tasks are marked as either completed or uncompleted.\n\n"
          "Let's familiarise you with the system's command:\n\n"
          "Tasks:\n"
          "addtask: add a new task\n"
          "remtask: delete an unfinished task\n"
          "checktask: mark a completed task as complete\n"
          "unchecktask: revert a completed task to uncompleted"
          "taskscomp: view completed tasks\n"
          "tasksuncomp: view unfinished tasks\n"
          "searchtask: find a specific task\n"
          "alltasks: display the names of all tasks\n\n"
          "Players:\n"
          "addplayers: add players to the system\n"
          "remplayers: remove players from the system\n"
          "listplayers: view all players\n\n"
          "Categories:\n"
          "addcategories: add task categories(eg Mining, Redstone)\n"
          "remcategories: delete task categories\n"
          "listcategories: view all task categories\n\n"
          "Locations:\n"
          "addlocations: add a locations(eg Basecamp, Sugarcane Farm)\n"
          "remlocations: remove a location\n"
          "listlocations: view all locations\n\n"
          "System/Meta\n"
          "help: pull up the user manual you are currently reading\n"
          "allstatus: to view all tasks, players, locations, categories (an overview of the whole session)\n"
          "exit: end your work session\n\n"
          "Some things you should know:\n"
          "-This program is not case sensitive. So 'Steve' and 'steve' are  considered the same thing\n"
          "-This program removes all leading and trailing whitespace in your inputs\n\n")

def allstatus(tasks, players, locations, categories):
    print("\nHere's overview of your entire session so far:\n")

    if not players:
        print("There are no players saved in this session\n")

    else:
        print("Players:")
        for player in players:
            print(player)
        print()

    if not locations:
        print("There are no locations saved in this session\n")

    else:
        print("Locations:")
        for location in locations:
            print(location)
        print()

    print("Categories:")
    for category in categories:
        print(category)
    print()

    if not tasks:
        print("You have no tasks in this session\n")
        return

    else:
        h.tasks_by_status(tasks, True, "Completed")
        h.tasks_by_status(tasks, False, "Uncompleted")


def setup(item_list, item_type, item_type_plural, presaved=0):
    print(f"Enter {item_type_plural} you want to save, or press Enter with no input to finish:")
    while True:
        item = input()
        if item:
            if item.isspace():
                print(f"I don't see anything. Please enter a valid {item_type}")
                continue
            elif item.lower().strip() in item_list:
                print(f"You already entered this {item_type}")
                continue
            item_list.append(item.strip().lower())
        else:
            if len(item_list) == presaved:
                print(f"\nNo new {item_type_plural} were entered")
                break
            print(f"\nThese are the {item_type_plural} you have entered: ")
            for item in item_list:
                print(item)
            break