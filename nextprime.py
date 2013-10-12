from primeTest import *

def nextprime(i):
    """This function returns the smallest prime greater than i."""

    # 2 is the only even prime, a special case
    if i == 2: return i

    # start with the first odd number >= i
    num = i + 1 - (i%2)

    isPrime = False
    while not isPrime:
        isPrime = primeTest(num)
        num += 2

    return (num - 2)
