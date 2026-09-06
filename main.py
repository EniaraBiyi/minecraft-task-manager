#Data Structures:
tasks = []
players = []
locations = []
categories = ["default"]

#Welcome Message and tutorial
print("Welcome to the Minecraft Task Manager!!!\n"
      "No more shall you struggle with your in-game administrative tasks. You can centralize your workflow here\n\n"
      "The system manages all your TASKS. Tasks are the work you need to get done. They can have associated\n"
      "PLAYERS, designated LOCATIONS, and belong to a CATEGORY, all of which you predetermine. A task must not strictly\n"
      "have assigned players or a location, and belongs to a built-in default category if you do not assign one. All\n"
      "A task can have only one name and fall under one category, but it can have multiple players and locations assigned\n"
      "tasks are marked as either completed or uncompleted.\n"
      "Let's familiarise you with the system's command:\n\n"
      "Tasks:\n"
      "addtask: add a new task\n"
      "remtask: delete an uncompleted task\n"
      "checktask: mark a task as complete\n"
      "taskscomp: view completed tasks\n"
      "tasksuncomp: view uncompleted tasks\n"
      "searchtask: find a specific task\n\n"
      "alltasks: display the names of all tasks\n"
      "Players:\n"
      "addplayers: add a player to the system\n"
      "remplayers: remove a player from the system\n"
      "listplayers: view all players\n\n"
      "Categories:\n"
      "addcategories: add a task category\n"
      "remcategories: delete a task category\n"
      "listcategories: view all task categories\n\n"
      "Locations:\n"
      "addlocations: add a named location (eg Basecamp, Sugarcane Farm)\n"
      "remlocations: remove a location\n"
      "listlocations: view all locations\n\n"
      "System/Meta\n"
      "help: pull up the user manual you are currently reading\n"
      "allstatus: to view all tasks, players, locations, categories (an overview of the whole session)\n"
      "exit: end your work session\n\n"
      "Some things you should know:\n"
      " -This program is not case sensitive\nSo 'Steve' and 'steve' are  considered the same thing\n"
      " -This program removes all leading and trailing whitespace (fancy talk for invisible characters) in your inputs")

#Session setup
print("Let's get your session all setup")
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
                  print("No player was entered")
                  break
            print("These are the players you have entered: ")
            for player in players:
                  print(player)
            break

#Adding location
print("\nNext, let's add locations: ")
print("Enter the locations you want to save, or press Enter with no input to finish:")
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
                  print("No location was entered")
                  break
            print("These are the locations you have entered: ")
            for location in locations:
                  print(location)
            break

#Adding Categories
print("\nFinally, let's add categories, that'll help group similar tasks together\n"
      "(Note that there is already a Default category for tasks that won't have a specific category assigned): ")
print("Enter categories you want to save, or press Enter without input to finish")
while True:
      category = input()
      if category:
            if category.isspace():
                  print("Please enter a valid category")
                  continue
            elif category.lower().strip() in categories:
                  print("You already entered this category")
                  continue
            categories.append(category.strip().lower())
      else:
            if len(categories) == 1:
                  print("No category was entered. Only the default one currently exists")
                  break
            print("These are the categories you have entered (default is built-in): ")
            for category in categories:
                  print(category)
            break


print("\nGreat, you should be all set up now.\n"
      "Now you have full accesss to the programs features and can enter commands at will. Enjoy : )\n")


#Command processor
while True:
      command = input("Enter command: ")

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
            print("Enter player(s) assigned to the task, or press Enter to skip:")
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
            print("Enter location(s) for the task, or press Enter to skip: ")
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
                  task_category = input("Enter the category for this task. Press Enter alone to put task in to Default category: ")

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
            print("Your task was successfully added\n")

      #remtask command logic
      elif command == "remtask":

            deletable_tasks = [task.get("name") for task in tasks if not task.get("status")]

            if len(deletable_tasks) != 0:
                  print("\nCurrent pending tasks in system:")
                  for task in deletable_tasks:
                        print(task)


            else:
                  print("There are currently no tasks in the system to delete\n")
                  continue

            task_to_delete = input("\nEnter the name of the task which you wish to delete: ").strip().lower()

            if not task_to_delete in deletable_tasks:
                  print("No such pending task exists\n")
                  continue

            else:
                  for task in tasks:
                        if task.get("name") == task_to_delete:
                              tasks.remove(task)
                              break
                  print("The task was successfully deleted\n")

      #checktask command logicd
      elif command == "checktask":

            checkable_tasks = [task.get("name") for task in tasks if not task.get("status")]

            print("\nHere are your uncompleted tasks: ")

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
                              print("The task was successfully checked\n")
                              break


      #taskscomp command logic
      elif command == "taskscomp":

            print("\nHere are your completed tasks: ")
            for task in tasks:
                  if task["status"]:
                        print(task.get("name"))
            print()

      #taskuncomp command logic
      elif command == "tasksuncomp":

            print("\nHere are your uncompleted tasks: ")
            for task in tasks:
                  if not task["status"]:
                        print(task.get("name"))
            print()

      #searchtask command logic
      elif command == "searchtask":

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
                  print("No such task exists in the system.\nPlease use the 'alltasks' command to view the tasks saved in your session")
                  continue

            print()

      #alltasks command logic
      elif command == "alltasks":

            if not tasks:
                  print("\nNo tasks exist in the system yet.")
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

      #addplayer command logic
      elif command == "addplayers":
                  print("\nEnter players, or press Enter alone to finish:")

                  counter = 0
                  while True:
                        player = input().strip().lower()

                        if player and player not in players:
                              players.append(player)
                              counter += 1
                        elif player in players:
                              print("This player is already saved to the system. Be mindful of spelling. Casing is irrelevant")
                              print("You may continue, or press Enter to finish")
                        elif not player:
                              break

                  print(f"{counter} players were added\n")

      else:
            print("Unkown Command")