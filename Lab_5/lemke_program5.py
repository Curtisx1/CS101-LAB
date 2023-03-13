# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Program 5
# Due Date: 11/20/2022
# Created date: 11/20/2022


# Imported Libraries
from datetime import date


# Functions

# Classes

class House:
    """ Displays house information and returns values on input """

    def __init__(self, built_year, price, current_value=0, location=str):
        self.built_year = built_year
        self.price = price
        self.current_year = current_year
        self.location = location

    def current_value(self):
        """Returns current value of the house when called"""
        current_value = self.price * (1 + 0.08) ** (self.current_year - self.built_year)
        return int(current_value)

    def money_earned(self):
        """Returns total amount of money earned-Subtracts current value from price"""
        money_earned = self.current_value() - self.price
        return money_earned

    def __str__(self):
        """Main information"""
        print('=' * 25)
        print("House Information:")
        print("\t Year Built: ", self.built_year)
        print("\t Purchase price: ", self.price)
        print("\t Current Value of House: ", self.current_value())
        print("\t Location: ", self.location)
        print('=' * 25)
        print('=' * 45)
        print()
        print('Total value you will earn: ', self.money_earned())
        print()
        print('=' * 45)

    def main(self):
        self.__str__()


# Main program


if __name__ == "__main__":
    print("Welcome to our house calculation app")
    print('=' * 36)
    print()
    choice = input("Do you want to check the price of a house? Y/N")
    final_choice = choice.lower()
    if final_choice == "y":
        x = True
        while x:
            house_model_year = int(input("Enter house model year: "))
            if 0 < house_model_year < date.today().year:
                x = False
            else:
                print("Enter Valid year.")

        y = True
        while y:
            price = int(input("Price of the house: "))
            if price > 0:
                y = False
            else:
                print("Enter Valid price.")

        z = True
        while z:
            current_year = int(input("Enter the current year : "))
            if current_year == date.today().year:
                z = False
            else:
                print("Enter the correct current year  ")
    elif final_choice == "n":
        exit()

house_location = str(input("Enter your house location: "))
inputs = House(house_model_year, price, current_year, house_location)
inputs.main()
