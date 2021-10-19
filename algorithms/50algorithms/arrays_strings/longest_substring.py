"""What is the longest substring."""


def longest_string(string: str) -> int:
    """Find size of longest substring."""
    map: dict = dict()
    left = 0
    right = 0
    ans = 0
    size = len(string)

    while(left < size and right < size):
        el = string[right]
        if(el in map):
            left = max(left, map[el] + 1)
        map[el] = right
        ans = max(ans, right - left + 1)
        right += 1

    return ans


ans = longest_string("fivestarreview")
print(f"longest string: {ans}")
