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
                        print(f"This {item_type} is already saved in this session. Be mindful of spelling. Casing is irrelevant")
                        print("You may continue, or press Enter to finish:")
                        continue

            else:
                  break

      label = item_type if len(added_items) else item_type_plural
      verb = "was" if added_items == 1 else "were"
      print(f"{added_items} {label} {verb} added")

      if added_items:
            print(f"Added {item_type_plural}:")
            for item in added_items:
                  print(item)
      print()

def remove_items(item_list, item_type, item_type_plural, protected_item = None):
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

def tasks_by_status(list_of_tasks, status, label):
      matching_tasks = [task for task in list_of_tasks if task.get("status") == status]
      if not matching_tasks:
            print(f"You have no {label} tasks")
            return

      print(f"{label} tasks: ")
      for task in matching_tasks:
                  print(task.get("name"))
      print()

def list_items(list_of_items, list_item_plural):
      if not list_of_items:
            print(f"There are no {list_item_plural} saved yet\n")

      else:
            print(f"\nHere are the {list_item_plural} saved in your session:")
            for item in list_of_items:
                  print(item)
            print()

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
            "checktask: mark an unfinished task as complete\n"
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

#Data Structures:
tasks = []
players = []
locations = []
categories = ["default"]

#Welcome Message and tutorial
print("Welcome to the Minecraft Task Manager!!!\n"
      "No more shall you struggle with your in-game administrative tasks. You can centralize your workflow here\n\n")
help_message()

#Session setup
print("Let's get your session all setup!\n")
#Adding players
print("First, let's add players to your system: ")
print("Enter player names you want to save, or press Enter with no input to finish:")
while True:
      player = input()
      if player:
            if player.isspace():
                  print("I don't see anything. Please enter a valid player name")
                  continue
            if player.lower().strip() in players:
                  print("You already entered this player")
                  continue
            players.append(player.strip().lower())
      else:
            if len(players) == 0:
                  print("\nNo player was entered")
                  break
            print("\nThese are the players you have entered: ")
            for player in players:
                  print(player)
            break

#Adding location
print("\nNext, let's add locations: ")
print("Like before, Enter the locations you want to save, or press Enter with no input to finish:")
while True:
      location = input()
      if location:
            if location.isspace():
                  print("I don't see anything. Please enter a valid location")
                  continue
            elif location.lower().strip() in locations:
                  print("You already entered this location")
                  continue
            locations.append(location.strip().lower())
      else:
            if len(locations) == 0:
                  print("\nNo location was entered")
                  break
            print("\nThese are the locations you have entered: ")
            for location in locations:
                  print(location)
            break

#Adding Categories
print("\nFinally, let's add categories, that'll help group similar tasks together\n"
      "(Note that there is already a Default category for tasks that won't have a specific category assigned): ")
print("Enter categories you want to save, or press Enter without input to finish:")
while True:
      category = input()
      if category:
            if category.isspace():
                  print("Please enter a valid category")
                  continue
            elif category.lower().strip() in categories:
                  print("This category has already been saved")
                  continue
            categories.append(category.strip().lower())
      else:
            if len(categories) == 1:
                  print("\nNo category was entered. Only the default one currently exists")
                  break
            print("\nThese are the categories you have entered (default is built-in): ")
            for category in categories:
                  print(category)
            break


print("\nGreat, you should be all set up now.\n"
      "Now you have full accesss to the programs features and can enter commands at will. Enjoy : )\n")


