numbers_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Imperative approach
doubled_list: list[int] = []
for x in numbers_list:
    doubled_list.append(x * 2)

print(doubled_list)


# Functional approach with a typed function
def double(x: int) -> int:
    return x * 2


#   MAP
#   Applies a function to each item in an iterable.
# 	Returns a new iterable (a map object, which is lazy — you often convert it to a list).
doubled_list_functional: list[int] = list(map(double, numbers_list))
print(doubled_list_functional)
