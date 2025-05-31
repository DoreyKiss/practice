def count_down(x: int) -> None:
    if x < 0:
        print("Done!")
        return
    print(x)
    count_down(x - 1)


count_down(10)


def count_up(x: int, maximum: int) -> None:
    if x > maximum:
        print("Done!")
        return
    print(x)
    count_up(x + 1, maximum)


count_up(0, 10)
