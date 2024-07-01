CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))


def buy_cheese(gold: int) -> tuple:
    while True:
        print(f'You have {gold} gold to spend.')
        purchase = input("State [cheese quantity]: ").split()
        cheese_type = purchase[0]
        while True:
            if len(purchase) == 1:
                if cheese_type == "back":
                    return 0, (0, 0, 0)
                if cheese_type != "cheddar" and cheese_type != "marble" and cheese_type != "swiss":
                    print(f"We don't sell {cheese_type}!")
                    buy_cheese(gold)
                    return 0, (0, 0, 0)
                else:
                    print("Missing quantity.")
                    buy_cheese(gold)
                    return 0, (0, 0, 0)
            if len(purchase) == 2:
                cheese_amount = int(purchase[1])
                cheese_total = 0
                cheese_total += cheese_amount
                total_cheddar_cost = cheese_amount * CHEESE_MENU[0][1]
                total_marble_cost = cheese_amount * CHEESE_MENU[1][1]
                total_swiss_cost = cheese_amount * CHEESE_MENU[2][1]
                if cheese_type != "cheddar" and cheese_type != "marble" and cheese_type != "swiss":
                    print(f"We don't sell {cheese_type}!")
                    return 0, (0, 0, 0)
                if cheese_amount <= 0 and cheese_type == "cheddar":
                    print("Must purchase positive amount of cheese.")
                    return 0, (0, 0, 0)
                if cheese_amount <= 0 and cheese_type == "marble":
                    print("Must purchase positive amount of cheese.")
                    return 0, (0, 0, 0)
                if cheese_amount <= 0 and cheese_type == "swiss":
                    print("Must purchase positive amount of cheese.")
                    return 0, (0, 0, 0)
                elif cheese_type == "cheddar" and total_cheddar_cost <= gold:
                    gold -= total_cheddar_cost
                    print(f'Successfully purchase {cheese_amount} cheddar.')
                    return total_cheddar_cost, (cheese_total, 0, 0)
                elif cheese_type == "marble" and total_marble_cost <= gold:
                    gold -= total_marble_cost
                    print(f'Successfully purchase {cheese_amount} marble.')
                    return total_marble_cost, (0, cheese_total, 0)
                elif cheese_type == "swiss" and total_swiss_cost <= gold:
                    gold -= total_swiss_cost
                    print(f'Successfully purchase {cheese_amount} swiss.')
                    return total_swiss_cost, (0, 0, cheese_total)
                else:
                    print("Insufficient gold.")
                    buy_cheese(gold)
                    return 0, (0, 0, 0)


def test1():
    check1 = buy_cheese(125)
    assert check1 == (50, (5, 0, 0)), "cheddar 5"
    print("Testcase 1 for buy_cheese passed")


def test2():
    check2 = buy_cheese(300)
    assert check2 == (200, (0, 0, 2)), "swiss 2"
    print("Testcase 2 for buy_cheese passed")


def test3():
    check3 = buy_cheese(10)
    assert check3 == (0, (0, 0, 0)), "cheddar -1"
    print("Testcase 3 for buy_cheese passed")


def test4():
    check4 = buy_cheese(50)
    assert check4 == (0, (0, 0, 0)), "brie 5"
    print("Testcase 4 for buy_cheese passed")


def test5():
    check5 = buy_cheese(500)
    assert check5 == (500, (0, 0, 2)), "cheddar 50"
    print("Testcase 5 for buy_cheese passed")


def test6():
    check6 = buy_cheese(0)
    assert check6 == (0, (0, 0, 0)), "cheddar 1"
    print("Testcase 6 for buy_cheese passed")




