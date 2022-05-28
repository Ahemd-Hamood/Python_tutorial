command = ""
car_started = False

while True:
    command = input("> ")
    if command.lower() == "help":
        print("start - to start the car \nstop - to stop the car \nquit - to exit")
    elif command.lower() == "start":
        if car_started:
            print("Car already started...")
        else:
            car_started = True
            print("Car started.... Ready to go!")
    elif command.lower() == "stop":
        if not car_started:
            print("you need to start the car first")
        else:
            car_started = False
            print("Car stopped")
    elif command.lower() == "quit":
        break
    else:
        print("I can't understand")

# output:
# > help
# start - to start the car
# stop - to stop the car
# quit - to exit
# > stop
# you need to start the car first
# > start
# Car started.... Ready to go!
# > start
# Car already started...
# > stop
# Car stopped
# > quit