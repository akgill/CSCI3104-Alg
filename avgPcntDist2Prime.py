from getrand100 import *
from nextprime import *

def avgPcntDist2Prime(nSamp=1000):
    """ This function computes the average percent distance
    to the next prime number in the range 0 to 10**101 - 1 by
    taking the average percent distance over nSamp samples."""

    arr = []
    for i in range(1,nSamp):
        s = getrand100()
        arr.append((nextprime(s)-s)/s)

    return (sum(arr)/nSamp)
