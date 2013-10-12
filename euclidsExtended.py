def euclidsExtended(a,b):
    """This function computes d = gcd(a,b) and also returns the values
    x and y that satisfy x*a + y*b = d."""

    if b==0:
        return (a, 1, 0)
    
    (d, xx, yy) = euclidsExtended(b, a % b)
    return (d, yy, xx - (a//b)*yy)
