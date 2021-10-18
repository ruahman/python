"""Boats to save people."""
from typing import List


def num_of_boats(people: List[int], limit: int) -> int:
    """Find number of boats needed."""
    left = 0
    right = len(people) - 1
    boats_number = 0

    # sort people from heviest to lightest
    people.sort()

    while(left <= right):
        if(left == right):
            boats_number += 1
            break

        # move left pointer, next lightest
        if(people[left]+people[right] <= limit):
            left += 1

        # move right pointer, next heviest
        right -= 1
        boats_number += 1

    return boats_number


res = num_of_boats([2, 1, 3, 4], 4)
print(f"number of boats: {res}")
