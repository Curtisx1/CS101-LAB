# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 8
# Date: 10/19/2022
# Created date: 10/19/2022


# Imported Libraries
import math

# Function List


def mean(x):
    if len(x) == 0:
        return 0
    else:
        total = 0.0
    for i in x:
        total += i
    return total/len(x)


def std(_mean, x):
    square_root = 0.0
    for i in x:
        square_root += (i - _mean)**2
    return (square_root/len(x))**0.5


def menu_tests(test, assignment):
    number_tests = len(test)
    num_assign = len(assignment)
    weighted = 0.0
    print("Type # min max avg std")
    print("====================================================== ")
    if number_tests == 0:
        test_min = "n/a"
        test_max = "n/a"
        test_avg = "n/a"
        test_std = "n/a"
        print("Tests 0 n/a n/a n/a n/a")
    else:
        test_min = min(test)
        test_max = max(test)
        test_avg = mean(test)
        test_std = std(test_avg, test)
        weighted += test_avg*0.6
        print("Tests %d %.2f %.2f %.2f %.2f"%(number_tests, test_min, test_max, test_avg, test_std))

    if num_assign == 0:
        assignment_min = "n/a"
        assignment_max = "n/a"
        assignment_avg = "n/a"
        assignment_std = "n/a"
        print("Programs 0 n/a n/a n/a n/a")
    else:
        assignment_min = min(assignment)
        assignment_max = max(assignment)
        assignment_avg = mean(assignment)
        assignment_std = std(assignment_avg, assignment)
        weighted += assignment_avg*0.4
        print("Programs %d %.2f %.2f %.2f %.2f"%(num_assign, assignment_min, assignment_max, assignment_avg, assignment_std))
        print("The weighted scores is %.2f", weighted)


def main_program():
    test_scores = []
    assignment_scores = []
    while True:
        print(" Grade Menu")
        print("1 - Add Test")
        print("2 - Remove Test")
        print("3 - Clear Tests")
        print("4 - Add Assignment")
        print("5 - Remove Assignment")
        print("6 - Clear Assignments")
        print("D - Display Scores")
        print("Q - Quit")
        user_choice = (input("==> "))
        if user_choice == '1':
            test_temp = float(input("Enter the new Test score 0-100 ==> "))
            while test_temp < 0:
                test_temp = float(input("Enter the new Test score 0-100 ==> "))
                test_scores.append(test_temp)
        elif user_choice == '2':
            test_remove = float(input("Enter the Test to remove 0-100 ==> "))
            removed_element = False
            for i in test_scores:
                if i == test_remove:
                    test_scores.remove(test_remove)
                    removed_element = True
                if not removed_element:
                    print("Could not find that score to remove")
        elif user_choice == '3':
                test_scores.clear()
        elif user_choice == '4':
            test_temp = float(input("Enter the new Assignment score 0-100 ==> "))
            while test_temp < 0:
                test_temp = float(input("Enter the new Assignment score 0-100 ==> "))
                assignment_scores.append(test_temp)
        elif user_choice == '5':
            test_temp = float(input("Enter the Assignment to remove 0-100 ==> "))
            removed_element = False
            for i in assignment_scores:
                if i == test_temp:
                    assignment_scores.remove(test_temp)
                    removed_element = True
                if not removed_element:
                    print("Could not find that score to remove")
        elif user_choice == '6':
            assignment_scores.clear()
        elif user_choice == 'D' or user_choice == 'd':
            menu_tests(test_scores, assignment_scores)
        elif user_choice == 'Q' or user_choice == 'q':
            break
        else:
            print("Please choose correct option.")

main()

