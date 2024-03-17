#!/usr/bin/python3

import math
import sys
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    stack: int
    amount: int

ITEMS = (
    Item("Science Red", 200, 25),
    Item("Science Green", 200, 25),
    Item("Science Blue", 200, 25),
    Item("Science Dark", 200, 25),
    Item("Science Yellow", 200, 25),
    Item("Stone", 50, 25),
    Item("Rocket Fuel", 10, 5),
    Item("Processor", 100, 5),
    Item("Small Motor", 50, 20),
    Item("Steel", 100, 17),
    Item("Density", 50, 10),
    Item("Water", 10, 1),
    Item("Lubricant", 10, 2),
)

STORAGE = 500
MULTIPLIER = int(sys.argv[1])
taken_space = 0

for item in ITEMS:
    total_amount = item.amount * MULTIPLIER
    total_space = math.ceil(total_amount / item.stack)
    taken_space += total_space
    print(item.name, total_amount, total_space)

print("Space taken:", taken_space)

