# Todo list
# Requirements: Add/View/Delete Task - Add priority to list
import json 


priorities = {
    "high": [],
    "normal": [],
    "low": []
}

def AddItemToList(p_key, p_taskName):
    priorities[p_key].append(p_taskName)


def RemoveItemFromList(p_key):
        userOption = int(input("What number task would you like to delete?: "))
        priorities[p_key].pop(userOption - 1)


def DisplayList(p_key, p_priority):
    if priorities[p_key]:
        counter = 1
        print(f"---- {p_priority} Priority ----")
        for task in priorities[p_key]:
            print(f"{counter}. {task}")
            counter +=1


def AddTask():
    while True:
        taskName = input("Input a task you'd like to put on your to-do list: ")
        taskPriority = input("Input the priority for the task: [N]ormal, [H]igh, [L]ow: ").lower()
        
        if taskPriority[0] == 'n':
            AddItemToList("normal", taskName)
        elif taskPriority[0] == 'h':
            AddItemToList("high", taskName)
        else: 
            AddItemToList("low", taskName)

        userInput = input("Do you want to create another task? [y/n] ").lower()
        
        if userInput[0] == 'y':
            continue
        else: 
            break


def DisplayTask():
    
    DisplayList("high", "High")
    DisplayList("normal", "Normal")
    DisplayList("low", "Low")
        
    if not priorities["high"] and not priorities["normal"] and not priorities["low"]:
        print("\nList is empty!")


def DeleteTask():
    while True:

        DisplayTask()
        userOption = input("What category priority is your task you's like to delete?\n [H]igh\n [N]ormal\n [L]ow").lower().strip()

        if userOption[0] == 'h':
            RemoveItemFromList("high")
        elif userOption[0] == 'n':
            RemoveItemFromList("normal")
        elif userOption[0] == 'l':
            RemoveItemFromList("low")
        elif userOption[0] == 'q':
            break
        else:
            print("Invalid character!")

        userInput = input("Do you want to delete another task? [y/n] ").lower()
        
        if userInput == 'y':
            continue
        else: 
            break

        

def UserMenu():
    userOption = input("\nWelcome to your todo list!\n Would you like to: \n [A]dd a task \n [S]how task \n [D]elete Task \n [Q]uit \n").lower()
    return userOption


def SaveTaskJson():
    with open("data.json", "w") as file:
        json.dump(priorities, file, indent=4)

def LoadTaskListJson():
    with open("data.json", "r") as file:
        priorities = json.load(file)
        return priorities


try:
    priorities = LoadTaskListJson()
except FileNotFoundError:
    enterToContinue = input("No save data found, press enter to continue...")

while True:
    userOption = UserMenu()

    try:
        if userOption[0] == 'a':
            AddTask()
        elif userOption[0] == 's':
            DisplayTask()
            input("\nPress enter to continue...")
        elif userOption[0] == 'd':
            DeleteTask()
        elif userOption[0] == 'q':
            SaveTaskJson()
            break
        else: 
            print("Invalid character: please try again!")
    
    except ValueError:
        print("Be sure you're typing a character!")
