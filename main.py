import commands as c

#Data Structures:
tasks = []
players = []
locations = []
categories = ["default"]

#Welcome Message and tutorial
print("Welcome to the Minecraft Task Manager!!!\n"
      "No more shall you struggle with your in-game administrative tasks. You can centralize your workflow here\n\n")
c.help_message()

#Session setup
print("Let's get your session all setup!\n")

#Adding players
print("First, let's add players to your system, that'll be asigned to and carry out tasks: ")
c.setup(players, "player", "players")

#Adding location
print("\nNext, let's add locations, that'll describe where players do their tasks: ")
c.setup(locations, "location", "locations")

#Adding Categories
print("\nFinally, let's add categories, that'll help group similar tasks together\n"
      "(Note that there is already a default category for tasks that don't have a specific category assigned): ")
c.setup(categories, "category", "categories", 1)

print("\nGreat, you should be all set up.\n"
      "Now you have full accesss to the programs features and can enter commands at will. Enjoy : )\n")

#Command processor
while True:
      command = input("Enter command: ").strip().lower()

      if command == "exit":
            print("\nSession Ended")
            print("Thank you for using the Minecraft Task Manager")
            break

      elif command == "addtask":
            c.addtask(tasks, players, locations, categories)

      elif command == "remtask":
            c.remtask(tasks)

      elif command == "checktask":
            c.checktask(tasks)

      elif command =="unchecktask":
            c.unchecktask(tasks)

      elif command == "taskscomp":
            c.taskscomp(tasks)

      elif command == "tasksuncomp":
            c.tasksuncomp(tasks)

      elif command == "searchtask":
            c.searchtask(tasks)

      elif command == "alltasks":
            c.alltasks(tasks)

      elif command == "addplayers":
            c.addplayers(players)

      elif command == "remplayers":
            c.remplayers(players)

      elif command == "listplayers":
            c.listplayers(players)

      elif command == "addcategories":
            c.addcategories(categories)

      elif command == "remcategories":
            c.remcategories(categories)

      elif command == "listcategories":
            c.listcategories(categories)

      elif command == "addlocations":
            c.addlocations(locations)

      elif command == "remlocations":
            c.remlocations(locations)

      elif command == "listlocations":
            c.listlocations(locations)

      elif command == "help":
            c.help_message()

      elif command == "allstatus":
            c.allstatus(tasks, players, locations, categories)

      else:
           print("Unkown Command\n")
           continue