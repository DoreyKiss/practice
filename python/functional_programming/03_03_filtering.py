numbers_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Imperative style
even_numbers: list[int] = []
for x in numbers_list:
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)


# Functional style
def is_even(x: int) -> bool:
    return x % 2 == 0


#   Filter
# 	Applies a predicate function (returns True or False) to each item.
# 	Keeps only the items where the function returns True.
even_numbers_functional: list[int] = list(filter(is_even, numbers_list))
print(even_numbers_functional)
