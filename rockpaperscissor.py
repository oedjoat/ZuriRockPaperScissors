from random import choice

t = ["R", "P", "S"]

computer = choice(t)

player = False

while player == False:
    player = input("R for Rock, P for Paper, S for Scissors: ")
    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("You lose! paper covers rock")
        else:
            print("You win! rock smashes paper")
    elif player == "P":
        if computer == "S":
            print("You lose! scissors cut paper")
        else:
            print("You win! paper covers scissors")
    elif player == "S":
        if computer == "R":
            print("You lose... Rock smashes scissors")
        else:
            print("You win! Scissors cut rock")
    else:
        print("That's not a valid play. Check your Input")
    player = False
    computer = choice(t)