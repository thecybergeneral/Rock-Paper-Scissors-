import random

Choice = ["R", "P", "S"]

print("Let The Game Begin.")


def game():
    User = input("Make your choice(Type R, P or S): ")
    while User not in ["R", "S", "P"]:
        print(f"\nYou typed '{User}' which isn't a valid choice")
        game()
        break

    else:
        CPU = random.choice(Choice)

        print(f"\nPlayer({User}) : CPU({CPU})\n")

        if User == CPU:
            print(f"\n Both players selected {User}. It's a tie!.")
            game()
        elif User == "P" and CPU == "S":

            print("CPU wins")
        elif User == "R" and CPU == "P":

            print("CPU wins")
        elif User == "S" and CPU == "P":

            print("User wins")
        elif User == "P" and CPU == "R":

            print("User wins")
        elif User == "R" and CPU == "S":

            print("User wins")
        elif User == "S" and CPU == "R":

            print("CPU wins")


game()
