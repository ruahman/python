"""Max water that can be contained."""


def max_water_contain(heights: list[int]) -> int:
    """Find max water that can be contained."""
    maxarea = 0
    left = 0
    right = len(heights) - 1

    while(left < right):
        newMaxarea = min(heights[left], heights[right])*(right-left)
        maxarea = max(maxarea, newMaxarea)
        if(heights[left] < heights[right]):
            left += 1
        else:
            right -= 1

    return maxarea


res = max_water_contain([2, 1, 1, 2])
print(f"maxArea: {res}")
