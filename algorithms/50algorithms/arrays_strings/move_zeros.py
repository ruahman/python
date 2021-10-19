"""Move zeros to end of array."""


def move_zeros(nums):
    """Move zeros to end."""
    j = 0
    n = len(nums)
    for num in nums:
        if(num != 0):
            nums[j] = num
            j += 1

    for x in range(j, n):
        nums[x] = 0


nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums)
