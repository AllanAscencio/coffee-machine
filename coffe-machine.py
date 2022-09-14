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
