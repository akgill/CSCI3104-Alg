def modExp(x,y,N):
    """This function computes x^y mod N. """
    
    if y==0: return 1
    
    z = modExp(x,y//2,N)
    
    if ((y % 2) == 0): return ((z**2) % N)
    else: return ((x * z**2) % N)
