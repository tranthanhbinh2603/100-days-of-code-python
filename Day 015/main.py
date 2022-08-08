from List import MENU
from List import resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

def checkResource(choose1):
    global water
    global milk
    global coffee
    if water < MENU[choose1.lower()]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return 1
    elif milk < MENU[choose1.lower()]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return 1
    elif coffee < MENU[choose1.lower()]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee. ")
        return 1
    else:
        return -1

def checkPrice(priceInput, choose):
    if float(priceInput) < MENU[choose]['cost']:
        return -1
    else:
        return priceInput - MENU[choose]['cost']

def setResouce(choose):
    global water
    global milk
    global coffee
    water -= MENU[choose.lower()]["ingredients"]["water"]
    milk -= MENU[choose.lower()]["ingredients"]["milk"]
    coffee -= MENU[choose.lower()]["ingredients"]["coffee"]

while True:
    choose = str(input(" What would you like? (espresso/latte/cappuccino): "))
    if choose.upper() == "REPORT":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}ml")
        print(f"Money: ${round(money,1)}")
    elif (choose.lower() == "espresso") or (choose.lower() == "latte") or (choose.lower() == "cappuccino"):
       if checkResource(choose) != 1:
           print("Please insert coins.")
           priceInput = float(input("how many quarters?: "))*0.25 + float(input("how many dimes?: "))*0.1 + float(input("how many nickles?: "))*0.05 + float(input("how many pennies?: "))*0.01
           refund = checkPrice(priceInput, choose)
           if refund != -1:
               print(f"Here is ${round(refund, 1)} in change.")
               setResouce(choose)
               money += MENU[choose]['cost']
           else:
               print("Sorry that's not enough money. Money refunded.")
    else:
        print("ERROR~~~")

