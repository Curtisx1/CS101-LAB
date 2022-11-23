# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Program 4
# Due Date: 10/30/2022
# Created date: 10/29/2022


# Imported Libraries


# Function List


def main_menu():
    """Main menu for user choice. Validates user choice"""
    choice = 0
    print("1- Print Transaction ID and user name\n2- Print user name, total before and total after discount\n3- Quit")
    while choice < 1 or choice > 3:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 3:
                print("Enter valid option.")
        except ValueError:
            print("Enter valid option.")
            print("Enter your choice: ")
    return choice


def add_file_read():
    """Reads file chosen by user. Adds to a list."""
    file_name = 'input.txt'
    while True:
        user_file = input("Enter file name: ")
        if user_file.lower() == file_name:
            break
        else:
            print("Enter correct file name.")
    print("Reading data.....")

    user_data = []
    try:
        with open(file_name, 'r') as f:
            data = f.read().split('\n')
            for line in data:
                user_data.append(line)
        return user_data
    except IOError:
        print("File not found. Please try again.")


def main():
    """Main program. Outputs formatted data."""
    retry = 'y'
    while retry.lower() == 'y':
        choice = main_menu()
        if choice == 1:
            user_data = add_file_read()
            print("{:<5} {:<10} {:<10}".format('ID', 'First Name', 'Last Name'))
            print("=" *29)
            for line in user_data:
                row = line.split(" ")
                print("{:<5} {:<10} {:<10}".format(row[0], row[1], row[2]))
        elif choice == 2:
            user_data = add_file_read()
            print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10}".format('ID', 'First Name', 'Last Name', 'Before', 'After', 'Saved'))
            print("=" * 55)
            for line in user_data:
                row = line.split(" ")
                discount = float(row[3]) - float(row[3]) * 0.4
                saved = float(row[3]) - discount
                print("{:<5} {:<10} {:<10} {:<10.2f} {:<10.2f} {:<10.2f}".format(row[0], row[1], row[2], float(row[3]), discount, saved))
        elif choice == 3:
            retry = 'n'


# Main program


if __name__ == "__main__":
    main()