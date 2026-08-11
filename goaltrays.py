import json
import os
filename = 'goaltray.json'

#new goal tray
def creategoaltray():
   
    goal = input('What is your goal? ')
    tasks = []
    tasknumber  = input('how many tasks will this goal need to be attained? ')
    for i in range (int(tasknumber)):
        task = input("Task name: ")
        taskpoints = 0
        duration = input("Task duration in hours: ")
        completion_time = input("date to complete: ")
        tasks.append({
        "task": task,
        "duration": duration,
        "time_to_complete": completion_time,
        'staus': 'pending',
        'taskpoints': taskpoints
        })
    newgoal = {
        'Goal': goal,
        'tasks' : tasks
        
    }    
    # open file and store in variable
    with open (filename, 'r') as file:
        goals = json.load(file)
    goals.append(newgoal)
    print(f'your goal is: {goal}')
    # update file after adding new goal 
    with open (filename, 'w') as file:
        json.dump(goals, file, indent=4)
#list of goals 
def goallist():
    with open (filename, 'r') as file:
        goals = json.load(file)
    if not goals:
        print("No goals yet.")
        return
    print("Your goals:")
    for num, value in enumerate(goals, start=1):
        a = f"{num}. {value['Goal']}"
        print(f"{num}. {value['Goal']}")
        
    return a
# track your task
def goalprogress():
    goallist()
    goal = int(input('Which goal do you want to track? Enter the number: '))
    with open(filename, 'r') as file:
        goals = json.load(file)
    value = goals[goal - 1]
    print (f"Here's a run down on '{value['Goal']}': ")
    for task in value['tasks']:
        print(task['task'])
    
             

     

    