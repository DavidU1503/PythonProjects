
def guessingGame ():
    print("Welcome to: The Guessing Game That's Better Than Yours!\nI'm your host Steve Harvey!!")
    secretWord = "hyper"
    guess = ""
    guessCount = 0
    guessLimit = 10
    outOfGuesses = False

    while guess != secretWord and not outOfGuesses:
        if guessCount < guessLimit:
            guess = input("Please Enter Your Enter Guess: ")
            guessCount += 1
        else:
            outOfGuesses = True

    if outOfGuesses:
        print("Out of guesses, YOU LOSE!! (insert loser music here)")
    else:
        print("\ \ \ \ \ / / / / / ")
        print("=^.^= YOU WIN! =^.^=")
        print("/ / / / / \ \ \ \ \ ")

guessingGame()
