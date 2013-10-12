from snakeEyesRoller import *

def snakeEyesMonteCarlo(nIts):
    """This program calls snakeEyesRoller nIts number of times and
    reports the average number of rolls it takes to get snake eyes."""

    nRolls=[]
    for i in range(1,nIts):
        nRolls.append(snakeEyesRoller())

    return (sum(nRolls)/nIts)
