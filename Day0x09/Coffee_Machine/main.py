#!/usr/bin/python3

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drink = Menu()
resource = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'report':
        resource.report()
        money.report()
    elif choice == 'off':
        is_on = False
    else:
        cost = drink.find_drink(choice).cost
        drink_item = drink.find_drink(choice)

        if resource.is_resource_sufficient(drink_item):
            if money.make_payment(cost):
                resource.make_coffee(drink_item)
