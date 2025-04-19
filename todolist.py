# Todo list
# Requirements: Add/View/Delete Task - Add priority to list
highPriorityList = []
normalPriorityList = []
lowPriorityList = []

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __str__(self):
        return f"{self.name}"


def AddItemToList(p_list, p_taskName, p_taskPriority):
    p_list.append(Task(p_taskName, p_taskPriority))


def RemoveItemFromList(p_list):
        userOption = int(input("What number task would you like to delete?: "))
        p_list.pop(userOption - 1)


def DisplayList(p_list, p_priority):
    if p_list:
        counter = 1
        print(f"---- {p_priority} Priority ----")
        for task in p_list:
            print(f"{counter}. {task.name}")
            counter +=1


def AddTask():
    while True:
        taskName = input("Input a task you'd like to put on your to-do list: ")
        taskPriority = input("Input the priority for the task: [N]ormal, [H]igh, [L]ow: ").lower()
        
        if taskPriority == 'n':
            AddItemToList(normalPriorityList, taskName, taskPriority)
        elif taskPriority == 'h':
            AddItemToList(highPriorityList, taskName, taskPriority)
        else: 
            AddItemToList(lowPriorityList, taskName, taskPriority)

        userInput = input("Do you want to create another task? [y/n]").lower()
        
        if userInput == 'y':
            continue
        else: 
            break


def DisplayTask():
    
    DisplayList(highPriorityList, "High")
    DisplayList(normalPriorityList, "Normal")
    DisplayList(lowPriorityList, "Low")
        
    if not lowPriorityList and not highPriorityList and not normalPriorityList:
        print("\nList is empty!")


def DeleteTask():
    while True:

        DisplayTask()
        userOption = input("What category priority is your task you's like to delete?").lower()

        if userOption == 'h':
            RemoveItemFromList(highPriorityList)
        elif userOption == 'n':
            RemoveItemFromList(normalPriorityList)
        elif userOption == 'l':
            RemoveItemFromList(lowPriorityList)
        elif userOption == 'q':
            break
        else:
            print("Invalid character!")
        

def UserMenu():
    userOption = input("\nWelcome to your todo list!\n Would you like to: \n [A]dd a task \n [S]how task \n [D]elete Task \n [Q]uit \n").lower()
    return userOption


def main():
    while True:
        userOption = UserMenu()

        try:
            if userOption == 'a':
                AddTask()
            elif userOption == 's':
                DisplayTask()
                input("\nPress enter to continue...")
            elif userOption == 'd':
                DeleteTask()
            elif userOption == 'q':
                break
            else: 
                print("Invalid character: please try again!")
        
        except ValueError:
            print("Be sure you're typing a character!")
    
main()                   
