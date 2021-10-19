"""The sliding window problem."""


def maximum_sum(arr, window_size):
    """
    Find the max sum of consec nums in array.

    Only looping throught the array once.
    """
    array_size = len(arr)

    # windows size can not be bigger than array
    if array_size <= window_size:
        print("Invalid opperation")
        return -1

    # first window sum
    window_sum = sum([arr[i] for i in range(window_size)])
    max_sum = window_sum

    # we just have to go throught the loop once
    for i in range(array_size - window_size):
        # subtract last value add new one
        window_sum = window_sum - arr[i] + arr[i + window_size]
        max_sum = max(window_sum, max_sum)

    return max_sum


array = [80, -50, 90, 100]
consecutive = 2
answer = maximum_sum(array, consecutive)

print(answer)
