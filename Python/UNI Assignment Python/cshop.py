class CheeseShop:

    def __init__(self):
        self.cheeses = {"Cheddar": 10, "Marble": 50, "Swiss": 100}
        self.menu = {"1.": "Buy cheese", "2.": "View inventory", "3.": "Leave shop"}

    def get_cheeses(self) -> str:
        return f'Cheddar - 10 gold\nMarble - 50 gold\nSwiss - 100 gold'

    def get_menu(self) -> str:
        return f'1. Buy cheese\n2. View inventory\n3. Leave shop'

    def greet(self) -> str:
        return f'Welcome to The Cheese Shop!\nCheddar - 10 gold\nMarble - 50 gold\nSwiss - 100 gold'

    def buy_cheese(self, gold) -> tuple:
        gold = 125
        print(f'You have {gold} gold to spend.')
        purchase = input("State [cheese quantity]: ").split()
        cheese_type = purchase[0]
        if len(purchase) == 1:
            if cheese_type == "back":
                return 125, (0, 0, 0)
        if cheese_type != "cheddar" and cheese_type != "marble" and cheese_type != "swiss":
            print(f"We don't sell {cheese_type}!")
            return 125, (0, 0, 0)
        else:
            print("Missing quantity.")
            return 125, (0, 0, 0)

    def move_to(self):
        print(f'\nWelcome to The Cheese Shop!\nCheddar - 10 gold\nMarble - 50 gold\nSwiss - 100 gold')
        while True:
            option = input(f'\nHow can I help ye?\n1. Buy cheese\n2. View inventory\n3. Leave shop\n')
            
