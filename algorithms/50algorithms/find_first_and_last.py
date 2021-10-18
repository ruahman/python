"""Find first and last position of elemente in sorted array."""

# import ipdb


def find_first_and_last(nums: list[int], target: int) -> list[int]:
    """Find first and last index of target."""
    left = get_left_position(nums, target)
    right = get_right_position(nums, target)

    return [left, right]


def get_left_position(nums: list[int], target: int) -> int:
    """Get left position of target."""
    left = 0
    right = len(nums) - 1

    while(left <= right):
        mid = (left+right)//2
        if(nums[mid] == target):
            if(mid-1 >= 0 and nums[mid-1] != target or mid == 0):
                return mid
            right = mid - 1
        elif(nums[mid] > target):
            right = mid - 1
        else:
            left = mid + 1

    return -1


def get_right_position(nums: list[int], target: int) -> int:
    """Get right position of target."""
    left = 0
    right = len(nums) - 1

    while(left <= right):
        mid = (left+right)//2
        if(nums[mid] == target):
            if(mid + 1 < len(nums)
                    and nums[mid+1] != target
                    or mid == len(nums)-1):
                return mid
            left = mid+1
        elif(nums[mid] > target):
            right = mid - 1
        else:
            left = mid + 1

    return -1


# ipdb.set_trace()
res = find_first_and_last([1, 2, 2, 3, 4, 4, 4, 4], 4)
print(f"first and last: {res}")
