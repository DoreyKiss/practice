from collections.abc import Callable


# Function that returns a function with no parameters and no return value
def create_printer() -> Callable[[], None]:
    def printer() -> None:
        print("Hello functional!")

    return printer


my_printer = create_printer()
my_printer()


# Function that returns a function taking an int and returning an int
def create_multiplier(a: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * a

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(5))  # 10
print(triple(6))  # 18
print(quadruple(7))  # 28
