"""Find the number that was not repeated."""


def find_number(nums: list[int]) -> int:
    """Find the number that was not repeated."""
    numberSet = set(nums)
    res = 2*sum(numberSet) - sum(nums)
    return res


res = find_number([2, 2, 1])
print(f"missing number: {res}")
