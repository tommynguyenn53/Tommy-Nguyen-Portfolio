MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 2.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 4.5,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine_off = False
money_made = 0
money_inserted = 0


def calculate(coffee_type, water, milk, coffee, inserted):
    global money_made
    if water >= MENU[coffee_type]['ingredients']['water']:
        if milk >= MENU[coffee_type]['ingredients']['milk']:
            if coffee >= MENU[coffee_type]['ingredients']['coffee']:
                if inserted >= MENU[coffee_type]['cost']:
                    resources['water'] -= MENU[coffee_type]['ingredients']['water']
                    resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
                    resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
                    money_returned = round(float(inserted - MENU[coffee_type]['cost']), 2)
                    money_made += MENU[coffee_type]['cost']
                    return f"Here is ${money_returned} in change.\nHere is your {coffee_type} ☕️. Enjoy!"
                else:
                    return "Sorry that's not enough money. Money refunded."
            else:
                return "Sorry there is not enough coffee."
        else:
            return "Sorry there is not enough milk."
    else:
        return "Sorry there is not enough water."


while not coffee_machine_off:
    user_choice = input("What would you like? {espresso/latte/cappuccino}: ").lower()

    if user_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_made}")

    elif user_choice == "off":
        coffee_machine_off = True

    else:
        print("Please insert coins.")
        five_cents = int(input("How many five cents? "))
        ten_cents = int(input("How many ten cents? "))
        twenty_cents = int(input("How many twenty cents? "))
        fifty_cents = int(input("How many fifty cents? "))
        one_dollar = int(input("How many one dollars? "))
        two_dollar = int(input("How many two dollars? "))

        money_inserted = (five_cents * 0.05 + ten_cents * 0.10 + twenty_cents * 0.20 +
                          fifty_cents * 0.50 + one_dollar * 1 + two_dollar * 2)

        print(calculate(coffee_type=user_choice, water=resources['water'], milk=resources['milk'],
                        coffee=resources['coffee'], inserted=money_inserted))
