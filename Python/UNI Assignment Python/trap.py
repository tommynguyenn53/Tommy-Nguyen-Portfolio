'''
Write your solution for the class Trap here.
This is your answer for Question 8.1.

Author:
SID:
Unikey:
'''


class Trap:

    def __init__(self):
        self.trap_name = ""
        self.trap_cheese = None
        self.arm_status = False
        self.one_time_enchantment = False

    def set_trap_name(self, name):
        if name == "Cardboard and Hook Trap" or name == "High Strain Steel Trap" or name == "Hot Tub Trap":
            self.trap_name = name

    def set_trap_cheese(self, cheese):
        if cheese == "Cheddar" or cheese == "Marble" or cheese == "Swiss":
            self.trap_cheese = cheese
            self.set_arm_status()

    def set_arm_status(self):
        if self.trap_cheese is None:
            self.arm_status = False
        else:
            self.arm_status = True

    def set_one_time_enchantment(self, status):
        if self.trap_cheese != "Cardboard and Hook Trap":
            self.one_time_enchantment = status
        else:
            self.one_time_enchantment = False

    def get_trap_name(self) -> str:
        return self.trap_name

    def get_trap_cheese(self) -> str:
        return self.trap_cheese

    def get_arm_status(self) -> bool:
        return self.arm_status

    def get_one_time_enchantment(self) -> bool:
        return self.one_time_enchantment

    def __str__(self) -> str:
        if self.one_time_enchantment:
            return f"One-time Enchanted {self.trap_name}"
        elif not self.one_time_enchantment:
            return f"{self.trap_name}"

