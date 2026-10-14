from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

mode_on = True
while mode_on:
    print("----------"*15)
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}): ").lower()

    if choice == "off":
        mode_on = False
        print("\t**out of order**")
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        