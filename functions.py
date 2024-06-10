import data


# TODO: 3. Check resources are sufficient or not
def check_resource_sufficient(coffee) -> bool:
    for item in coffee:
        if coffee[item] > data.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 4. Process coins
def process_coins(cost) -> float:
    total_amount = 0
    quarters = int(input("How many quarters? "))
    total_amount += 0.25 * quarters
    if total_amount > cost:
        return total_amount
    dimes = int(input("How many dimes? "))
    total_amount += 0.1 * dimes
    if total_amount > cost:
        return total_amount
    nickles = int(input("How many nickles? "))
    total_amount += 0.05 * nickles
    if total_amount > cost:
        return total_amount
    pennies = int(input("How many pennies? "))
    total_amount += 0.01 * pennies
    if total_amount > cost:
        return total_amount


# TODO: 5. Check transaction is successful or not
def trans_success(amount_receive, cost) -> bool:
    if amount_receive < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(amount_receive - cost, 2)
        print(f"Here is ${change} in change.")
        data.profit += cost
    return True


# TODO: 6. Make the coffee
def make_coffee(coffee_name, ingredients) -> any:
    for item in ingredients:
        data.resources[item] -= ingredients[item]
    print(f"Here is your {coffee_name}.Enjoy!.")



