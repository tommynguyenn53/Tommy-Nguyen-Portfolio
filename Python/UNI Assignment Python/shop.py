'''
Write your solution to 1. Upgraded Cheese Shop here.
It should borrow code from Assignment 1.

Author:
SID:
Unikey:
'''

CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))


def buy_cheese(gold: int) -> tuple:
    cheese_total = (0, 0, 0)
    total_cost = 0
    while True:
        print(f'You have {gold} gold to spend.')
        purchase = input("State [cheese quantity]: ").split()
        cheese_type = purchase[0]
        if len(purchase) == 1:
            if cheese_type == "back":
                return total_cost, cheese_total
            if cheese_type != "cheddar" and cheese_type != "marble" and cheese_type != "swiss":
                print(f"We don't sell {cheese_type}!")
                continue
            else:
                print("Missing quantity.")
                continue
        if len(purchase) == 2:
            cheese_amount = int(purchase[1])
            total_cheddar_cost = cheese_amount * CHEESE_MENU[0][1]
            total_marble_cost = cheese_amount * CHEESE_MENU[1][1]
            total_swiss_cost = cheese_amount * CHEESE_MENU[2][1]
            if cheese_amount <= 0:
                print("Must purchase positive amount of cheese.")
                continue
            elif cheese_type == "cheddar" and total_cheddar_cost <= gold:
                gold -= total_cheddar_cost
                cheese_total = (cheese_total[0] + cheese_amount, cheese_total[1], cheese_total[2])
                total_cost += total_cheddar_cost
                print(f'Successfully purchase {cheese_amount} cheddar.')
                continue
            elif cheese_type == "marble" and total_marble_cost <= gold:
                gold -= total_marble_cost
                cheese_total = (cheese_total[0], cheese_total[1] + cheese_amount, cheese_total[2])
                total_cost += total_marble_cost
                print(f'Successfully purchase {cheese_amount} marble.')
                continue
            elif cheese_type == "swiss" and total_swiss_cost <= gold:
                gold -= total_swiss_cost
                cheese_total = (cheese_total[0], cheese_total[1], cheese_total[2] + cheese_amount)
                total_cost += total_swiss_cost
                print(f'Successfully purchase {cheese_amount} swiss.')
                continue
            else:
                print("Insufficient gold.")
                continue



def display_inventory(gold: int, cheese: list, trap: str) -> None:
    print(f'Gold - {gold}\nCheddar - {cheese[0][1]}\nMarble - {cheese[1][1]}\nSwiss - {cheese[2][1]}\nTrap - {trap}')


def main():
    starting_gold = 125
    gold = starting_gold
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap = "Cardboard and Hook Trap"
    while True:
        option = input(f'\nHow can I help ye?\n1. Buy cheese\n2. View inventory\n3. Leave shop\n')
        if option == "1":
            gold_spent, (cheddar_amount, marble_amount, swiss_amount) = buy_cheese(gold)
            gold -= gold_spent
            cheese[0][1] += cheddar_amount
            cheese[1][1] += marble_amount
            cheese[2][1] += swiss_amount
        elif option == "2":
            display_inventory(gold, cheese, trap)
        elif option == "3":
            break


if __name__ == '__main__':
    print(f'Welcome to The Cheese Shop!\nCheddar - 10 gold\nMarble - 50 gold\nSwiss - 100 gold')
    main()

