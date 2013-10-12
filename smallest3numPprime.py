from smallestPseudoprime import *

def smallest3numPprime(a,b,c):
    aPprime = False
    bPprime = False
    cPprim = False

    N = 3
    while not (aPprime and bPprime and cPprime):
        N = smallestPseudoprime(a,N)
        aPprime = True

        if (modExp(b,N-1,N)==1):
            bPprime = True
            if (modExp(c,N-1,N)==1):
                cPprime = True
            else:
                bPprime = False
        else:
            aPprime = False

    return N
