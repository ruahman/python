"""Find the missing number."""


def missing_number(nums: list[int]) -> int:
    """Find missing number."""
    currentSum: int = sum(nums)
    n = len(nums)
    intendedSum = n*(n+1)/2
    return int(intendedSum - currentSum)


answer = missing_number([0, 3, 1, 2, 5])
print(f"answer: {answer}")
