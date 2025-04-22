import json 

priorities: dict = {
    "high": [],
    "normal": [],
    "low": []
}

errorColor: str = "\033[31m"
warningColor: str = "\033[0;33m"
ansiReset: str = "\033[0m"

def AddItemToList(p_key: str, p_taskName: str) -> None:
    priorities[p_key].append(p_taskName)


def RemoveItemFromList(p_key: str) -> None:
        userOption = int(input("What number task would you like to delete?: "))
        priorities[p_key].pop(userOption - 1)


def DisplayList(p_key: str, p_priority: str) -> None:
    if priorities[p_key]:
        counter = 1
        print(f"---- {p_priority} Priority ----")
        for task in priorities[p_key]:
            print(f"{counter}. {task}")
            counter +=1


def AddTask() -> None:
    isRunning = True
    while isRunning:
        userConfirm = True

        taskName = input("Input a task you'd like to put on your to-do list: ")
        taskPriority = input("Input the priority for the task:\n"
                             "[N]ormal\n"
                             "[H]igh\n"
                             "[L]ow\n").lower().strip()
        
        try:
            if taskPriority[0] == 'n':
                AddItemToList("normal", taskName)
            elif taskPriority[0] == 'h':
                AddItemToList("high", taskName)
            elif taskPriority[0] == "l": 
                AddItemToList("low", taskName)
            else:
                print(f"{errorColor}Invalid character: Please try again!{ansiReset}")
        except IndexError:
            print(f"{errorColor}Error: Can't process empty input, Try again!{ansiReset}")
            userConfirm = False

        while userConfirm:
            userInput = input("Do you want to create another task? [y/n] ").lower().strip()
            
            if userInput[0] == 'y':
                break
            elif userInput[0] == 'n': 
                isRunning = False
                break
            else:
                print(f"{errorColor}Invalid Input, please type [Y]es or [N]o{ansiReset}")


def DisplayTask() -> None:
    
    DisplayList("high", "High")
    DisplayList("normal", "Normal")
    DisplayList("low", "Low")
        
    if not priorities["high"] and not priorities["normal"] and not priorities["low"]:
        print(f"\n{warningColor}List is empty!{ansiReset}\n")


def DeleteTask() -> None:
    isRunning = True
    while isRunning:
        userConfirm = True

        DisplayTask()
        userOption = input("What category priority is your task you's like to delete?\n"
                           "[H]igh\n"
                           "[N]ormal\n" 
                           "[L]ow\n").lower().strip()

        try:
            if userOption[0] == 'h':
                RemoveItemFromList("high")
            elif userOption[0] == 'n':
                RemoveItemFromList("normal")
            elif userOption[0] == 'l':
                RemoveItemFromList("low")
            elif userOption[0] == 'q':
                break
            else:
                print(f"{errorColor}Invalid character!{ansiReset}")
        except IndexError:
            print(f"{errorColor}Error: Can't process empty input, Try again!{ansiReset}")
            userConfirm = False

        while userConfirm:
            userInput = input("Do you want to remove another task? [y/n] ").lower().strip()
            
            if userInput[0] == 'y':
                break
            elif userInput[0] == 'n': 
                isRunning = False
                break
            else:
                print(f"{errorColor}Invalid Input, please type [Y]es or [N]o{ansiReset}")


def UserMenu() -> str:
    userOption = input("\nWelcome to your todo list!\n Would you like to:\n"
                       "[A]dd a task\n"
                       "[S]how task\n" 
                       "[D]elete Task\n" 
                       "[Q]uit\n").lower().strip()
    return userOption[0]


def SaveTaskJson() -> None:
    with open("data.json", "w") as file:
        json.dump(priorities, file, indent=4)


def LoadTaskListJson() -> dict:
    with open("data.json", "r") as file:
        priorities = json.load(file)
        return priorities


try:
    priorities = LoadTaskListJson()
except FileNotFoundError:
    enterToContinue = input(f"{warningColor}No save data found, press enter to continue...{ansiReset}")


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
            print(f"{errorColor}Invalid character: please try again!{ansiReset}")
    except IndexError:
        print(f"{errorColor}Error: Can't process empty input, Try again!{ansiReset}")
