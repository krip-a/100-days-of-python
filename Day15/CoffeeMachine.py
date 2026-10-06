from coffeeData import MENU, resources
from coffee_art import cup
from datetime import datetime

money = 0.00

def update_piggybank(new_amount):
    """add money once transaction successful"""
    global money
    money += new_amount
    

def get_resources(coffee_type):
    """returns the resource list required for type of coffee"""
    requirements = MENU[coffee_type]
    ingredients = requirements["ingredients"]
    
    water = ingredients["water"] if "water" in ingredients else 0
    milk = ingredients["milk"] if "milk" in ingredients else 0
    coffee = ingredients["coffee"] if "coffee" in ingredients else 0
    cost = requirements["cost"] if "cost" in requirements else 0
    
    return water, milk, coffee, cost

def check_resources(coffee_type):
    """check is the resource bank has enough ingredients"""
    water, milk, coffee, _ = get_resources(coffee_type)
    missing =(
            "water" if water >= resources["water"] 
            else "milk" if milk >= resources["milk"]
            else "coffee" if coffee >= resources["coffee"]
            else "none"
        )
    if missing == "none":
        return True
    else:
        print(f"Sorry, not enough {missing}.")
        return False

def insert_and_check_coins(price):
    """check and insert until the amount exceeds the price"""
    print(f"\nPlease insert ${price} coins.")
    quarters = int(input("How many quarters are you inserting? "))
    dimes = int(input("How many dimes are you inserting? "))
    nickles = int(input("How many nickles are you inserting? "))
    pennies = int(input("How many pennies are you inserting? "))
    total_amount = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
       
    if total_amount > price:
        change = total_amount - price
        print(f"\nYour change is ${change: .2f}")
        update_piggybank(price)
        return True
    else:
        print("\n"*10)
        print("Sorry, the coins you inserted are too low.")
        print("Your coins will be returned. Insert Again.")
        insert_and_check_coins(price)

def make_coffee(coffee_type):
    water, milk, coffee, _ = get_resources(coffee_type)
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee
    print(cup)
    print(f"Here is your {coffee_type}. Enjoy!")
    
def main():
    mode_on = True
    while mode_on:
        print("----------"*15)
        product = input("What would you like to drink? ").lower()
        if product == "report":
            print(f"As of {datetime.now()}, we have:")
            print(f"\tWater: {resources["water"]}ml")
            print(f"\tMilk: {resources["milk"]}ml")
            print(f"\tCoffee: {resources["coffee"]}g")
            print(f"\tMoney: ${money}")

        elif product == "espresso":
            if check_resources("espresso"):
                _, _, _, price = get_resources("espresso")
                enough_money = insert_and_check_coins(price)
                if enough_money:
                    make_coffee("espresso")
            
        elif product == "latte":
            if check_resources("latte"):
                _, _, _, price = get_resources("latte")
                enough_money = insert_and_check_coins(price)
                if enough_money:
                    make_coffee("latte")         

        elif product == "cappuccino":
            if check_resources("cappuccino"):
                _, _, _, price = get_resources("cappuccino")
                enough_money = insert_and_check_coins(price)
                if enough_money:
                    make_coffee("cappuccino")
            
        elif product == "off":
            mode_on = False
            print("\t**out of order**")
        else:
            exit()

main()