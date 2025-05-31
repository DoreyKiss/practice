from collections.abc import Callable


def create_printer() -> Callable[[], None]:
    my_favorite_number = 42

    def printer() -> None:
        print(f"My favorite number is {my_favorite_number}")

    return printer


my_printer = create_printer()
my_printer()


def create_counter() -> tuple[Callable[[], int], Callable[[], None]]:
    count = 0

    def get_count() -> int:
        return count

    def increment() -> None:
        nonlocal count
        count += 1

    return (get_count, increment)


get_count, increment = create_counter()

print(get_count())
increment()
increment()
print(get_count())
increment()
increment()
increment()
print(get_count())
