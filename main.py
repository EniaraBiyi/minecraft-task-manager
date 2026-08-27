#Data Structures:
tasks = []
players = []
locations = []
categories = ["Default"]

#Welcome Message and tutorial
print("Welcome to the Minecraft Task Manager!!!\n"
      "No more shall you struggle with your in-game administrative tasks. You can centralize your workflow here\n\n"
      "The system manages all your TASKS. Tasks are the work you need to get done in them. They can have associated\n"
      "PLAYERS, designated LOCATIONS, and belong to a CATEGORY, all of which you predetermine. A task must not strictly\n"
      "have assigned players or a location, and belongs to a built-in default category if you do not assign one. All\n"
      "tasks are marked as either completed or uncompleted.\n"
      "Let's familiarise you with the system's command:\n\n"
      "Tasks:\n"
      "addtask: add a new task\n"
      "remtask: delete a task\n"
      "checktask: mark a task as complete\n"
      "taskscomp: view completed tasks\n"
      "tasksuncomp: view uncompleted tasks\n"
      "searchtask: find a specific task\n\n"
      "Players:\n"
      "addplayer: add a player to the system\n"
      "remplayer: remove a player from the system\n"
      "listplayers: view all players\n\n"
      "Categories:\n"
      "addcategory: add a task category\n"
      "remcategory: delete a task category\n"
      "listcategories: view all task categories\n\n"
      "Locations:\n"
      "addlocation: add a named location (eg Basecamp, Sugarcane Farm)\n"
      "remlocation: remove a location\n"
      "listlocations: view all locations\n\n"
      "System/Meta\n"
      "help: pull up the user manual you are currently reading\n"
      "allstatus: to view all tasks, players, locations, categories\n"
      "exit: end your work session\n")

#Session setup
#Adding players
print("First, let's add players to your system: ")
print("Enter players, or press Enter to finish:")
while True:
      player = input()
      if player:
            if player in players:
                  print("You already entered this player")
                  continue
            players.append(player)
      else:
            print("These are the players you have entered: ")
            if len(players) == 0:
                  print("No player was entered")
            for player in players:
                  print(player)
            break

#Adding location
print("\nNext, let's add locations: ")
print("Enter locations, or press Enter to finish:")
while True:
      location = input()
      if location:
            if location in locations:
                  print("You already entered this location")
                  continue
            locations.append(location)
      else:
            print("These are the locations you have entered: ")
            if len(locations) == 0:
                  print("No location was entered")
            for location in locations:
                  print(location)
            break

#Adding Categories
print("\nFinally, let's add categories, that'll help group similar tasks together\n"
      "(Note that there is already a Default category for tasks that don't have a specific category assigned): ")
print("Enter categories, or press Enter to finish")
while True:
      category = input()
      if category:
            if category in categories:
                  print("You already entered this category")
            categories.append(category)
      else:
            print("These are the categories you have entered (Default is built-in): ")
            if len(categories) == 0:
                  print("No category was entered")
            for category in categories:
                  print(category)
            break


print("\nGreat, you should be all set up now.\n"
      "Now you have full accesss to the programs features and can enter commands at will. Enjoy : )\n")


#Command processor
while True:
      command = input("Enter command")

      if command == "exit":
           break

      #addtask command logic
      elif command == "addtask":
            task = { }

            task_name = ""
            task_players = []
            task_locations = []
            task_category = ""

            #obtain task name
            print("Enter inputs for the prompts accordingly. Press Enter without input to skip or continue")
            while True:
                  task_name = input("Enter task name: ")

                  if not task_name or task_name.isspace():
                        print("You must enter a valid task name")

                  else:
                        task["name"] = task_name
                        break

            print("Enter players assigned to the task:")
            while True:
                  task_player = input()

                  if not task_player:
                        task["players"] = task_players
                        break

                  elif task_player not in players:
                        print("The player entered has not yet been saved in the system. Please enter a valid location")

                  elif task_player in task_players:
                        print("That player has already been assigned to this task")

                  else:
                        task_players.append(task_player)

            print("Enter location(s) for the task: ")
            while True:
                  task_location = input()

                  if not task_location:
                        task["location"] = task_locations
                        break

                  elif task_location not in locations:
                        print("The location entered has not yet been saved in the system. Please enter a valid location")

                  elif task_location in task_locations:
                        print("That location has already been assigned to this task")

                  else:
                        task_locations.append(task_location)

            while True:
                  task_category = input("Enter the category for this task. Press Enter to put task in to Default category: ")

                  if not task_category:
                        task["category"] = "Default"
                        break

                  elif task_category not in categories:
                        print("The category entered has not yet been saved in the system. Please enter a valid category")

                  else:
                        task["category"] = task_category
                        break

            task["status"] = False
            tasks.append(task)
            print("Execution complete. You may now enter another command")
      else:
            print("Unkown Command")

print(tasks)