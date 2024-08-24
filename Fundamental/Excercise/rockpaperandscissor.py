import random
# data type for rock paper scissors
choices = ["rock", "paper", "scissors"]

# data can restore of computer, player and tie score
computer_score = 0
player_score = 0
tie_score = 0

# while loop for running the game
while True:
    computer = random.choice(choices)
    player = None

    #if case for score if who winner
    if player_score == 5:
        print("The Winner is Player")
        print("Computer Lose this game")
        break
    elif computer_score == 5:
        print("The Winner is Computer")
        print("You Lose this game")
        break

    #while if the player input not in choices
    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    # if case for logic of the game
    if player == computer:
        print("computer: ", computer)
        print("Player: ", player)
        print("tie")
        tie_score += 1 # add 1 if tie
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")
            computer_score += 1 # add 1 computer_score if computer win
        if computer == "scissors":
            print("computer: ", computer)
            print("Player: ", player)
            print("You win!")
            player_score += 1 # add 1 player_score if player win
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")
            computer_score += 1
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You win!")
            player_score += 1
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")
            computer_score += 1
        if computer == "scissors":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")
            computer_score += 1
    #ask again if you want play again for next round of rock paper and scissors
    play_again = input("Play again? (yes/no): ").lower()
    # if case for player_again if no the game will be end
    if play_again != "yes":
        break

print("Bye!")
