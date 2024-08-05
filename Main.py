import random

exit = False
user_points = 0
computer_point = 0

while exit == False:

    options = ["rock", "paper", "scissors"]
    user_input = input("Can you beat a computer? Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options).lower()

    if user_input == "exit":
        print("Game ended")
        exit = True
    if user_input == "rock":
        if computer_input == "rock":
            print("Computer: rock")
            print("Tie")
        elif computer_input == "paper":
            print("Computer: paper")
            print("Computer wins! :)")
            computer_point += 1
        elif computer_input == "scissors":
            print("Computer: scissors")
            print("You win!")
            user_points += 1
    elif user_input == "paper":
        if computer_input == "paper":
            print("Computer: paper")
            print("Tie")
        elif computer_input == "rock":
            print("Computer: rock")
            print("You win!")
            user_points += 1
        elif computer_input == "scissors":
            print("Computer: scissors")
            print("Computer wins!")
            computer_point += 1
    elif user_input == "scissors":
        if computer_input == "paper":
            print("Computer: paper")
            print("You win!")
            user_points += 1
        elif computer_input == "rock":
            print("Computer: rock")
            print("Computer wins!")
            computer_point += 1
        elif computer_input == "scissors":
            print("Computer: scissors")
            print("Tie")

    elif user_input != "rock" or "paper" or "scissors":
        print("Invalid choice")