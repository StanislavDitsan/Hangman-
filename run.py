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