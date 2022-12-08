# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 8
# Due Date: 12/9/2022
# Created date: 12/7/2022


# Imported Libraries


# Function List

# Classes
class Store:
    """Handles location name and items for sale. Base class for Cart"""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.products = {"Milk" : 2.5, "Bread" : 1.98, "Egg" : 0.7, "Flour" : 1.18, "Oil" : 4, "Cheese" : 2.68}

    def setName(self, name):
         self.name = name 

    def setLocation(self, location):
        self.location = location

    def addProduct(self, product, price):
        self.products[product] = price

    def displayProducts(self):
        print("Available Products:")
        print("=" * 19)
        for i, j in self.products.items():
            print("{:<10}: ${:.2f}".format(i, j))

    def displayData(self):
        print("Placed order from: " + self.name + "\nAt address: " + self.location)

# Cart Class
class Cart (Store):
    """Handles the shopping cart. Inherits from the "Store" class. Displays user shopping cart and totals."""
    def __init__(self, store_name, store_address):
        self.receipt = 0
        self.cart = {}
        Store.__init__(self, store_name, store_address)

    def add_item(self, item, quantity):
        if(item in self.products):
            self.cart[item] = quantity 
            self.receipt += self.products[item] * quantity

        else:
            print("Item not present in our store.\n")

    def remove_item(self, item, quantity):
        if(len(self.cart) == 0):
            print("Your cart is empty. Please continue shopping.\n")
            return

        if(item in self.cart):
            if(quantity == self.cart[item]):
                self.cart.pop(item)
                self.receipt -= self.products[item] * quantity

            elif(quantity < self.cart[item]):
                self.cart[item] -= quantity
                self.receipt -= self.products[item] * quantity

            else:
                print("There are not enough items in your cart.\n")
                print("Please try again.\n")
            
        else:
            print("Item not present in the cart.\n")

    def displayData(self):
        super().displayData()
        print("Order in cart is:",len(self.cart))
        for i,j in self.cart.items():
            print(i,"With quantity:",j)
            print("Shopping cart total is $",self.receipt)

# Main function 

if __name__ == '__main__':
    store_name = input("Good morning! Which store would you like to use today?\n")
    store_address = input("Which location do you want to use?\n")
    store = Store(store_name, store_address)
    cart = Cart(store_name, store_address)
    store.displayProducts()
    product = input("Enter the name of a product to add:\n").title()
    while(True):
        try:
            quantity = int(input("Enter item quantity:\n"))
            break

        except:
            print("Please enter an integer for quantity.\n")

    cart.add_item(product, quantity)
    cart.displayData()
    while(True):
        choice = input("Do you want to remove an item? (Yes/No)\n").lower()
        if(choice == "yes"):
            product = input("Enter the name of a product to add:\n").title()
            while(True):
                try:
                    quantity = int(input("Enter item quantity:\n"))
                    break
                except:
                    print("Please enter an integer for quantity.\n")
            cart.remove_item(product, quantity)
            cart.displayData()
        else:
            choice2 = input("Do you want to add another product? (Yes/No):\n").lower()
            if(choice2 == "yes"):
                store.displayProducts()
                product = input("Enter the name of a product to add:\n").title()
                while(True):
                    try:
                        quantity = int(input("Enter item quantity:\n"))
                        break
                    except:
                        print("Please enter an integer for quantity.\n")
                cart.add_item(product, quantity)
                cart.displayData()
            else:
                print("Your Order details are as follows:\n")
                cart.displayData()
                print("Thank you for shopping with us! Have a nice day.")
                break
