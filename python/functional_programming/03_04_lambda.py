from collections.abc import Callable

numbers_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# lambda that takes two ints and returns an int
add: Callable[[int, int], int] = lambda x, y: x + y
print(add(2, 3))

# map returns a lazy iterable, so we wrap it in list()
doubled_numbers: list[int] = list(map(lambda x: x * 2, numbers_list))
print(doubled_numbers)


# Function that returns a multiplier function (closure)
def create_multiplier(a: int) -> Callable[[int], int]:
    return lambda x: x * a


double: Callable[[int], int] = create_multiplier(2)
print(double(5))
