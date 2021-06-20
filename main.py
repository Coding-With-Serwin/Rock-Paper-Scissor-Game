computer = 0
player = 0
win = False


while not win:
    var = input("Enter : Rock,Paper,Scissor :")

    if var == "Rock" or var == "rock":
        print("Computer Chooses Paper!")
        computer += 1
        print(f"You have {player} points!")
        print(f"Computer have {computer} Points!")
    
    elif var == "Paper" or var == "paper":
        print("Computer Chooses Scissor!")
        computer += 1
        print(f"You have {player} points!")
        print(f"Computer have {computer} Points!")

    elif var == "Scissor" or var == "scissor":
        print("Computer Chooses Rock!")
        computer += 1
        print(f"You have {player} points!")
        print(f"Computer have {computer} Points!")

    if computer == 3:
        print("Computer Has Won!!")
        print("Want To Play Again??")
        reply = input()
        if reply == "yes" or reply == "Yes":
            win = False

        if reply == "no" or reply == "No":
            win = True

            