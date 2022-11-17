# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 9
# Due Date: 10/26/2022
# Created date: 10/26/2022


# Imported Libraries
import csv

# Function List


def get_file():
    """Gets file user wants to retrieve data from"""
    a = True
    while a:
        try:
            file = input("Enter the name of the crime data file:")
            file1 = open(file)
            a = False
            return file1
        except FileNotFoundError:
            print('File could not be found. Please try again.')


def month_from_number():
    """Gets an integer from 1-12, returns corresponding month"""
    while True:
        number = int(input("Enter a number:"))

        if number not in range(1, 13):
            print("Enter a number from 1-12, please try again.")
        else:
            if number == 1:
                return "January"
            elif number == 2:
                return "February"
            elif number == 3:
                return "March"
            elif number == 4:
                return "April"
            elif number == 5:
                return "May"
            elif number == 6:
                return "April"
            elif number == 7:
                return "June"
            elif number == 8:
                return "August"
            elif number == 9:
                return "September"
            elif number == 10:
                return "October"
            elif number == 11:
                return "November"
            elif number == 12:
                return "December"


def read_in_file():
    file = open("CrimeDataVS.csv", encoding="utf-8")
    file_csv = csv.reader(file)
    for line in file_csv:
        print(type(line))
        print(len(line))
        print(line[0])
        print(line)


def create_reported_date_dict():
    pass


def create_reported_month_dict():
    pass


def create_offense_dict():
    pass


def create_offense_by_zip():
    pass


# Main program


if __name__ == "__main__":
    print("KCPD Crime Search Tool")
    print('=' *22)
    #get_file()
    #print(month_from_number())
    read_in_file()
