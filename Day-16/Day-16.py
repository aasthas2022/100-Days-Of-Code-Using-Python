## Day 16 - Section 16: Intermediate - Object Oriented Programming (OOP)

# Procedural programming - Top Bottom Approach - earliest paradigm of programming 

# Object oriented programming - objects have attributes (things object have) and methods (thisngs obj can do) - blueprint is called a class - class names are always pascal-s case Eg. class WhatIsYourName - attributes can be access by say eg objname.attributename and for method it can be accessed as objname.menthodname()

# Pypi - Python package index 


# Coffee Machine Program Using OOD

"""
Refer day 15 for detailed problem statement. We are rewriting the same code but using ood paradigm.

MenuItem Class
Attributes:
- name
(str) The name of the drink.
e.g. “latte”
- cost
(float) The price of the drink.
e.g 1.5
- ingredients
(dictionary) The ingredients and amounts required to make the drink.
e.g. {“water”: 100, “coffee”: 16}

Menu Class
Methods:
- get_items()
Returns all the names of the available menu items as a concatenated string.
e.g. “latte/espresso/cappuccino”
- find_drink(order_name)
Parameter order_name: (str) The name of the drinks order.
Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
otherwise returns None.

CoffeeMaker Class
Methods:
- report()
Prints a report of all resources.
e.g.
Water: 300ml
Milk: 200ml
Coffee: 100g
- is_resource_sufficient(drink)
Parameter drink: (MenuItem) The MenuItem object to make.
Returns True when the drink order can be made, False if ingredients are insufficient.
e.g.
True
- make_coffee(order)
Parameter order: (MenuItem) The MenuItem object to make.
Deducts the required ingredients from the resources.

MoneyMachine Class
Methods:
- report()
Prints the current profit
e.g.
Money: $0
- make_payment(cost)
Parameter cost: (float) The cost of the drink.
Returns True when payment is accepted, or False if insufficient.
e.g. False
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    while True:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        if choice == "off":
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                else:
                    print("Sorry, insufficient resources or payment declined.")
            else:
                print("Invalid choice. Please select a valid drink.")

if __name__ == "__main__":
    main()
