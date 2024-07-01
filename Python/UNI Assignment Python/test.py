'''
Write solutions to 4. New Mouse Release here.

Author: Tommy Nguyen
SID: 530509598
Unikey: tong9587
'''



'''
Keep this line!
'''
import random

TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")


def generate_mouse() -> str | None:
    x = random.random()
    if 0 <= x < 0.5:
        return f'{TYPE_OF_MOUSE[0]} - {x:.2f}'
    if 0.5 <= x < 0.6:
        return f'{TYPE_OF_MOUSE[1]} - {x:.2f}'
    if 0.6 <= x < 0.75:
        return f'{TYPE_OF_MOUSE[2]} - {x:.2f}'
    if 0.75 <= x < 0.85:
        return f'{TYPE_OF_MOUSE[3]} - {x:.2f}'
    if 0.85 <= x < 0.95:
        return f'{TYPE_OF_MOUSE[4]} - {x:.2f}'
    if 0.95 <= x < 1:
        return f'{TYPE_OF_MOUSE[5]} - {x:.2f}'


def loot_lut(mouse_type: str | None) -> tuple:
    if mouse_type == TYPE_OF_MOUSE[0]:
        return 0, 0
    if mouse_type == TYPE_OF_MOUSE[1]:
        return 125, 115
    if mouse_type == TYPE_OF_MOUSE[2]:
        return 200, 200
    if mouse_type == TYPE_OF_MOUSE[3]:
        return 125, 90
    if mouse_type == TYPE_OF_MOUSE[4]:
        return 100, 70
    if mouse_type == TYPE_OF_MOUSE[5]:
        return 900, 200


class Mouse:
    def __init__(self):
        name = generate_mouse()
        gold, points = loot_lut(None)
        self.name = name
        self.gold = gold
        self.points = points
        i = 0
        while i < 100:
            i += 1
            print(generate_mouse())

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold

    def get_points(self) -> int:
        return self.points

    def __str__(self) -> str:
        return f"{self.name}"


mouse = Mouse()

