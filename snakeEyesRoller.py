import random

def snakeEyesRoller():
    """This function tells you how many rolls it made before 
    getting snake-eyes."""

    count=0
    snakeEyes=False

    while not snakeEyes:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if (die1==1 and die2==1):
            snakeEyes=True
        count += 1 

    return count
