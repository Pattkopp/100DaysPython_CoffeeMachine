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
}

leave = False
money = 0


def report():
    for k, v in resources.items():
        if k == "water":
            print(f"Water: {v}ml")
        elif k == "milk":
            print(f"Milk: {v}ml")
        elif k == "coffee":
            print(f"Coffee: {v}g")
    print(f"Money: ${money}")
    return


def check_resources(sel):
    for k, v in resources.items():
        if k not in MENU[sel]["ingredients"]:
            continue
        if MENU[sel]["ingredients"][k] > v:
            if k == "water":
                print("Not enough water.")
            if k == "milk":
                print("Not enough milk.")
            if k == "coffee":
                print("Not enough coffee.")
    return


def process_coins():
    print("Please enter your money:")
    quarters = int(input("Number of quarters: "))
    dimes = int(input("Number of dimes: "))
    nickels = int(input("Number of nickels: "))
    cents = int(input("Number of cents: "))
    amount = round(quarters * .25 + dimes * .10 + nickels * .05 + cents * .01, 2)
    print(f"Amount: ${amount}")
    return amount


def enough_money(sel, money_got):
    if MENU[sel]["cost"] > money_got:
        print(f"Sorry, not enough money for a {sel}. Money refunded.")
        return False
    else:
        return True


while not leave:
    money_obtained = 0
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == "off":
        leave = True
    elif selection == "report":
        report()
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        check_resources(selection)
        money_obtained = process_coins()
        if enough_money(selection, money_obtained):
            money += money_obtained
            if money_obtained > MENU[selection]["cost"]:
                refund = round(money_obtained - MENU[selection]["cost"], 2)
                print(f"Refunded: ${refund}")

