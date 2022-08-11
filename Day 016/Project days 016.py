from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#  What would you like? (espresso/latte/cappuccino): espresso
# Please insert coins.
# how many quarters?: 20
# how many dimes?: 3
# how many nickles?: 3
# how many pennies?: 3
# Here is $4.0 in change.
#  What would you like? (espresso/latte/cappuccino): latte
# Please insert coins.
# how many quarters?: 28
# how many dimes?: 83
# how many nickles?: 28
# how many pennies?: 378
# Here is $18.0 in change.
#  What would you like? (espresso/latte/cappuccino): cappuccino
# Sorry there is not enough water.
#  What would you like? (espresso/latte/cappuccino): report
# Water: 50ml
# Milk: 50ml
# Coffee: 58ml
# Money: $4.0
#  What would you like? (espresso/latte/cappuccino): test
# ERROR~~~
#  What would you like? (espresso/latte/cappuccino):

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_On = True

while is_On:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == "off":
        is_On = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
