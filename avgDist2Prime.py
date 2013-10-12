from getrand100 import *
from nextprime import *

def avgDist2Prime(nSamp=1000):
    """ This function computes the average numerical distance
    to the next prime number in the range 0 to 10**101 - 1 by
    taking the average over nSamp samples."""

    # computes the average as a running sum to improve
    # computation
    avg = 0
    for i in range(1,nSamp):
        s = getrand100()
        avg += (nextprime(s)-s)/nSamp

    return avg
