command = ''
started = False

while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("The car is already started...")
        else:
            started = True
            print("car is started")
    elif command == "stop":
        if not started:
            print("The car is already stoped")
        else:
            started = False
            print("car is stoped")
    elif command == "help":
        print('''The game commands
start - to star the car
stop - to stop the car
quit - to quit the game
''')
    elif command == 'quit':
        break
    else:
        print("I don't understand your commands")
