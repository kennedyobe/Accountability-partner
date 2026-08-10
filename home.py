import goaltrays
#menu
while True:
    request = int (input(
        'hello, what would you like to do? ' \
    '\n 1: create a new goal?' \
    ' \n 2: check your goal list?'
     '\n 3: progress'
    ' \n 4: Exit '))
    if request == int(1):
        goaltrays.creategoaltray()
    elif request == int(2):
        goaltrays.goallist()
    elif request == int(3):
        goaltrays.goalprogress()
    elif request == 4:
        break
    else:
        print('incorrect request')
    stopprogram = input ('thank you! try another thing? y/n?')
    if stopprogram == 'y':
        pass
    elif stopprogram == 'n':
        break
    else:
        print('incorrect input')
        


