from data import MENU, resources

def get_a_drink_choice():
    """Ask a customer to choose a drink."""
    valid_choices = list(MENU.keys()) + ["report", "off"]
    options = " / ".join(MENU.keys()).title()
    drink_name = ""
    while drink_name not in valid_choices:
        drink_name = input(f"What would you like? \n{options}: ").lower()
        if drink_name not in valid_choices:
            print(f"'{drink_name.title()}' is not in our menu. 🙇🏽‍♂️ Please select the drink again.\n")
    return drink_name

def print_a_report(remaining_resources, remaining_fund):
    print(f"Water: {remaining_resources['water']}ml\n"
          f"Milk: {remaining_resources['milk']}ml\n"
          f"Coffee: {remaining_resources['coffee']}g\n"
          f"Money: ${remaining_fund}\n")

def enough_ingredients(ingredients, remaining_resources):
    """Check each ingredient OF THE DRINK is enough to make a drink. """
    for item in ingredients:
        if ingredients[item] > remaining_resources.get(item,0):
            print(f"Sorry there is not enough {item}.\n")
            return False
    return True

def calculate_money():
    """Return the total calculated from inserted coins."""
    print("Please insert coins.")
    try:
        quarters = int(input("  How many quarters?: ")) * 0.25
        dimes = int(input("  How many dimes?: ")) * 0.1
        nickles = int(input("  How many nickles?: ")) * 0.05
        pennies = int(input("  How many pennies?: ")) * 0.01
        total = quarters + dimes + nickles + pennies
        return total
    except ValueError:
        print("Error! ❌ Invalid Input! 🪙 Please select the drink again.\n")
        return None

def update_resources(item, remaining_resources):
    """Reduce the resources by the ingredients used"""
    for ingredient in item:
        remaining_resources[ingredient] -= item[ingredient]
    # no need to return remaining_resources because it's already changed itself.

profit = 0

while True:
    drink = get_a_drink_choice()
    if drink == "off":
        print("Turning off the machine.📴")
        break
    elif drink == "report":
        print_a_report(resources, profit)
        continue
    else:
        drink_ingredients = MENU[drink]["ingredients"]
        drink_cost = MENU[drink]["cost"]

    if enough_ingredients(drink_ingredients,resources):
        print(f"{drink.title()}'s price: ${drink_cost}")
        inserted_money = calculate_money()
        if inserted_money is None:
            continue
        print(f"\nMoney inserted: ${inserted_money:.2f}")

        # Check if the total inserted money is enough to buy a coffee
        if inserted_money >= drink_cost:
            profit += drink_cost  # Add money
            update_resources(drink_ingredients, resources)
            print(f"Here is your {drink} ☕. Enjoy! ✨")
            print(f"Here is ${(inserted_money - drink_cost):.2f} in change.\n")

        else:
            print("😟 Sorry, that's not enough money. Money refunded.\n")

