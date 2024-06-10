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


# TODO: 3. Check resources are sufficient or not
def check_resource_sufficient(coffee) -> bool:
    for item in coffee:
        if coffee[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 4. Process coins
def process_coins() -> float:
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total_amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total_amount


# TODO: 5. Check transaction is successful or not
def trans_success(amount_receive, cost) -> bool:
    if amount_receive < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(amount_receive - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
    return True


# TODO: 6. Make the coffee
def make_coffee(coffee_name, ingredients) -> any:
    global resources
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {coffee_name}.Enjoy!.")


if __name__ == "__main__":
    is_ture = 1

    while is_ture:
        # TODO: 1. Prompt user by asking "What would you like?(espresso/latte/capuccino):"
        choice = input("What would you like?(espresso/latte/cappuccino): ").lower()
        try:
            if choice == 'off':
                is_ture = 0
            # TODO: 2. print resources of the coffee machine
            elif choice == 'report':
                print(f"Water: {resources["water"]}ml")
                print(f"Milk: {resources["milk"]}ml")
                print(f"Coffee: {resources["coffee"]}g")
                print(f"Money: ${profit}")
            else:
                order = MENU[choice]
                if check_resource_sufficient(order['ingredients']):
                    payment = process_coins()
                    if trans_success(payment, order['cost']):
                        make_coffee(choice, order['ingredients'])
        except:
            print("Please enter a valid input!")
