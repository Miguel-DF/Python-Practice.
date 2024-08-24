# Python quiz Game


# this is the  question data type
questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the human body?:",
            "Which planet in the solary system is the hottest?: ")
# this is the answer choices data type
optiions = (("A. 116","B. 117","C. 118","D. 119"),
            ("A. While","B. Crocodile","C. Elephant","D. Ostrich"),
            ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
            ("A. 206","B. 207","C. 208","D. 209"),
            ("A. Mercry","B. Venus","C. Earth","D. Mars"))


# this is the Correct answer of question data
answers = ("C","D","A","A","B")

# this is the guesses data type restore user guess
guesses = []
# this is the score data type of user
score = 0
# this is the question number data type of choices
question_num = 0

#loop for question
for question in questions:
    print("-----------------------")
    print(question)
    #loop for options choices
    for option in optiions[question_num]:
        print(option)
    # this data variable can restore of user inputed
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    # if case for user guess if correct or inccorect
    if guess == answers[question_num]:
        score += 1 # the score will be add 1 if correct
        print("Correct")
    else:
        print("Incoorect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------------")
print("        Result         ")
print("-----------------------")

# for loop for display  answer
print("Answers:", end="")
for answer in answers:
    print(answer, end="")
print()
#for loop for display user answer choices
print("Guesses:", end="")
for guess in guesses:
    print(guess, end="")
print()

# print total score of users
score = int(score/ len(questions) * 100)
print(f"Your score is: {score}%")
