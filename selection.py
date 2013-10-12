import random

def selection(arr, k):
    """This function takes in an array and returns the element
    corresponding to the kth element of the sorted array.
    The first element in the array is the 0th element."""
    
    # define some variables)
    nElements = len(arr)
    pivot = random.randint(0,nElements-1)
    arrLower = []
    arrUpper = []

    # partition
    for i in range(0,nElements):
        if i != pivot:
            if arr[i]<arr[pivot]:
                arrLower.append(arr[i])
            else:
                arrUpper.append(arr[i])
    
    # lengths of resulting arrays
    nLower = len(arrLower)
    nUpper = len(arrUpper)

    # decide if base case is reached, else recurse
    if k == nLower:
        return arr[pivot]
    elif k < nLower:
        return selection(arrLower,k)
    else:
        return selection(arrUpper,k-nLower-1)

