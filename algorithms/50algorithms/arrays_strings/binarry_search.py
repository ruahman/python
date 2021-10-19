"""
binary search
    *  only works on sorted lists
    *  there are
        -  start = 0
        -  end = 5
        -  middle = (start + end) / 2
        -  goal : 15
        -  current : 12
"""


def binary_search(arr, targ):
    """
    array must already be sorted
    this is 0(Log(N))
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targ:
            return mid

        if arr[mid] < targ:
            left = mid + 1
        else:
            right = mid - 1

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 3

result = binary_search(array, target)

if result != -1:
    print("found in index: %d" % result)
else:
    print("nothing was found")
