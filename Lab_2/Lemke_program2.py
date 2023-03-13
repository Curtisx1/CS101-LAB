# Name: Curtis Lemke
# Class: CS101 Section 3
# Program: 2
# Creation date: 9/22/2022
# Due date: 9/25/2022

# Imported modules
import random

# True or False questions
questions = [{
    "q": "I am 6\' 2\".",
    "type": "Lie"
}, {
    "q": "I am married.",
    "type": "True"
}, {
    "q": "I have been to Africa.",
    "type": "True"
}, ]

# Welcome message-Start of the program

print("Welcome To TWO TRUTHS AND A LIE!\n")
while True:
    playing = []
    correct = 0
    incorrect = 0
    # Generates Random question
    for i in range(2):
        selectedNumber = random.randint(1, 3)
        while selectedNumber in playing:
            selectedNumber = random.randint(1, 3)
        playing.append(selectedNumber)
        print("Truth or Lie??\n")
        print(questions[selectedNumber - 1]["q"])
        print()
        # Prompt for user answer
        print(f'1-Truth\n2-Lie\n')
        guess = input("Choice: ")
        # Checks user answer
        while guess in [1]:
            if questions[selectedNumber - 1]["type"] == "True":
                correct += 1
                print("Your choice is correct\n")
            else:
                incorrect += 1
                print("Your choice is incorrect\n")
        else:
            if questions[selectedNumber - 1]["type"] == "Lie":
                correct += 1
                print("Your choice is correct\n")
            else:
                incorrect += 1
                print("Your choice is incorrect\n")
                print("Number of correct choice :", correct)
                print("Number of incorrect choice :", incorrect)
    # Play again/quit
    choice = input("Do you want to play again (Y/y) (N/n): ")
    if choice in ["Y", "y"]:
        continue
    else:
        break
