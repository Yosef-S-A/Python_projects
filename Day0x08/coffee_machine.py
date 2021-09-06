#!/usr/bin/python3

from os import system, name


def clear_screen():
    # clear screen
    if name == 'nt':  # for Windows
        _ = system('cls')
    else:  # for linux and mac
        _ = system('clear')
    print(art.logo)


water = 300  # in milliliter
milk = 200  # in milliliter
coffee = 100  # in grams
money = 0.0  # in dollars


def get_stat():
    print("Water: {}".format(water))
    print("Milk: {}".format(milk))
    print("Coffee: {}".format(coffee))
    print("Money: {}". format(money))


def switch_off():
    return False


def make_esp():
    global water, milk, coffee, money, price
    if water >= 50:
        water -= 50
    else:
        print("Not enough water")
        return False
    if coffee >= 18:
        coffee -= 18
    else:
        print("Not enough coffee")
        return False

    price = 1.50
    money += price
    return True


def make_cap():
    global water, milk, coffee, money, price
    if water >= 250:
        water -= 250
    else:
        print("Not enough water")
        return False

    if milk >= 100:
        milk -= 100
    else:
        print("Not enough milk")
        return False
    if coffee >= 24:
        coffee -= 24
    else:
        print("Not enough coffee")
        return False

    price = 3.0
    money += price
    return True


def make_latte():
    global water, milk, coffee, money, price
    if water >= 200:
        water -= 200
    else:
        print("Not enough water")
        return False

    if milk >= 150:
        milk -= 150
    else:
        print("Not enough milk")
        return False

    if coffee >= 24:
        coffee -= 24
    else:
        print("Not enough coffee")
        return False

    price = 2.5
    money += price
    return True


def get_change():
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    total = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    if total >= price:
        return "This is your change: {0:.2f}".format(total - price)
    else:
        return "Not enough money"


def operation():
    global money
    accept_order = True
    while accept_order:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'espresso':
            if make_esp():
                change = get_change()
                print(change)
                print("Here is your {}. Enjoy!".format(choice))
            else:
                accept_order = switch_off()
        elif choice == 'latte':
            if make_latte():
                change = get_change()
                print(change)
                print("Here is your {}. Enjoy!".format(choice))
            else:
                accept_order = switch_off()
        elif choice == 'cappuccino':
            if make_cap():
                change = get_change()
                print(change)
                print("Here is your {}. Enjoy!".format(choice))
            else:
                accept_order = switch_off()
        elif choice == 'report':
            get_stat()
        elif choice == 'off':
            accept_order = switch_off()
        else:
            print("Command not found, Please check")


operation()
