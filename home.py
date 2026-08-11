import goaltrays
#menu
while True:
    print ('')
    request = input(
        'hello, owhat would you like to do? ' \
    '\n 1: create a new goal?' \
    ' \n 2: check your goal list?'
     '\n 3: progress'
    ' \n 4: Exit ')
    if request == '1':
        goaltrays.creategoaltray()
    elif request == '2':
        goaltrays.goallist()
    elif request == '3':
        goaltrays.goalprogress()
    elif request == '4':
        break
    else:
        print('incorrect request')
        break
              
    stopprogram = input ('thank you! try another thing? y/n?')
    if stopprogram == 'y':
        pass
    elif stopprogram == 'n':
        break
    else:
        print('incorrect input')
        


