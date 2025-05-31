from collections.abc import Callable


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def combine_2_and_3(func: Callable[[float, float], float]) -> float:
    return func(2, 3)


print(combine_2_and_3(min))


def combine_names(func: Callable[[str, str], str]) -> str:
    return func("Shaun", "Wassell")


def append_with_space(str1: str, str2: str) -> str:
    return f"{str1} {str2}"


def get_government_form_notation(first: str, last: str) -> str:
    return f"{last.upper()}, {first.upper()}"


print(combine_names(get_government_form_notation))
