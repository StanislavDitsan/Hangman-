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
