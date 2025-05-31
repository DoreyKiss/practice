from functools import reduce

numbers_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_sum(acc: int, x: int) -> int:
    # This function takes two numbers and returns their sum.
    # It's used by `reduce` to add up all the numbers in the list one by one.
    print(f"acc is {acc}, x is {x}")
    return acc + x


# reduce takes the get_sum function and applies it to the list from left to right:
# Step 1: get_sum(0, 1) → 1
# Step 2: get_sum(1, 2) → 3
# Step 3: get_sum(3, 3) → 6
# ... and so on, until it goes through the entire list.
# It "reduces" the list to a single value — the total sum.
sum_result: int = reduce(get_sum, numbers_list)

print(sum_result)
