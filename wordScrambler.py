import random

# function needs to have a list of 4 words
# function needs to take 1 word from list radomly
# Selected word needs to be randomized/shuffled
# Allow user to guess the original / correct word.
# IF it is correct, they ELSE they lose

# Add logic that will allow the user to make 3 guessing attempts
# and show the user the number of attempts they have

def scrambleWordGame():
    wordPool = ["Pennsylvania", "North Carolina","Congregate","Function"]
    print("Welcome to word scramble!")

    randomWordSelect = random.randint(0,3)
    correctWord = ""

    if randomWordSelect == 0:
        correctWord= wordPool[0]
    elif randomWordSelect == 1:
        correctWord= wordPool[1]
    elif randomWordSelect == 2:
        correctWord= wordPool[2]
    elif randomWordSelect == 3:
        correctWord= wordPool[3]

    convertedSelection = list(correctWord)
    random.shuffle(convertedSelection)
    scrambled = "".join(convertedSelection)
    
    for x in range(3):

        print("Guess the correct word: " + scrambled)
        userGuess = input()
        if userGuess == correctWord:
            break
        else:
            print("Sorry, that is incorrect.")



scrambleWordGame()
