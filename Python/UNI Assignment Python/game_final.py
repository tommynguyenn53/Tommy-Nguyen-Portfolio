'''
Answer for Question 7 - PIAT: Improved Full Game.

Author:
SID:
Unikey:
'''

import random

title = "Mousehunt\n"
logo = '''       ____()()
      /      @@
`~~~~~\_;m__m._>o\n'''
author = " An INFO1110/COMP9001 Student"
credits = f"Inspired by Mousehunt© Hitgrab\nProgrammer -{author}\nMice art - Joan Stark and Hayley Jane Wakenshaw"

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
                print("Must purchase a positive amount of cheese.")
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


def cheese_shop_menu(hunter_name):
    print(f'\nWelcome to The Cheese Shop!\nCheddar - 10 gold\nMarble - 50 gold\nSwiss - 100 gold')
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
            get_game_menu(hunter_name, gold, cheese, trap)
        else:
            print("I did not understand.")


def is_valid_name(name: str) -> tuple:
    if 9 >= len(name) >= 1 == len(name.split()) and name[0].isalpha():
        message = f'Welcome to the Kingdom, Hunter {name}!'
    else:
        name = "Bob"
        message = f'Welcome to the Kingdom, Hunter {name}!'
    return name, message


def training(hunter_name):
    print("Before we begin, let's train you up!")
    skip = input(f'Press "Enter" to start training or "skip" to Start Game: ')
    if skip == "skip":
        get_game_menu(hunter_name, 0, [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]], "Cardboard and Hook Trap")
    while True:
        print("\nLarry: I'm Larry. I'll be your hunting instructor.")
        print("Larry: Let's go to the Meadow to begin your training!")
        travel = input("Press Enter to travel to the Meadow...")
        if travel and ord(travel[0]) == 27:
            get_game_menu(hunter_name, 0, [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]], "Cardboard and Hook Trap")
        else:
            print("Travelling to the Meadow...")
            print("Larry: This is your camp. Here you'll set up your mouse trap.")
            trap = input(
                "Larry: Let\'s get your first trap...\nPress Enter to view traps that Larry is holding...").strip()
            if trap and ord(trap[0]) == 27:
                get_game_menu(hunter_name, 0, [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]], "Cardboard and Hook Trap")
            else:
                print(f'Larry is holding...\nLeft: High Strain Steel Trap\nRight: Hot Tub Trap')
                hand = input(f'Select a trap by typing "left" or "right": ').strip()
                if hand == 'left':
                    print('Larry: Excellent choice.\nYour "High Strain Steel Trap" is now set!')
                    print("Larry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!")
                elif hand == 'right':
                    print('Larry: Excellent choice.\nYour "Hot Tub Trap" is now set!')
                    print("Larry: You need cheese to attract a mouse.\nLarry places one cheddar on the trap!")
                elif hand and hand[0] == chr(27):
                    get_game_menu(hunter_name, 0, [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]],
                                  "Cardboard and Hook Trap")
                else:
                    print('Invalid command! No trap selected.\nLarry: Odds are slim with no trap!')
                    continue

                print("Sound the horn to call for the mouse...")
                sound_answer = input(f'Sound the horn by typing "yes": ')
                if hand == "left" and sound_answer == "yes":
                    print("Caught a Brown mouse!\nCongratulations. Ye have completed the training.\nGood luck~")
                elif hand == "right" and sound_answer == "yes":
                    print("Caught a Brown mouse!\nCongratulations. Ye have completed the training.\nGood luck~")
                elif hand == "left" and sound_answer != "yes":
                    print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
                elif hand == "right" and sound_answer != "yes":
                    print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
                elif hand != "left" and sound_answer == "yes":
                    print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
                elif sound_answer and ord(sound_answer[0]) == 27:
                    get_game_menu(hunter_name, 0, [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]],
                                  "Cardboard and Hook Trap")
                else:
                    print("Nothing happens.")

                restart = input(f'\nPress Enter to continue training and "no" to stop training: ')
                if restart == "":
                    continue
                if restart == "no" or ord(sound_answer[0]) == 27:
                    get_game_menu(hunter_name, 0, [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]],
                                  "Cardboard and Hook Trap")


def get_game_menu(hunter_name, gold: int, cheese: list, trap: str):
    print(
        f'\nWhat do ye want to do now, Hunter {hunter_name}?\n1. Exit game\n2. Join the Hunt\n3. '
        f'The Cheese Shop\n4. Change Cheese')
    while True:
        menu_options = input(f'Enter a number between 1 and 4: ')
        if menu_options == "1":
            quit()
        if menu_options == "2":
            starting_points = 0
            points = starting_points
            added_gold = gold
            added_gold, points = hunt(125, cheese, None, points)
            points += starting_points
            added_gold += gold
        if menu_options == "3":
            cheese_shop_menu(hunter_name)
        if menu_options == "4":
            change_cheese(hunter_name, trap, cheese, False)
        else:
            try:
                int(menu_options)
                print("Must be between 1 and 4.")
            except ValueError:
                print("Invalid input.")


