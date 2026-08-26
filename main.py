#Data Structures:
tasks = []
players = []
locations = []
categories = []

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
while True:
      print("Enter a player, or press Enter to finish:")
      player = input()
      if player:
            if player in players:
                  double_entry = input("You already entered a player of the same name\n"
                        "Are you sure you wish to proceed and enter this name again?(y/n): ")
                  while double_entry != "y" and double_entry != "n":
                              double_entry = input("Please enter y or n: ")
                  if double_entry == "n":
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
while True:
      print("Enter a location, or press Enter to finish:")
      location = input()
      if location:
            if location in locations:
                  double_entry = input("You already entered a location of the same name\n"
                        "Are you sure you wish to proceed and enter this location again?(y/n): ")
                  while double_entry != "y" and double_entry != "n":
                              double_entry = input("Please enter y or n: ")
                  if double_entry == "n":
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
print("\nFinally, let's add categories, that'll help group similar tasks together: ")
while True:
      print("Enter a category, or press Enter to finish")
      category = input()
      if category:
            if category in categories:
                  double_entry = input("You already entered a category of the same name\n"
                        "Are you sure you wish to proceed and enter this category again?(y/n): ")
                  while double_entry != "y" and double_entry != "n":
                              double_entry = input("Please enter y or n: ")
                  if double_entry == "n":
                        continue
            categories.append(category)
      else:
            print("These are the categories you have entered: ")
            if len(categories) == 0:
                  print("No category was entered")
            for category in categories:
                  print(category)
            break