import math

numbers_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

doubled: list[int] = [x * 2 for x in numbers_list]
print(doubled)

minus_one: list[int] = [x - 1 for x in numbers_list]
print(minus_one)

factorial: list[int] = [math.factorial(x) for x in numbers_list]

evens: list[int] = [x for x in numbers_list if x % 2 == 0]
print(evens)
