"""Get subsets."""


def subsets(nums: list[int]) -> list[list[int]]:
    """Return subsets of list."""
    ans: list[list[int]] = []

    # current options already taken
    cur: list[int] = []

    recursive_subsets(nums, ans, cur, 0)

    return ans


def recursive_subsets(nums: list[int], ans: list[list[int]],
                      cur: list[int], index) -> None:
    """Recursivly find subsets."""

    # we went through all numbers
    if(index > len(nums)):
        return

    ans.append(cur[:])
    for i in range(index, len(nums)):
        # is num is not currently in selected list
        if(nums[i] not in cur):
            cur.append(nums[i])
            recursive_subsets(nums, ans, cur, i)
            cur.pop()


res = subsets([1, 2])

print(f"subsets: {res}")

res = subsets([1, 2, 3])

print(f"subsets: {res}")
