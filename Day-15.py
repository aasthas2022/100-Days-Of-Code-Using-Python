## Day 15 - Section 15:  Intermediate - Local Development Environment Setup & the Coffee Machine

# IDE - Integrated Developement Env - Helps in writing testing debugging and executing code all in one place. Eg. PyCharm
# Can spell check including english typo and keywords, has built in linter is PEP 8 is a style guide, keeps version history in terms of timepoint, can view structure 

'''
Coffee Machine Program Requirements
 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    a. Check the user’s input to decide what to do next.
    b. The prompt should show every time action has completed, e.g. once the drink is
       dispensed. The prompt should show again to serve the next customer.
 2. Turn off the Coffee Machine by entering “off” to the prompt.
    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
       the machine. Your code should end execution when this happens.
 3. Print report.
    a. When the user enters “report” to the prompt, a report should be generated that shows
       the current resource values. e.g.
       Water: 100ml
       Milk: 50ml
       Coffee: 76g
       Money: $2.5
 4. Check resources sufficient?
    a. When the user chooses a drink, the program should check if there are enough
       resources to make that drink.
    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
       not continue to make the drink but print: “Sorry there is not enough water.”
    c. The same should happen if another resource is depleted, e.g. milk or coffee.
 5. Process coins.
    a. If there are sufficient resources to make the drink selected, then the program should
       prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickels = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
       pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
 6. Check transaction successful?
    a. Check that the user has inserted enough money to purchase the drink they selected.
       E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
       program should say “Sorry that's not enough money. Money refunded.”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the
       machine as the profit and this will be reflected the next time “report” is triggered. E.g.
       Water: 100ml
       Milk: 50ml
       Coffee: 76g
       Money: $2.5
    c. If the user has inserted too much money, the machine should offer change.
       E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
       places.
 7. Make Coffee.
    a. If the transaction is successful and there are enough resources to make the drink the
       user selected, then the ingredients to make the drink should be deducted from the
       coffee machine resources.
       E.g. report before purchasing latte:
       Water: 300ml
       Milk: 200ml
       Coffee: 100g
       Money: $0
       Report after purchasing latte:
       Water: 100ml
       Milk: 50ml
       Coffee: 76g
       Money: $2.5
    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
       latte was their choice of drink.
'''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def makeCoffee(coffee):
    global resources, profit
    coffeeIngredients = coffee["ingredients"]
    if not isResourcesSufficient(coffeeIngredients) : 
        print("Sorry there is not enough resources.")
        return

    for item in resources:
        if item in coffeeIngredients:
            resources[item] -= coffeeIngredients[item]
    profit += coffee["cost"]
    print("Here is your coffee. Enjoy!")

    
def printReport():
    global resources, profit
    print("Water:", resources["water"], "ml")
    print("Milk:", resources["milk"], "ml")
    print("Coffee:", resources["coffee"], "g")
    print("Money: $", "{:.2f}".format(profit))
    
def switchOffTheMachine():
    global resources, profit
    printReport()
    exit()

def isResourcesSufficient(coffee):
    global resources
    for item in resources:
        if item in coffee:
            if resources[item] < coffee[item]:
                print("Sorry there is not enough", item + ".")
                return False
    return True

def processCoins(cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > cost:
        change = total - cost
        print("Here is $", "{:.2f}".format(change), "dollars in change.")
    return True

def main():
    while True:
        action = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
        if action == "off":
            switchOffTheMachine()
        elif action == "report":
            printReport()
        elif action in MENU:
            drink = MENU[action]
            if isResourcesSufficient(drink["ingredients"]):
                if processCoins(drink["cost"]):
                    makeCoffee(drink)
        else:
            print("Invalid input.")

main()

 