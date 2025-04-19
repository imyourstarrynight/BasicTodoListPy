highPriorityList = []
normalPriorityList = []
lowPriorityList = []

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __str__(self):
        return f"{self.name}"

def AddTask():
    
    while True:
        taskName = input("Input a task you'd like to put on your to-do list: ")
        taskPriority = input("Input the priority for the task: [N]ormal, [H]igh, [L]ow: ").lower()
        
        if taskPriority == 'n':
            normalPriorityList.append(Task(taskName, taskPriority))
        elif taskPriority == 'h':
            highPriorityList.append(Task(taskName, taskPriority))
        else: 
            lowPriorityList.append(Task(taskName, taskPriority))

        userInput = input("Do you want to create another task? [y/n]").lower()
        
        if userInput == 'y':
            continue
        else: 
            break


def DisplayTask():
    print("---- High Priority ----")
    for task in highPriorityList: 
        print(task.name)

    print("---- Normal Priority ----")    
    for task in normalPriorityList: 
        print(task.name)

    print("---- Low Priority ----")
    for task in lowPriorityList: 
        print(task.name)

AddTask()
DisplayTask()
