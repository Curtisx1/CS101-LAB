# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 4
# Date: 9/28/2022
# Created date: 9/28/2022


# Imported Libraries
import string

# Function List

def get_card_number():
    number = input("Enter Library Card Number:\n")


def get_school():
    pass

def get_grade():
    pass

def character_value(char: str) -> int:
    return string.ascii_uppercase.index(char)

def get_check_digit():
    pass

def verify_check_digit(idnum: string) -> int:
    if len(idnum) != 10:
        return False, "The length of the number given must be 10."
    elif not idnum[0:5].isalpha():
        for i in range(0, 5):
            if not idnumber[i].isalpha():
                return False, 'The first 5 characters must be A-Z, the invalid character is at {} is {}'.format(
                    idnumber[i], i)
            elif not idnum[7:10].isdigit():
                for i in range(7, 10):
                    if not idnum[i].isdigit():
                        return False, 'The last three characters must be 0-9, the invalid character is at {} is {}'.format(
                            idnum[i], i)
            elif idnum[5] != '1' and idnum[5] != '2' and idnum[5] != '3':
                return False, 'The sixth character must be 1 2 or 3'
            elif idnum[6] != '1' and idnumber[6] != '2' and idnum[6] != '3' and idnum[6] != '4':
                return False, 'The seventh character must be 1 2 3 or 4'
            elif int(idnum[9]) != get_check_digit(idnum):
                return False, 'Check Digit {} does not match calculated value {}'.format(idnum[9], get_check_digit(idnum))
        else:
            return True, ''



if __name__ == "__main__":
    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("=" * 60)