def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
    print(
        f'Hunter {hunter_name}, you currently have:\nCheddar - {cheese[0][1]}\nMarble - {cheese[1][1]}'
        f'\nSwiss - {cheese[2][1]}')
    while True:
        arm_cheese = input("\nType cheese name to arm trap: ").lower()
        if arm_cheese == "back":
            return hunter_name, trap, cheese, False
        if arm_cheese == "cheddar" and cheese[0][1] > 0:
            are_you_sure = input(f'Do you want to arm your trap with Cheddar? ')
            if are_you_sure == "yes":
                print(f'{trap} is now armed with Cheddar!')
                return True, arm_cheese
            if are_you_sure == "no":
                print(
                    f'\nHunter {hunter_name}, you currently have:\nCheddar - {cheese[0][1]}\nMarble - {cheese[1][1]}'
                    f'\nSwiss - {cheese[2][1]}')
                continue
        elif arm_cheese == "marble" and cheese[1][1] > 0:
            are_you_sure = input(f'Do you want to arm your trap with Marble? ')
            if are_you_sure == "yes":
                print(f'{trap} is now armed with Marble!')
                return True, arm_cheese
            if are_you_sure == "no":
                change_cheese(hunter_name, trap, cheese, False)
        elif arm_cheese == "swiss" and cheese[2][1] > 0:
            are_you_sure = input(f'Do you want to arm your trap with Swiss? ')
            if are_you_sure == "yes":
                print(f'{trap} is now armed with Swiss!')
                return True, arm_cheese
            if are_you_sure == "no":
                change_cheese(hunter_name, trap, cheese, False)
        elif arm_cheese == "cheddar" and cheese[0][1] > 0:
            print("Out of cheese!")
            change_cheese(hunter_name, trap, cheese, False)
            return False, None
        elif arm_cheese == "marble" and cheese[1][1] <= 0:
            print("Out of cheese!")
            change_cheese(hunter_name, trap, cheese, False)
            return False, None
        elif arm_cheese == "swiss" and cheese[2][1] <= 0:
            print("Out of cheese!")
            change_cheese(hunter_name, trap, cheese, False)
            return False, None
        elif arm_cheese == "cheddar" and cheese[0][1] <= 0:
            print("Out of cheese!")
            change_cheese(hunter_name, trap, cheese, False)
            return False, None
        elif arm_cheese == "marble" and cheese[1][1] <= 0:
            print("Out of cheese!")
            change_cheese(hunter_name, trap, cheese, False)
            return False, None
        elif arm_cheese == "swiss" and cheese[2][1] <= 0:
            print("Out of cheese!")
            change_cheese(hunter_name, trap, cheese, False)
            return False, None
        elif arm_cheese != "cheddar" and arm_cheese != "marble" and arm_cheese != "swiss":
            print("No such cheese!")
            change_cheese(hunter_name, trap, cheese, False)
            return False, None


def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int) -> tuple:
    while True:
        i = 0
        while i < 5:
            print("Sound the horn to call for the mouse...")
            sound_horn = input(f'Sound the horn by typing "yes": ')
            if sound_horn == "stop hunt":
                break
            if sound_horn != "yes":
                print("Do nothing.")
                print(f'My gold: {gold},', f'My points: {points}')
            else:
                if len(cheese) > 0:
                    cheese_count = cheese[0][1] + cheese[1][1] + cheese[2][1]
                    if cheese_count > 0:
                        x = random.random()
                        if (cheese[0][1] > 0 and x < 0.5) or (
                                cheese[1][1] > 0 and x < 0.5) or (
                                cheese[2][1] > 0 and x < 0.5):
                            print("Caught a Brown mouse!")
                            gold += 125
                            points += 115
                            if cheese[0][1] > 0:
                                cheese[0][1] -= 1
                            elif cheese[1][1] > 0:
                                cheese[1][1] -= 1
                            else:
                                cheese[2][1] -= 1
                            print(f'My gold: {gold},', f'My points: {points}')
                        else:
                            print("Nothing happens")
                            print(f'My gold: {gold},', f'My points: {points}')
                    else:
                        print("Nothing happens. You are out of cheese!")
                        print(f'My gold: {gold},', f'My points: {points}')
                else:
                    print("Nothing happens. You are out of cheese!")
                    print(f'My gold: {gold},', f'My points: {points}')
            i += 1
        if sound_horn == "stop hunt":
            break
        continue_hunting = input("Do you want to continue the hunt? ")
        if continue_hunting == "no":
            break
        else:
            continue
    return gold, points


def consume_cheese(to_eat: str, cheese: list) -> None:
    pass


def main():
    print(f'Launching game...\n.\n.\n.')
    print(title)
    print(logo)
    print(credits)
    name = str(input("\nWhat's ye name, Hunter? "))
    hunter_name, welcome_message = is_valid_name(name)
    print(welcome_message)
    training(hunter_name)


if __name__ == '__main__':
    main()

