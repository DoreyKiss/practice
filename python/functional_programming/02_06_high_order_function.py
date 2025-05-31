from collections.abc import Callable
from typing import ParamSpec, TypeVar

# Represent any return type of the wrapped function
R = TypeVar("R")
# Represent the argument specification of the wrapped function
P = ParamSpec("P")


def divide(x: float, y: float) -> float:
    return x / y


def second_argument_is_not_zero(func: Callable[P, R]) -> Callable[P, R | None]:
    def safe_version(*args: P.args, **kwargs: P.kwargs) -> R | None:
        if len(args) > 1 and args[1] == 0:
            print("Warning: second argument is zero")
            return None
        return func(*args, **kwargs)

    return safe_version


divide_safe = second_argument_is_not_zero(divide)

print(divide_safe(10, 2))  # Output: 5.0
print(divide_safe(10, 0))  # Output: Warning + None
