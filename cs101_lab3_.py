# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 3
# Date: 9/14/2022
# Creation date: 9/14/2022

# Start of the program-welcome message
print("Welcome to Flarsheim Guesser!")
print("Please think of a number between and including 1 and 100.\n")

# User choice-Assigns yes or no variable to user_choice for loop-y default
user_choice = 'y'

# While loop to continue game until 'n' choice
while user_choice == 'Y' or user_choice == 'y':

# Remainder variables
    div3 = 0
    div5 = 0
    div7 = 0

# Remainder of 3 while loop
    div3 = int(input("What is the remainder when your number is divided by 3?\n"))
    while div3 < 0 or div3 >= 3:
            if div3 < 0:
                print("The value entered must be 0 or greater.\n")
            elif div3 >= 3:
                print("The value entered must be less than 3.\n")
            div3 = int(input("What is the remainder when your number is divided by 3?\n"))

# Remainder of 5 while loop
    div5 = int(input("What is the remainder when your number is divided by 5?\n"))
    while div5 < 0 or div5 >= 5:
            if div5 < 0:
                print("The value entered must be 0 or greater.\n")
            elif div5 >= 5:
                print("The value entered must be less than 5.\n")
            div5 = int(input("What is the remainder when your number is divided by 5?\n"))

# Remainder of 7 while loop
    div7 = int(input("What is the remainder when your number is divided by 7?\n"))
    while(div7 < 0 or div7 >= 7 ):
            if div7 < 0:
                print("The value entered must be 0 or greater.\n")
            elif div7 >= 7:
                print("The value entered must be less than 7.\n")
            div7 = int(input("What is the remainder when your number is divided by 7?\n"))

# For loop to guess user number
    for i in range(1, 101):
        if i % 3 == div3 and i % 5 == div5 and i % 7 == div7:
            print("Your number was",i)
            print("How amazing is that?\n")

# New choice-Game restart/end
    user_choice = input("Do you want to play again? Y to continue or N to quit: \n")
    while user_choice != 'Y' and user_choice != 'N' and user_choice != 'y' and user_choice != 'n':
        choice = input("Do you want to play again? Y to continue or N to quit: ")