# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 8
# Due Date: 12/9/2022
# Created date: 12/7/2022


# Imported Libraries


# Function List

# Classes
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_description(self):
        print(self.item_name + ", " + self.item_description)

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str( self.item_price * self.item_quantity ));


class ShoppingCart:
    def __init__(self, cn="none", cd="January 1, 2016"):
        self.customerName = cn
        self.current_date = cd
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, itemName):
        foundIdx = -1
        for i in range(len(self.items)):
            if self.items[i].item_name == itemName:
                foundIdx = i
                break
            if foundIdx == -1:
                print("Item not found in the cart. Nothing removed.")
            else:
                del self.items[foundIdx]

    def modify_item(self, item):
        foundIdx = -1
        for i in range(len(self.items)):
            if self.items[i].item_name == item.item_name:
                foundIdx = i
                break

        if foundIdx == -1:
            print("Item not found in the cart. Nothing modified.")
        else:
            self.items[foundIdx].item_quantity = item.item_quantity

    def get_num_items_in_cart(self):
        return len(self.items)

    def get_cost_of_cart(self):
        totalCost = 0
        for item in self.items:
            totalCost += (item.item_quantity * item.item_price)
            return totalCost

    def print_total(self):
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customerName + "'s Shopping Cart - " + self.current_date)
            print("Number of Items: ", self.get_num_items_in_cart(),"\n")
        for item in self.items:
            item.print_item_cost()
            print("\n\nTotal: $" + str(self.get_cost_of_cart()))

    def print_descriptions(self):
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customerName + "'s Shopping Cart - " + self.current_date)
            print("\nItem Descriptions")
        for item in self.items:
            item.print_item_description()

        def print_menu(pObj):
            while(True):
                print("\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output item's description\no - Output shopping cart\nq - Quit\n\nChoose an option:")
                ch = input()
                if ch.lower() == "q":
                    break

                elif ch.lower() == "a":
                    print("ADD ITEM TO CART")
                    item = ItemToPurchase()
                    item.item_name = input('Enter the item name:\n')
                    item.item_description = input('Enter the item description:\n')
                    item.item_price = int(input('Enter the item price:\n'))
                    item.item_quantity = int(input('Enter the item quantity:\n'))
                    pObj.add_item(item)

                elif ch.lower() == "r":
                    print("REMOVE ITEM FROM CART")
                    itemName = input('Enter the item name to remove:\n')
                    pObj.remove_item(itemName)

                elif ch.lower() == "c":
                    print("CHANGE ITEM QUANTITY")
                    item = ItemToPurchase()
                    item.item_name = input('Enter the item name:\n')
                    item.item_quantity = int(input('Enter the new quantity:\n'))
                    pObj.modify_item(item)

                elif ch.lower() == "o":
                    print("OUTPUT SHOPPING CART")
                    pObj.print_total()

                elif ch.lower() == "i":
                    print("OUTPUT ITEM'S DESCRIPTIONS")
                    pObj.print_descriptions()

                def main(self):
                    self.cName = input("Enter customer's name:\n")
                    self.cDate = input("Enter today's date:\n")
                    print("\nCustomer name:", self.cName)
                    print("Today's date:", self.cDate)
                    pObj = ShoppingCart(self.cName, self.cDate)
                    self.print_menu(pObj)


if __name__ == '__main__':
    ShoppingCart.main(ShoppingCart)
