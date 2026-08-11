import goaltrays
#taskpoints should is a way to check progess
# a person using this app is supposed to show progress in meeting up to his goal
# for example
# i need to learn python.
# i need to finish the book so i dedicate three hours (task hours) every monday, wednesday, and friday 


# the app should be able to alert you, with a notification on that day
# you enter task mode which then does a counter of task hours while ou work on your task  
# each task mode commits points for the task. let's 9 points max per taskmode.. the 10 poins    
taskpoints = 0

def taskmode ():
    def __init__(self, taskpoints):
        self.taskpoints = taskpoints
        taskpoints = 0
    # stage 1
    # at the exact time and day, a notif will be sent  
    stage1 = input ('have you started your task?y/n ')
    if stage1 == 'y':
        taskpoints += 3
    stage2 = input ('have you started your task?y/n ')
    if stage2 == 'y':
        taskpoints += 3    
    stage3 = input ('have you started your task?y/n ')
    if stage3 == 'y':
        taskpoints += 3    
    print (taskpoints)
        
taskmode()     