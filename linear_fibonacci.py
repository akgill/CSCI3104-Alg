def linear_fibonacci(n):
    """This function computes the nth Fibonacci number in linear time."""
    if (n==0 or n==1): return n

    fib=[0,1]
    for i in range(2,n+1):
        fib.append(fib[i-2] + fib[i-1])

    return fib[-1]
