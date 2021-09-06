#!/usr/bin/python3

from coffee_data import MENU, resources

is_on = True
profit = 0


def resource_check(order_ingredients):
    for item in order_ingredients:
        if (order_ingredients[item] >= resources[item]):
            print("Sorry there is not enough {}.".format(item))
            return False

    return True


def total_money():
    quarter = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total = (quarter * 0.25) + (dimes * 0.1) + \
        (nickles * 0.05) + (pennies * 0.01)
    return total


def get_change(order):
    global profit
    customer_money = total_money()
    if (customer_money >= order):
        print("Here is ${:.3} in change.".format(customer_money - order))
        profit += order
        return True
    else:
        return False

def use_resource(chosen_drink):
    for item in chosen_drink:
       resources[item] -= chosen_drink[item]

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False

    elif choice == "report":
        print('Water: {}ml'.format(resources['water']))
        print('Milk: {}ml'.format(resources['milk']))
        print('Coffee: {}g'.format(resources['coffee']))
        print('Money: ${}'.format(profit))
    else:
        drink = MENU[choice]
        if resource_check(drink["ingredients"]):
            if get_change(drink['cost']):
               use_resource(drink["ingredients"])
               print("Here is your {}. Enjoy!".format(choice))
            else:
               print("Sorry that's not enough money. Money refunded.")
