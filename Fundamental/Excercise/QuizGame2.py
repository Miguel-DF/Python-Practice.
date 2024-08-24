#-----------------------------
from http.client import responses  # Importing responses from http.client module (not used in this code)


def new_game():
    # Initialize variables to keep track of guesses, correct guesses, and question number
    guesses = []
    correct_guesses = 0
    question_num = 1

    # Loop through each question in the questions dictionary
    for key in questions:
        print("#-----------------------------")
        print(key)  # Print the question
        for i in options[question_num - 1]:
            print(i)  # Print the options for the question
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()  # Convert the user's input to uppercase
        guesses.append(guess)  # Add the user's guess to the list of guesses

        # Check if the user's guess is correct and increment correct_guesses if so
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1  # Move on to the next question

    # Display the user's score and guesses
    display_score(correct_guesses, guesses)


#-----------------------------
def check_answer(answer, guess):
    # Check if the user's guess matches the correct answer
    if answer == guess:
        print("Correct!")  # Print a success message
        return 1  # Return 1 to indicate a correct guess
    else:
        print("Wrong!")  # Print an error message
        return 0  # Return 0 to indicate an incorrect guess


#-----------------------------
def display_score(correct_guesses, guesses):
    print("#-----------------------------")
    print("Results")
    print("#-----------------------------")

    # Print the correct answers
    print("Answers:", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    # Print the user's guesses
    print("Guesses:", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    # Calculate and print the user's score as a percentage
    score = int((correct_guesses / len(questions)) * 100)
    print("Your Score is: " + str(score) + "%")


#-----------------------------
def play_again():
    # Ask the user if they want to play again
    response = input("Do you want to play again?: (yes or no): ")
    response = response.upper()

    # Return True if the user wants to play again, False otherwise
    if response == "YES":
        return True
    else:
        return False


#-----------------------------

# Define the questions and options
questions = {"Who created Python?: ":"A",
             "What year was Python created?: ":"B",
             "Python is tributed to which comedy group?:":"C",
             "Is the Earth round?: ":"A"}

options = [["A. Guida van Rossum,","B. Elon Musk","C. Bill Gates","D. Mark Zuckerburg"],
           ["A. 1989","B. 1991","C. 2000","D. 2016"],
           ["A. Lonely Island","B. Smosh","C. Monty Python","D. SNL"],
           ["A. True","B. False","C. sometimes","D. What's Earth"]]

# Start the game
new_game()

# Keep playing until the user decides to quit
while play_again():
    new_game()
print("Byeeeee!")