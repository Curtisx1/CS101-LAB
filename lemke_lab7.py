# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 7
# Date: 10/12/2022
# Created date: 10/12/2022


# Imported Libraries


# Function List


def minimum_mpg():
    # Returns the minimum gas mileage required
    x = True
    while x:
        try:
            while x:
                mpg = int(input("Enter the minimum mpg ==> "))
                if mpg <= 0:
                    print("Fuel economy given must be greater than 0.")
                elif mpg > 100:
                    print("Fuel economy must be less than 100.")
                else:
                    x = False
                    return mpg
        except ValueError:
            print("You must enter a number for the fuel economy.")


def open_file():
    # Returns the chosen user file-repeats until valid file is selected
    x = True
    while x:
        try:
            file = input("Enter the name of the input vehicle file ==> ")
            user_file1 = open(file)
            x = False
            return user_file1
        except FileNotFoundError:
            print('Unable to open chosen file. Please try again.'.format(file))


def file_output():
    # Returns the name of the output file
    x = True
    while x:
        try:
            file = input("Enter the name of the file to output to ==> ")
            user_file1 = open(file, 'a')
            x = False
            return user_file1
        except IOError:
            print('There is an IO Error {}.'.format(file))


def user_list(my_file):
    # Creates a list with \t seperator. Outputs to user file
    file = my_file.readlines()
    new_file = []
    for i in range(len(file)):
        new_file.append(file[i].split('\t'))
    return new_file


def output_file(lst_1, mpg_1, file):
    # Returns the formatted file
    for i in range(1, len(lst_1)):
        try:
            combined = float(lst_1[i][7])
            if combined >= mpg_1:
                file.write('{:<5}{:<20}{:<40}{:>10.3f}.\n'.format(lst_1[i][0], lst_1[i][1], lst_1[i][2], combined))
        except ValueError:
            print('Could not convert value {} for vehicle {} {} {}.'.format(lst_1[i][7], lst_1[i][0], lst_1[i][1], lst_1[i][2]))


def repeat():
    # Asks the user if they want to perform another search
    choice = "x"
    while choice != 'NO' or choice != 'N' or choice != 'YES' or choice != 'Y':
        choice = input('Perform another search? ==> ')
        choice = choice.upper()
        if choice == 'YES' or choice == 'Y':
            return True
        elif choice == 'NO' or choice == 'N':
            return False
        else:
            print('You must enter Y/YES/N/NO. Please try again.')
            continue


if __name__ == "__main__":
    print("{:^60}".format("Fuel Economy Search"))
    print("=" * 60)
    x = True
    while x:
        mpg = minimum_mpg()
        infile = open_file()
        user_file = user_list(infile)
        outfile = file_output()
        output_file(user_file, mpg, outfile)
        infile.close()
        outfile.close()
        x = repeat()