#Command processor
while True:
      command = input("Enter command: ").strip().lower()

      if command == "exit":
            print("\nSession Ended")
            print("Thank you for using the Minecraft Task Manager")
            break

      #addtask command logic
      elif command == "addtask":
            task_to_add = { }

            task_name = ""
            task_players = []
            task_locations = []
            task_category = ""

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
            print("\nEnter player(s) assigned to the task, or press Enter to skip:")
            while True:
                  task_player = input()

                  if not task_player:
                        task_to_add["players"] = task_players
                        break

                  elif task_player.strip().lower() not in players:
                        print("The player entered has not yet been saved in the system.")

                  elif task_player.strip().lower() in task_players:
                        print("That player has already been assigned to this task")

                  else:
                        task_players.append(task_player.strip().lower())

            #obtain task locations
            print("\nEnter location(s) for the task, or press Enter to skip: ")
            while True:
                  task_location = input()
                  if not task_location:
                        task_to_add["locations"] = task_locations
                        break

                  elif task_location.strip().lower() not in locations:
                        print("The location entered has not yet been saved in the system. Please enter a valid location")

                  elif task_location.strip().lower() in task_locations:
                        print("That location has already been assigned to this task")

                  else:
                        task_locations.append(task_location.strip().lower())

            #obtain task category
            while True:
                  task_category = input("\nEnter the category for this task. Press Enter alone to put task in the default category: ")

                  if not task_category:
                        task_to_add["category"] = "default"
                        break

                  elif task_category.strip().lower() not in categories:
                        print("The category entered has not yet been saved in the system.")

                  else:
                        task_to_add["category"] = task_category.strip().lower()
                        break

            #set task stasus
            task_to_add["status"] = False

            #add task
            tasks.append(task_to_add)
            print("\nYour task was successfully added\n")

      #remtask command logic
      elif command == "remtask":

            deletable_tasks = [task.get("name") for task in tasks if not task.get("status")]

            if not deletable_tasks:
                  print("There are currently no tasks in the system to delete\n")
                  print()
                  continue

            else:
                  print("\nCurrent pending tasks in system (You can only delete unfinished tasks)\n:")
                  for task in deletable_tasks:
                        print(task)

            task_to_delete = input("\nEnter the name of the task which you wish to delete: ").strip().lower()

            if not task_to_delete in deletable_tasks:
                  print("No such pending task exists\n")
                  continue

            else:
                  for task in tasks:
                        if task.get("name") == task_to_delete:
                              tasks.remove(task)
                              break
                  print("\nThe task was successfully deleted\n")

      #checktask command logicd
      elif command == "checktask":

            checkable_tasks = [task.get("name") for task in tasks if not task.get("status")]


            if  not checkable_tasks:
                print("There are no unfinished tasks as of now:")
                print()
                continue

            print("\nHere are your unfinished tasks: ")

            for task in checkable_tasks:
                  print(task)

            task_to_check = input("\nEnter the name of the task which you wish to check complete: ").strip().lower()

            if not task_to_check in checkable_tasks:
                  print("\nThe task you entered can't be marked complete")
                  continue

            else:
                  for task in tasks:
                        if task.get("name") == task_to_check:
                              task["status"] = True
                              print("\nThe task was successfully checked complete\n")
                              break


      #taskscomp command logic
      elif command == "taskscomp":
            tasks_by_status(tasks, True, "Completed")
      #taskuncomp command logic
      elif command == "tasksuncomp":
            tasks_by_status(tasks, False, "Uncompleted")
      #searchtask command logic
      elif command == "searchtask":

            if not tasks:
                print("You currently have no tasks yet\n")
                continue

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
                  print("No such task of that name exists.\nPlease use the 'alltasks' command to view the tasks saved in your session")
                  continue

            print()

      #alltasks command logic
      elif command == "alltasks":

            if not tasks:
                  print("\nNo tasks exist yet\n")
                  continue

            print("\nAll Tasks:")
            counter = 1
            for task in tasks:
                  print(f"{counter}. {task.get("name")}: ", end = "")
                  if task.get("status"):
                        print("Completed")
                  else:
                        print("Unfinished")
                  counter += 1

            print()

      #addplayers command logic
      elif command == "addplayers":
            add_items(players, "player", "players")

      #remplayers command logic
      elif command == "remplayers":
            remove_items(players, "player", "players")

      elif command == "listplayers":
            list_items(players, "players")

      elif command == "addcategories":
            add_items(categories, "category", "categories")

      elif command == "remcategories":
            remove_items(categories, "category", "categories", "default")

      elif command == "listcategories":
            list_items(categories, "categories")

      elif command == "addlocations":
            add_items(locations, "location", "locations")

      elif command == "remlocations":
            remove_items(locations, "location", "locations")

      elif command == "listlocations":
            list_items(locations, "locations")

      elif command == "help":
            help_message()

      elif command == "allstatus":
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
                  continue

            else:
                  tasks_by_status(tasks, True, "Completed")
                  tasks_by_status(tasks, False, "Uncompleted")

      else:
           print("Unkown Command\n")
           continue