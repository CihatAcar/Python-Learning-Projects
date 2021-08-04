command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started.. Ready to go!")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print("Car stopped!")
    elif command == "help":
        print("""
I do not understand that!
for start = Type "Start"
for stop = Type "Stop"
for quit = Type "Quit"
for help = Type  "Help"
""")
    elif command == "quit":
        break
    else:
        print("I am sorry.. I do not understand!")