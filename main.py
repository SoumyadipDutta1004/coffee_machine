import data
import functions as func


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
                print(f"Water: {data.resources["water"]}ml")
                print(f"Milk: {data.resources["milk"]}ml")
                print(f"Coffee: {data.resources["coffee"]}g")
                print(f"Money: ${data.profit}")
            else:
                order = data.MENU[choice]
                if func.check_resource_sufficient(order['ingredients']):
                    payment = func.process_coins(order['cost'])
                    if func.trans_success(payment, order['cost']):
                        func.make_coffee(choice, order['ingredients'])
        except:
            print("Please enter a valid input!")
