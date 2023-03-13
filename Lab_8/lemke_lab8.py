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


def grade_menu(test, assignment):
    number_tests = int(len(test))
    num_assign = int(len(assignment))
    weighted = 0.0
    print("Type   #   min   max   avg   std")
    print('=' * 15)
    if number_tests == 0:
        test_min = 'N/A'
        test_max = 'N/A'
        test_avg = 'N/A'
        test_std = 'N/A'
        print(f'Tests {test_min:.2f} {test_max:.2f} {test_avg:.2f} {test_std:.2f}\n')
    else:
        test_min = min(test)
        test_max = max(test)
        test_avg = mean(test)
        test_std = std(test_avg, test)
        weighted += test_avg * 0.6
        print(f'Tests {number_tests} {test_min:.2f} {test_max:.2f} {test_avg:.2f} {test_std:.2f}\n')
        print(f'The weighted scores is {weighted:.2f}')

    if num_assign == 0:
        assignment_min = 'N/A'
        assignment_max = 'N/A'
        assignment_avg = 'N/A'
        assignment_std = 'N/A'
        print(f'Programs {assignment_min} {assignment_max} {assignment_avg} {assignment_std}\n')
    else:
        assignment_min = min(assignment)
        assignment_max = max(assignment)
        assignment_avg = mean(assignment)
        assignment_std = std(assignment_avg, assignment)
        weighted += assignment_avg * 0.4
        print(f'Programs {num_assign} {assignment_min:.2f} {assignment_max:.2f} {assignment_avg:.2f} {assignment_std:.2f}\n')
        print(f'The weighted scores is {weighted:.2f}')


def main_program():
    test_scores = []
    assignment_scores = []
    while True:
        print(
            "Grade Menu\n"
            "===========\n"
            "1 - Add Test\n"
            "2 - Remove Test\n"
            "3 - Clear Tests\n"
            "4 - Add Assignment\n"
            "5 - Remove Assignment\n"
            "6 - Clear Assignments\n"
            "7 - Display scores\n"
            "8 - Quit"
        )
        user_choice = float(input("Please enter your choice:"))
        if user_choice == 1:
            test_temp = float(input("Enter a new test score 0-100:"))
            while test_temp < 0:
                test_temp = float(input("Enter a new test score 0-100:"))
            test_scores.append(test_temp)
        elif user_choice == 2:
            test_remove = float(input("Enter the Test to remove 0-100:"))
            removed_element = False
            for i in test_scores:
                if i == test_remove:
                    test_scores.remove(test_remove)
                    removed_element = True
            if not removed_element:
                print("Could not find that score to remove.")
        elif user_choice == 3:
            test_scores.clear()
        elif user_choice == 4:
            test_temp = float(input("Enter the new Assignment score 0-100:"))
            while test_temp < 0:
                test_temp = float(input("Enter the new Assignment score 0-100:"))
            assignment_scores.append(test_temp)
        elif user_choice == 5:
            test_temp = float(input("Enter the Assignment to remove 0-100:"))
            removed_element = False
            for i in assignment_scores:
                if i == test_temp:
                    assignment_scores.remove(test_temp)
                    removed_element = True
            if not removed_element:
                print("Could not find that score to remove.")
        elif user_choice == 6:
            assignment_scores.clear()
        elif user_choice == 7:
            grade_menu(test_scores, assignment_scores)
        elif user_choice == 8:
            break
        else:
            print("Please choose correct option.")

# Main program


if __name__ == "__main__":
    main_program()

