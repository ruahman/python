"""Find the primes."""
import math


def find_primes(num: int):
    """Find the primes."""
    if(num < 2):
        return 0
    isPrime = [True] * num
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, int(math.ceil(math.sqrt(num)))):
        if(isPrime[i]):
            for mult_of_i in range(i*i, num, i):
                isPrime[mult_of_i] = False

    return sum(isPrime)


answer = find_primes(12)
print(f"answer: {answer}")
