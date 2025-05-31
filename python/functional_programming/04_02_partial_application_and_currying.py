from collections.abc import Callable
from functools import partial


# A simple function that adds three integers
def add(x: int, y: int, z: int) -> int:
    return x + y + z


# Partial application using a custom nested function
def add_partial(x: int) -> Callable[[int, int], int]:
    def add_others(y: int, z: int) -> int:
        return x + y + z

    return add_others


add_5 = add_partial(5)  # Fixes x = 5
print(add_5(6, 7))  # Output: 18 (5 + 6 + 7)


# Partial application with two fixed parameters
def add_partial_2(x: int, y: int) -> Callable[[int], int]:
    def add_others(z: int) -> int:
        return x + y + z

    return add_others


add_5_and_6 = add_partial_2(5, 6)  # Fixes x = 5 and y = 6
print(add_5_and_6(7))  # Output: 18 (5 + 6 + 7)


# Fully curried version: each function takes one argument
def curry_add(x: int) -> Callable[[int], Callable[[int], int]]:
    def curry_add_inner(y: int) -> Callable[[int], int]:
        def curry_add_inner_2(z: int) -> int:
            return x + y + z

        return curry_add_inner_2

    return curry_add_inner


add_5 = curry_add(5)  # Returns a function expecting y
add_5_and_6 = add_5(6)  # Returns a function expecting z
print(add_5_and_6(7))  # Output: 18

print(curry_add(5)(6)(7))  # Output: 18 (all in one line)

# Using functools.partial to fix the first argument
add_5 = partial(add, 5)  # Fixes x = 5
print(add_5(6, 7))  # Output: 18
