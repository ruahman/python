"""
this is big o stuff.

f(n) = n
f(n) = n^2
f(n) = 1

O(1) # constant complexity
O(n) # linear complexity

O(aN+b) = O(N)

5N² + 3N + 1 = O(N²)

space complexity
    *  how much memeory do we consume

logarithms :
    *  log₂(16) = 4
    *  2^4 = 16
    *  how many times does 2 have to divied into 16 till it reaches near the
        value of one
        -  2/16 = 8
        -  2/8 = 4
        -  2/4 = 2
        -  2/2 = 1
            >  total of 4 times

O(1) < O(log₂(N)) < O(N)

o(N) < O(Nlog₂(N)) < O(n^2)

Binary search = O(log₂(N))

Merge sort = O(NLog(N))
"""


def sum_up_to_constant(num):
    """Func is always O(1)."""
    return num * (num + 1) / 2


def Dum_up_to_linear(num):
    """
    This is O(n) : leanear

    asdf
    """
    mysum = 0

    for i in range(0, num + 1):
        mysum += i
    return mysum


def sum_up_to_linear_2(num):
    """Also just O(n)."""
    for i in range(0, num):
        print(i)

    for i in range(num, 0, -1):
        print(i)


def quadratic(num):
    """this is O(n²) : this is quadratic complexity"""
    for i in range(0, num):
        for j in range(0, num):
            print(i, j)


def sum_up_to_space(num):
    """
    this has a space complexity of O(1)
    more memory is not created from size of input
    """
    sum_of_num = 0
    size = len(num)
    for i in range(0, size):
        sum_of_num += i
    return sum_of_num


def get_arr_up_to(num):
    """
    this is space complexity of O(n)
    since we allocate base on size of array
    """
    arr = []
    for i in range(0, num):
        arr.append(i)
    return arr
