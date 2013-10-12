from primeTest import *
from modExp import *

def smallestPseudoprime(a, N=3):
    """This function finds the smallest pseudoprime of a.
    Starts with guess of N=4 if N not specified."""

    found=False

    while not found:
        N +=1
        if not primeTest(N):
            modval = modExp(a,N-1,N)
            if modval==1: 
                found=True
            else:
                modval=0

    return N
