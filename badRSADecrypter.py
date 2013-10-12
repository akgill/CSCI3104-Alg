from euclidsExtended import *
from modExp import *

def badRSADecrypter(p,e,encryptedMessage):
    """This code decrypts a message encoded with N = p
    rather than with N = pq where p and q are both primes."""

    phi = p-1

    # Euclid's extended algorithm runs in Theta(n^3)
    (gcd, x, y) = euclidsExtended(e,phi)
    
    if gcd == 1:
        eInverse = x
    else:
        print("Your e and phi are not coprime!")
        return []

    # modular exponentiation runs in Theta(n^3)
    # computes encryptedMessage^{eInverse} mod phi
    decryptedMessage = modExp(encryptedMessage,eInverse,phi)
    return decryptedMessage
