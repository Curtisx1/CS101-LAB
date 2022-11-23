# Name: Curtis Lemke
# Class: CS101 Section 3
# Program: 3
# Creation date: 10/16/2022
# Due date: 10/16/2022

# Imported modules

# Fuctions


def main_menu():
    print('Welcome to 101 DELIVERY\n')
    print('We deliver from any of these 2 restaurants:\n')
    print('1- Chipotle\n2- Q39\n3- Both restaurants\n')
    choice = int(input('1 for Chipotle\n2 for Q39\n3 for both restaurants\nEnter your choice:'))
    if choice == 1:
        chipolte()
    elif choice == 2:
        q39()
    elif choice == 3:
        both()

def chipolte():
    total = 0
    cont = 'y'
    delver_cg = 0
    loop = True
    while (cont == 'y' or cont == 'Y'):
        print('Chipotle menu:\n1: Chicken burrito $7.95\n2: Steak burrito bowl $ 9.30\n3: Chicken Quesadilla $8.50')
        if (loop == True):
            ch = int(input('Enter your choice:'))
        if (ch == 1 or ch == 2 or ch == 3):
            qty = read_qty()
            print('Your ordered option', ch, ' with quantity', qty)
            if (ch == 1):
                total = total + (qty * 7.95)
                print('Your total for now is $', total)
            elif (ch == 2):
                total = total + (qty * 9.30)
                print('Your total for now is $', total)
            else:
                total = total + (qty * 8.50)
                print('Your total for now is $', total)
            cont = input('Do you want to add anything else? Y/N:')
            if (cont == 'n' or cont == 'N'):
                if (total < 35):
                    print('Your total is less than $35 Your total is $', round(total, 5))
                    rem = 35 - total
                    print('You need to add $', rem, 'for free delivery')
                    rem_ch = input('Do you want to add an item to your order? Y/N:\n')
                    if (rem_ch == 'y' or rem_ch == 'Y'):
                        cont = 'y'
                        loop = True
                    elif (rem_ch == 'n' or rem_ch == 'N' and qty != 0):
                        delver_cg = 10
                else:
                    delivery_tax()
                    print('Your total is equal or greater than $35.')
                    print('You have a free delivery!')
            else:
                loop = True
        else:
            ch = int(input('Enter a valid option 1/2/3:'))
            loop = False
    return total

def q39():
    total = 0
    cont = 'y'
    delver_cg = 0
    loop = True
    while (cont == 'y' or cont == 'Y'):
        print('Q39 Menu:\n1: Wings $13.25\n2: Burnt End Burger $16.50\n3: Brisket $12.99')
        if (loop == True):
            ch = int(input('Enter your choice:'))
        if (ch == 1 or ch == 2 or ch == 3):
            qty = read_qty()
            print('Your ordered option', ch, ' with quantity', qty)
            if (ch == 1):
                total = total + (qty * 13.25)
                print('Your total for now is $', total)
            elif (ch == 2):
                total = total + (qty * 16.50)
                print('Your total for now is $', total)
            else:
                total = total + (qty * 12.99)
                print('Your total for now is $', total)
            cont = input('Do you want to add anything else? Y/N:')
            if (cont == 'n' or cont == 'N'):
                if (total < 35):
                    print('Your total is less than $35 Your total is $', round(total, 5))
                    rem = 35 - total
                    print('You need to add $', rem, 'for free delivery')
                    rem_ch = input('Do you want to add an item to your order? Y/N:\n')
                    if (rem_ch == 'y' or rem_ch == 'Y'):
                        cont = 'y'
                        loop = True
                    elif (rem_ch == 'n' or rem_ch == 'N' and qty != 0):
                        delver_cg = 10
                else:
                    delivery_tax()
                    print('Your total is equal or greater than $35.')
                    print('You have a free delivery!')
            else:
                loop = True
        else:
            ch = int(input('Enter a valid option 1/2/3:'))
    return total
def both():
    total = 0
    cont = 'y'
    delver_cg = 0
    loop = True
    while cont == 'y' or cont == 'Y':
        print('***First store:***')
        print('Chipotle menu:\n1: Chicken burrito $7.95\n2: Steak burrito bowl $ 9.30\n3: Chicken Quesadilla $8.50')
        if (loop == True):
            ch = int(input('Enter your choice:'))
        if (ch == 1 or ch == 2 or ch == 3):
            qty = read_qty()
            print('Your ordered option', ch, ' with quantity', qty)
            if (ch == 1):
                total = total + (qty * 7.95)
                print('Your total for now is $', total)
            elif (ch == 2):
                total = total + (qty * 9.30)
                print('Your total for now is $', total)
            else:
                total = total + (qty * 8.50)
                print('Your total for now is $', total)
            cont = input('Do you want to add anything else? Y/N:')
            if (cont == 'n' or cont == 'N'):
                if (total < 35):
                    print('Your total is less than $35 Your total is $', round(total, 5))
                    rem = 35 - total
                    print('You need to add $', rem, 'for free delivery')
                    rem_ch = input('Do you want to add anything else from this store? Y/N\n')
                    if (rem_ch == 'y' or rem_ch == 'Y'):
                        cont = 'y'
                        loop = True
                    elif (rem_ch == 'n' or rem_ch == 'N' and qty != 0):
                        delver_cg = 10
                        print('***Second Store:***')
                        print('Q39 Menu:\n1: Wings $13.25\n2: Burnt End Burger $16.50\n3: Brisket $12.99')
                        if (loop == True):
                            ch = int(input('Enter your choice:'))
                        if (ch == 1 or ch == 2 or ch == 3):
                            qty = read_qty()
                            print('Your ordered option', ch, ' with quantity', qty)
                            if (ch == 1):
                                total = total + (qty * 13.25)
                                print('Your total for now is $', total)
                            elif (ch == 2):
                                total = total + (qty * 16.50)
                                print('Your total for now is $', total)
                            else:
                                total = total + (qty * 12.99)
                                print('Your total for now is $', total)
                            cont = input('Do you want to add anything else? Y/N:')
                            if (cont == 'n' or cont == 'N'):
                                if (total < 35):
                                    print('Your total is less than $35 Your total is $', round(total, 5))
                                    rem = 35 - total
                                    print('You need to add $', rem, 'for free delivery')
                                    rem_ch = input('Do you want to add anything else from this store? Y/N\n')
                                    if (rem_ch == 'y' or rem_ch == 'Y'):
                                        cont = 'y'
                                        loop = True
                                    elif (rem_ch == 'n' or rem_ch == 'N' and qty != 0):
                                        delver_cg = 10
                                        loop = False
                                else:
                                    delivery_tax()
                                    print('Your total is equal or greater than $35.')
                                    print('You have a free delivery!')
                            else:
                                loop = True
                        else:
                            ch = int(input('Enter a valid option 1/2/3:'))

    return total
def delivery_tax(total):
    grand_total = total + (total * 0.043) + total
    result = print('Your order total after tax is $', round(grand_total, 2))
    return result

def read_qty():
    qty=int(input('Enter your quantity:\n'))
    while(qty<0):
        qty=int(input('Enter valid quantity:\n'))
    return qty

# Main program


if __name__ == "__main__":
    main_menu()
