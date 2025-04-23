import json 

# ANSI color ease of use variables
errorColor: str = "\033[31m"
warningColor: str = "\033[0;33m"
ansiReset: str = "\033[0m"


# Adds an item to specified list
def AddItemToList(p_key: str, p_taskName: str, p_masterList: dict) -> None:
    p_masterList[p_key].append(p_taskName)


# Removes an item from the specified list
def RemoveItemFromList(p_key: str, p_masterList: dict) -> None:
        userOption = int(input("What number task would you like to delete?: "))
        p_masterList[p_key].pop(userOption - 1)


# Displays and Enumerates specific list
def DisplayList(p_key: str, p_priority: str, p_masterList: dict) -> None:
    if p_masterList[p_key]:
        counter = 1
        print(f"---- {p_priority} Priority ----")
        for task in p_masterList[p_key]:
            print(f"{counter}. {task}")
            counter +=1


# Addition logic that runs to add to certain list
def AddTask(p_masterList: dict) -> None:
    isRunning = True
    while isRunning:
        userConfirm = True

        taskName = input("Input a task you'd like to put on your to-do list: ")
        taskPriority = input("Input the priority for the task:\n"
                             "[N]ormal\n"
                             "[H]igh\n"
                             "[L]ow\n").lower().strip()
        
        try:
            match taskPriority[0]:
                case "h":
                    AddItemToList("high", taskName, p_masterList)
                case "n":
                    AddItemToList("normal", taskName, p_masterList)
                case "l":
                    AddItemToList("low", taskName, p_masterList)
                case _: 
                    print(f"{errorColor}Invalid character: Please try again!{ansiReset}")
        except IndexError:
            print(f"{errorColor}Error: Can't process empty input, Try again!{ansiReset}")
            userConfirm = False

        while userConfirm:
            userInput = input("Do you want to create another task? [y/n] ").lower().strip()

            match userInput[0]:
                case "y":
                    break
                case "n":
                    isRunning = False
                    break
                case _:
                    print(f"{errorColor}Invalid Input, Please type [Y]es or [N]o")
            

# Displays all the list to the user (If they aren't empty)           
def DisplayTask(p_masterList: dict) -> None:
    
    DisplayList("high", "High", p_masterList)
    DisplayList("normal", "Normal", p_masterList)
    DisplayList("low", "Low", p_masterList)
        
    if not p_masterList["high"] and not p_masterList["normal"] and not p_masterList["low"]:
        print(f"\n{warningColor}List is empty!{ansiReset}\n")


# Logic that runs to delete to certain list
def DeleteTask(p_masterList: dict) -> None:
    isRunning = True
    while isRunning:
        userConfirm = True

        DisplayTask(p_masterList)
        userOption = input("What category priority is your task you's like to delete?\n"
                           "[H]igh\n"
                           "[N]ormal\n" 
                           "[L]ow\n").lower().strip()
        
        try: 
            match userOption[0]:
                case "h":
                    RemoveItemFromList("high")
                case "n":
                    RemoveItemFromList("normal")
                case "l":
                    RemoveItemFromList("low")
                case "q":
                    break
                case _:
                    print(f"{errorColor}Invalid Character!{ansiReset}")
        except IndexError:
            print(f"{errorColor}Error: Can't process empty input, Try again!{ansiReset}")
            userConfirm = False

        while userConfirm:
            userInput = input("Do you want to remove another task? [y/n] ").lower().strip()
            
            match userInput[0]:
                case "y":
                    break
                case "n":
                    isRunning = False
                    break
                case _:
                    print(f"{errorColor}Invalid Input, Please type [Y]es or [N]o")


# The user menu seperated into a function
def UserMenu() -> str:
    userOption = input("\nWelcome to your todo list!\n Would you like to:\n"
                       "[A]dd a task\n"
                       "[S]how task\n" 
                       "[D]elete Task\n" 
                       "[Q]uit\n").lower().strip()
    return userOption[0]


# The save function
def SaveTaskJson(p_masterList) -> None:
    with open("data.json", "w") as file:
        json.dump(p_masterList, file, indent=4)


# Loads the list if the user has used app before
def LoadTaskListJson() -> dict:
    with open("data.json", "r") as file:
        masterList = json.load(file)
        return masterList


# Main function
def main() -> None:
    try:
        masterList: dict = LoadTaskListJson() 
    except FileNotFoundError:
        input(f"{warningColor}No save data found, press enter to continue...{ansiReset}")
        
        masterList: dict = {
            "high": [],
            "normal": [],
            "low": []
        }

    while True:
        userOption: str = UserMenu()

        try:
            match userOption[0]:
                case "a":
                    AddTask(masterList)
                case "s":
                    DisplayTask(masterList)
                case "d":
                    DeleteTask(masterList)
                case "q":
                    SaveTaskJson(masterList)
                    break
                case _:
                    print(f"{errorColor}Invalid character: please try again!{ansiReset}")
        except IndexError:
            print(f"{errorColor}Error: Can't process empty input, Try again!{ansiReset}")

main()
