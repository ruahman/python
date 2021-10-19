"""Find first bad version."""


def is_bad_version(version):
    """Return if badVersion."""
    badVersion = 3
    return version >= badVersion


def find_first_bad_version(n: int) -> int:
    """Find first bad version."""
    left = 1
    right = n

    while(left < right):
        mid = (right + left)//2
        if(not is_bad_version(mid)):
            left = mid + 1
        else:
            right = mid

    return left


answer = find_first_bad_version(10)
print(f"answer: {answer}")
