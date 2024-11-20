def newGame() :
    guesses = []
    correctGuesses = 0
    questionNum = 1

    for question in questions :
        print("----------------")
        print(question)
        for option in options[questionNum-1] :
            print(option)
        guess = input("Enter: (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correctGuesses += checkAnswer(questions.get(question),guess)
        questionNum += 1

    displayScore(correctGuesses, guesses)

def checkAnswer(answer, guess) :
    if answer == guess :
        print("Correct!")
        return 1
    else :
        print("Incorrect!")
        return 0

def displayScore(correctGuesses, guesses) :
    print("=============================")
    print("Results")
    print("=============================")

    print("Answers: ", end="")
    for question in questions :
        print(questions.get(question), end=" ")
    print()

    print("Guesses: ", end="")
    for guess in guesses :
        print(guess, end=" ")
    print()

    score = int((correctGuesses/len(questions))*100)
    print("You scored: " + str(score) + "%")

def playAgain() :
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else :
        return False

questions = {
    "Who created Python?: " : "A",
    "What year was Python created?: " : "B",
    "Python is attributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. No really its round", "D. What's Earth?"]]

newGame()

while playAgain() :
    newGame()
print("Thank you for playing!")