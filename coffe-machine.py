"""COFFEE MACHINE MENU"""
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "total_money": 0
}


"""Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”"""
# DECIDE QUE VA A TOMAR EL USUARIO Y SE DESCUENTA DE LOS RECURSOS DE LA MAQUINA


def make_coffee():
    if user_choice == 'espresso':
            water_discount = list(resources.values())[0] - list(MENU.values())[0]['ingredients']['water']
            resources['water'] = water_discount
            coffee_discount = list(resources.values())[2] - list(MENU.values())[0]['ingredients']['coffee']
            resources['coffee'] = coffee_discount
            resources['total_money'] += 1.5
            print(f"Here is your {user_choice}. Enjoy!")

    elif user_choice == 'latte':
            water_discount = list(resources.values())[0] - list(MENU.values())[1]['ingredients']['water']
            resources['water'] = water_discount
            milk_discount = list(resources.values())[1] - list(MENU.values())[1]['ingredients']['milk']
            resources['milk'] = milk_discount
            coffee_discount = list(resources.values())[2] - list(MENU.values())[1]['ingredients']['coffee']
            resources['coffee'] = coffee_discount
            resources['total_money'] += 2.5
            print(f"Here is your {user_choice}. Enjoy!")

    elif user_choice == 'cappuccino':
            water_discount = list(resources.values())[0] - list(MENU.values())[2]['ingredients']['water']
            resources['water'] = water_discount
            milk_discount = list(resources.values())[1] - list(MENU.values())[2]['ingredients']['milk']
            resources['milk'] = milk_discount
            coffee_discount = list(resources.values())[2] - list(MENU.values())[2]['ingredients']['coffee']
            resources['coffee'] = coffee_discount
            resources['total_money'] += 3.0
            print(f"Here is your {user_choice}. Enjoy!")

    elif user_choice == 'report':
        print(report)

"""PROCESS COINS"""


def process_coins():
    global inserted_coins
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    total_quarters = quarters * 0.25
    dimes = float(input("How many dimes?: "))
    total_dimes = dimes * 0.10
    nickles = float(input("How many nickles?: "))
    total_nickles = nickles * 0.05
    pennies = float(input("How many pennies?: "))
    total_pennies = pennies * 0.01
    money_gathered = total_quarters + total_dimes + total_nickles + total_pennies
    inserted_coins = money_gathered


"""CHECK IF TRANSACTION IS SUCCESSFUL"""


def check_transaction():
    if user_choice == 'espresso':
        if inserted_coins == 1.5:
            make_coffee()
        elif inserted_coins > 1.5:
            change = inserted_coins - 1.5
            print(f"Here is ${change} dollars in change")
            make_coffee()
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif user_choice == 'latte':
        if inserted_coins == 2.5:
            make_coffee()
        elif inserted_coins > 2.5:
            change = inserted_coins - 2.5
            print(f"Here is ${change} dollars in change")
            make_coffee()
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif user_choice == 'cappuccino':
        if inserted_coins == 3.0:
            make_coffee()
        elif inserted_coins > 3.0:
            change = inserted_coins - 3.0
            print(f"Here is ${change} dollars in change")
            make_coffee()
        else:
            print("Sorry that's not enough money. Money refunded.")



"""Check if enough resources to make the coffee"""


def check():
    if user_choice == 'espresso':
        if list(resources.values())[0] < 50:
            print("Not enough water")
            return 1
        elif list(resources.values())[2] < 18:
            print("Not enough coffee")
            return 1
    elif user_choice == 'latte':
        if list(resources.values())[0] < 200:
            print("Not enough water")
            return 1
        elif list(resources.values())[1] < 150:
            print("Not enough milk")
            return 1
        elif list(resources.values())[2] < 24:
            print("Not enough coffee")
            return 1
    elif user_choice == 'cappuccino':
        if list(resources.values())[0] < 250:
            print("Not enough water")
            return 1
        elif list(resources.values())[1] < 100:
            print("Not enough milk")
            return 1
        elif list(resources.values())[2] < 24:
            print("Not enough coffee")
            return 1


off = False
inserted_coins = 0
report = resources

"""RUN OF THE WHOLE PROGRAM"""

while not off:
    user_choice = input("What would like? (espresso/latte/cappuccino)\nFor Admin Users write 'off' to refill the "
                        "machine or 'report' to print a report:\n").lower()
    if user_choice == 'off':
        break
    elif user_choice == 'espresso':
        if check() == 1:
            continue
        else:
            process_coins()
            check_transaction()
    elif user_choice == 'latte':
        if check() == 1:
            continue
        else:
            process_coins()
            check_transaction()
    elif user_choice == 'cappuccino':
        if check() == 1:
            continue
        else:
            process_coins()
            check_transaction()
    elif user_choice == 'report':
        for key, value in resources.items():
            print(key, ':', value)