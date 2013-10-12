import random

def getrand100():
    """This function produces a random 100 digit decimal number."""
    return random.randint(0, ((10**101) - 1))
