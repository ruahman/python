"""check if array is a mountain array."""


def mountain_array(array: list[int]) -> bool:
    """
    Check if is array is a mountain array.

    It incresses then decresses.
    """
    if(len(array) < 3):
        return False

    i = 1
    # array is incressing
    while(i < len(array) and array[i] > array[i-1]):
        i += 1

    if(i == 1):
        return False

    if(i == 1 or i == len(array)):
        return False

    # array is decressing
    while(i < len(array) and array[i] < array[i-1]):
        i += 1

    return i == len(array)


res = mountain_array([1, 1, 2, 3, 1])

print(f"mountain array: {res}")

res = mountain_array([0, 1, 2, 3, 1])

print(f"mountain array: {res}")
