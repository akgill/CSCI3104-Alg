import random
from modExp import modExp

def primeTest(N, nIts=100):
    """This function uses the converse of Fermat's Little Theorem 
    applied nIts times to a number, N, to check if
    N is prime to within a probability of 2**(-100)"""

    prime = True
    counter = 0
    while (prime and (counter < nIts)):
        a = random.randint(1,N-1)
        modval = modExp(a,N-1,N)

        if modval != 1: prime=False

        counter += 1

    return prime
