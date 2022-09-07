import random

name = input("Enter Your Name: ")
print("Hello", name, "Welcome to Hangman Game!")
print("Try to guess the word in under ten attempts!")
print("---------------------------------------------")


wordDictionary = [
    "zombie",
    "adoption",
    "confront",
    "process",
    "establish",
    "head",
    "worth",
    "kidney",
    "mole",
    "tablet"
]


# Choose a random word

randomWord = random.choice(wordDictionary)

# Prints out dashed lines for the user to fill in the word
# using for loop

for i in randomWord:
    print("_", end=" ")


def print_hangman(wrong):
    if (wrong == 0):
        print("\n+---+")
        print("    |---+")
        print("    |---+")
        print("    |---+")
        print("   ===")
    elif (wrong == 1):
        print("\n+---+")
        print("O   |---+")
        print("    |---+")
        print("    |---+")
        print("   ===")
    elif (wrong == 2):
        print("\n+---+")
        print("O   |---+")
        print("|   |---+")
        print("    |---+")
        print("   ===")
    elif (wrong == 3):
        print("\n+---+")
        print(" O   |---+")
        print("/|   |---+")
        print("     |---+")
        print("    ===")
    elif (wrong == 4):
        print("\n+---+")
        print(" O   |---+")
        print("/|\  |---+")
        print("     |---+")
        print("    ===")
    elif (wrong == 5):
        print("\n+---+")
        print(" O   |---+")
        print("/|\  |---+")
        print("/    |---+")
        print("    ===")
    elif (wrong == 6):
        print("\n+---+")
        print(" O__||---+")
        print("/|\  |---+")
        print("/ \  |---+")
        print("    ===")


# This function is in charge of printing out the word every time the loop runs.
# Checking if character in random word is equal to any of the guessed letters
# it will print the character at every single spot.
# Else if the current character not in the guessed word,
# fill it with the blank space.

def print_word(guessed_letters):
    counter = 0
    right_letters = 0
    for character in randomWord:
        if (character in guessed_letters):
            print(randomWord[counter], end=" ")
            right_letters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return right_letters
