def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
    print(
        f'Hunter {hunter_name}, you currently have:\nCheddar - {cheese[0][1]}\nMarble - {cheese[1][1]}'
        f'\nSwiss - {cheese[2][1]}')
    arm_cheese = input("\nType cheese name to arm trap: ")
    if e_flag:
        return False, None
    if arm_cheese == "back":
        return hunter_name, trap, cheese, False
    if arm_cheese == "cheddar" and cheese[0][1] > 0:
        are_you_sure = input(f'Do you want arm your trap with Cheddar? ')
        if are_you_sure == "yes":
            print(f'{trap} is now armed with Cheddar!')
            return True, arm_cheese
        if are_you_sure == "no":
            change_cheese(hunter_name, trap, cheese, False)
            return False, None
    if arm_cheese == "marble" and cheese[1][1] > 0:
        are_you_sure = input(f'Do you want arm your trap with Marble? ')
        if are_you_sure == "yes":
            print(f'{trap} is now armed with Marble!')
            return True, arm_cheese
        if are_you_sure == "no":
            return False, None
    if arm_cheese == "swiss" and cheese[2][1] > 0:
        are_you_sure = input(f'Do you want arm your trap with Swiss? ')
        if are_you_sure == "yes":
            print(f'{trap} is now armed with Swiss!')
            return True, arm_cheese
        if are_you_sure == "no":
            return False, None
    if arm_cheese == "cheddar" and cheese[0][1] > 0:
        print("Out of cheese!")
        return False, None
    if arm_cheese == "marble" and cheese[1][1] <= 0:
        print("Out of cheese!")
        return False, None
    if arm_cheese == "swiss" and cheese[2][1] <= 0:
        print("Out of cheese!")
        return False, None
    if arm_cheese == "cheddar" and cheese[0][1] <= 0:
        print("Out of cheese!")
        return False, None
    if arm_cheese == "marble" and cheese[1][1] <= 0:
        print("Out of cheese!")
        return False, None
    if arm_cheese == "swiss" and cheese[2][1] <= 0:
        print("Out of cheese!")
        return False, None
    if arm_cheese != "cheddar" and arm_cheese != "marble" and arm_cheese != "swiss":
        print("No such cheese!")
        return False, None


def test1():
    check1 = change_cheese("info1110", "Cardboard and Hook Trap", [["cheddar", 6], ["marble", 2], ["swiss", 4]], e_flag= False)
    assert check1 == (True, "cheddar")
    print("Testcase 1 for change_cheese passed")


def test2():
    check2 = change_cheese("info1110", "Cardboard and Hook Trap", [["cheddar", 1], ["marble", 0], ["swiss", 1]], e_flag = False)
    assert check2 == (True, "swiss")
    print("Testcase 2 for change_cheese passed")


def test3():
    check3 = change_cheese("info1110", "Cardboard and Hook Trap", [["cheddar", -10], ["marble", 0], ["swiss", 0]], e_flag = False)
    assert check3 == (False, None)
    print("Testcase 3 for change_cheese passed")


def test4():
    check4 = change_cheese("info1110", "Cardboard and Hook Trap", [["cheddar", 4], ["marble", 4], ["swiss", 4]], e_flag = False)
    assert check4 == (False, None)
    print("Testcase 4 for change_cheese passed")


def test5():
    check5 = change_cheese("info1110", "Cardboard and Hook Trap", [["cheddar", 10], ["marble", 10], ["swiss", 10]], e_flag = False)
    assert check5 == (False, None)
    print("Testcase 5 for change_cheese passed")


def test6():
    check6 = change_cheese("info1110", "Cardboard and Hook Trap", [["cheddar", 0], ["marble", 0], ["swiss", 0]], e_flag = False)
    assert check6 == (False, None)
    print("Testcase 6 for change_cheese passed")



