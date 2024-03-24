MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0,
}

def reporting():
    """Generate Report that shows current resource values"""
    print (F"Water: {resources['water']}ml")
    print (f"Milk: {resources['milk']}ml")
    print (f"Coffee: {resources['coffee']}g")
    print (f"Money: ${resources['money']}")

def check_resources(drink):
    """Check whether there are enough resources to make the input drink.
    If there aren't, print all missing ingredients."""
    issue = ''
    water_cost = MENU[drink]['ingredients']['water']
    if water_cost > resources['water']:
        issue += "Not enough water.\n"
    coffee_cost = MENU[drink]['ingredients']['coffee']
    if coffee_cost > resources['coffee']:
        issue += "Not enough coffee.\n"
    milk_cost = MENU[drink]['ingredients']['milk']
    if milk_cost > resources['milk']:
        issue += "Not enough milk.\n"
    if issue == "":
        print (f"Enough resources to make {drink}")
        return True
    else:
        print(issue)
        return False
    
def spend_resources(drink):
    """Helper function to spend ingredients from resources, based 
    on creating the input drink from the menu."""
    water_cost = MENU[drink]['ingredients']['water']
    coffee_cost = MENU[drink]['ingredients']['coffee']
    milk_cost = MENU[drink]['ingredients']['milk']
    resources["coffee"] -= coffee_cost
    resources["milk"] -= milk_cost
    resources["water"] -= water_cost
    

def process_payment (drink):
    """Helper function to take payment, check if it's enough, 
    check whether there's an overpayment, and modify our resources money."""
    price_to_pay = MENU[drink]["cost"]
    wallet = 0
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennnies?: "))
    wallet += quarters * 0.25
    wallet += dimes * 0.10
    wallet += nickles * 0.05
    wallet += pennies * 0.01
    if price_to_pay > wallet:
        print("You don't have enough to pay for the drink.  You've been refunded")
        return False
    elif price_to_pay == wallet:
        print ("You paid exact change")
        resources["money"] += price_to_pay
        spend_resources(drink)
        return True
    else:
        change = wallet - price_to_pay
        print (f"Here is ${round(change,2)} dollars in change")
        resources["money"] += price_to_pay
        spend_resources(drink)
        return True


machine_on = True

while machine_on is True:
    what_to_do=  input("What would you like? (espresso/latte/cappuccino):")
    if what_to_do == 'report':
        reporting()
    if what_to_do == 'off':
        machine_on = False
    else:
            proceed = check_resources(what_to_do)
            if proceed == True:
                proceed = process_payment(what_to_do)
            if proceed == True:
                print (f"Here is your {what_to_do}.  Enjoy!")
                reporting()
            else:
                proceed = False
