''' piRover Keyboard - this is the keyboard user interface 
for the rover system.
'''

def help():
    print("Please enter one of the following commands.")
    print("W for forward")
    print("X for backward")
    print("A for left turn")
    print("AA for left rotate")
    print("D for right turn")
    print("DD for right rotate")
    # continue this on your own



def main():
    print("This is the keyboard interface for my rover")
    print("Enter a valid command and press Enter.")
    print("Enter h for help and Q for quit.")
    print()

    while True:
        user_input = input("Command: ")
        command = user_input.upper()
        if command == "Q":
            break
        elif command == "H":    
            help()
        elif command  == "W":
            print("Rover is moving forward")
        # continue on your own
        else:
            print("Invalid command!")    



if __name__ == "__main__":
    main()