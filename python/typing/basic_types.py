import math

name: str = input("Enter your name: ")
print("Hello, ", name)

print("-----------")

for i in range(5):
    print(i)


print("-----------")
for i in range(10, 5, -1):
    print(i)

print("-----------")

x: int = 0
while x < 5:
    print(x)
    x += 1

print("-----------")


def great(name: str = "Great"):
    return f"Hello, {name}!"


print("-----------")
# Lists are ordered, mutable collection
my_list: list[int] = [1, 2, 3]
my_list.append(0)

print(f"Before sorting: {my_list}")
my_list.sort()
print(f"Sorted list: {my_list}")

my_list.reverse()
print(f"Reversed list: {my_list}")

popped_value = my_list.pop()
print(f"Popped value: {popped_value}")
print(f"List after popping the last value: {my_list}")

popped_value = my_list.pop(0)
print(f"Popped the first element: {popped_value}")
print(f"List after popping the first value: {my_list}")
print(*my_list)

print("-----------")

mixed_list = [1, "apple", 3, "banana", 5]
mixed_list.append("a")
print(mixed_list)


print("-----------")


numbers: list[int] = [0, 1, 2, 3, 4, 5]
print(numbers[2:5])
print(numbers[:3])
print(numbers[-2:])

num_and_string: list[int | str] = ["no", 1, "knows", 3, "what", 4]
print(num_and_string)
num_and_string.sort(key=str)
print(num_and_string)

print("-----------")

my_dict: dict[str, float] = {"a": 1, "b": 2, "c": 3}
person: dict[str, str | int] = {"name": "Alice", "age": 30, "city": "New York"}

print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 30

person["age"] = 31
print(person)

print("-----------")

my_tuple: tuple = (1, 2, 3, 4, 5)

# For tuples of fixed size, we specify the types of all the elements
fixed_sized_tuple: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+

# For tuples of variable size, we use one type and ellipsis
variable_sized_tuple: tuple[int, ...] = (1, 2, 3)  # Python 3.9+

print("-----------")

my_set = {1, 2, 3}

print("-----------")


def calculate_area(radius: float):
    """Calculate area of a circle."""
    return math.pi * radius * radius


print(f"{calculate_area(20)}")

print("-----------")
