# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 4
# Date: 9/28/2022
# Created date: 9/28/2022


# Imported Libraries
import string

# Function List


def get_school(idnum: str) -> str:

    if idnum[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif idnum[5] == '2':
        return 'School of Law'
    elif idnum[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'


def get_grade(idnum: str) -> str:
    if idnum[6] == '1':
        return "Freshman"
    elif idnum[6] == '2':
        return "Sophomore"
    elif idnum[6] == '3':
        return "Junior"
    elif idnum[6] == '4':
        return "Senior"
    elif idnum[6] == '5':
        return "Invalid Grade"


def character_value(char: str) -> int:
    return string.ascii_uppercase.index(char)


def get_check_digit(idnum: str) -> int:
    total = 0
    for i in range(0, 5):
        total += ((i + 1) * character_value(idnum[i]))
    for i in range(5, 10):
        total += ((i + 1) * int(idnum[i]))
    return total % 10


def verify_check_digit(idnum: str) -> tuple:

    if len(idnum) != 10:
        return False, "The length of the number given must be 10"
    elif not idnum[0:5].isalpha():
        for i in range(0, 5):
            if not idnum[i].isalpha():
                return False, 'The first 5 characters must be A-Z, the invalid character is at {} is {}'.format(idnum[i], i)
    elif not idnum[7:10].isdigit():
        for i in range(7, 10):
            if not idnum[i].isdigit():
                return False, 'The last three characters must be 0-9, the invalid character is at {} is {}'.format(idnum[i], i)
    elif idnum[5] != '1' and idnum[5] != '2' and idnum[5] != '3':
        return False, 'The sixth character must be 1 2 or 3'
    elif idnum[6] != '1' and idnum[6] != '2' and idnum[6] != '3' and idnum[6] != '4':
        return False, 'The seventh character must be 1 2 3 or 4'
    elif int(idnum[9]) != get_check_digit(idnum):
        return False, 'Check Digit {} does not match calculated value {}'.format(idnum[9], get_check_digit(idnum))
    else:
        return True, ''


if __name__ == "__main__":
    print("{:^50}".format("Linda Hall"))
    print("{:^50}".format("Library Card Check"))
    print("=" * 50)

    while True:
        id_num = input("Enter Library Card Number:\n").upper().strip()
        if id_num == "":
            break
        result, error = verify_check_digit(id_num)

        if result:
            print("Library card is valid.")
            print("The card belongs to a student in {}.".format(get_school(id_num)))
            print("The card belongs to a {}.".format(get_grade(id_num)))
        else:
            print("Library card is invalid.")
            print(error)


