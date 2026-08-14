#Data Structures:
tasks = []
players = []
locations = []
categories = []

#Welcome Message and tutorial
print("Welcome to the Minecraft Task Manager!!!\n"
      "No more shall you struggle with your in-game adminsitrative tasks. You can centralize your workflow here\n\n"
      "The system manages all your TASKS. Tasks are the work you need to get done in them. They can have associated\n"
      "PLAYERS, designated LOCATIONS, and belong to a CATEGORY, all of which you predetermine. A task must not strictly\n"
      "have asigned players or a location, and belongs to a built-in default catefory if you do not assign one. All\n"
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


