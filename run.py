import random
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hangman Game!!")
print(ascii_banner)

# User name input - accepts only letters
name_input = ''

while True:
    name_input = input("Enter Your Name: ")

    if not name_input.isalpha():
        print('Enter only Letters!\n')
        continue
    else:
        break

print("\nHello", name_input, "\nWelcome to Hangman Game!")
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
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 1):
        print("\n+---+")
        print(" O  |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 2):
        print("\n+---+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ===")
    elif (wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif (wrong == 4):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ===")
    elif (wrong == 5):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ===")
    elif (wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")
    elif (wrong == 7):
        print("\n+---+")
        print(" O  ||")
        print("/|\  |")
        print("/ \  |")
        print("    ===")
    elif (wrong == 8):
        print("\n+---+")
        print(" O  \|")
        print("/|\  |")
        print("/ \  |")
        print("    ===")
    elif (wrong == 9):
        print("\n+---+")
        print(" O -\|")
        print("/|\  |")
        print("/ \  |")
        print("    ===")
    elif (wrong == 10):
        print("\n+---+")
        print(" O--\|")
        print("/|\  |")
        print("/ \  |")
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


# Printing underscores underneath the letters by using a return character
# and printing OVERLINE with a special character \u203E


def print_lines():
    print("\r")
    for character in randomWord:
        print("\u203E", end=" ")


# Variables to operate the game
length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while (amount_of_times_wrong != 10 and current_letters_right !=
        length_of_word_to_guess):
    print("\nLetters used so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
# Asking for the input
    letter_guessed = input("\nPlease guess a letter: ")
# If the User is right
    if (randomWord[current_guess_index] == letter_guessed):
        print_hangman(amount_of_times_wrong)
        current_guess_index += 1
        current_letters_guessed.append(letter_guessed)
        current_letters_right = print_word(current_letters_guessed)
        print("You guessed it right")
        print_lines()

# If the User is wrong
    else:
        amount_of_times_wrong += 1
        current_letters_guessed.append(letter_guessed)
        print("\nNo luck this time!\nGive it another go")
# Updates hangman drawing
        print_hangman(amount_of_times_wrong)
# Print word
        current_letters_right = print_word(current_letters_guessed)
        print_lines()

print("Game is over!")
