import math
from collections.abc import Callable


def double(x: float) -> float:
    return x * 2


def minus_one(x: float) -> float:
    return x - 1


def squared(x: float) -> float:
    return x * x


function_list: list[Callable[[float], float]] = [
    squared,
    double,
    minus_one,
    math.sqrt,
]

my_number: float = 3

for func in function_list:
    my_number = func(my_number)

print(my_number)
