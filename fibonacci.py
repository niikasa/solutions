import time

# Calculate Fibonacci by recursive method
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


# Calculate Fibonacci using memoization
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1,memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n+1)
    return fib_2(n,memo)



# Calculate Fibonacci using bottom_up approach.
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]



def main():
    n = 35
    start = time.time()
    print("F({}) = {}".format(n,fib(n)))
    end = time.time()
    print(end - start, "seconds, recursive method\n")

    start = time.time()
    print("F({}) = {}".format(n,fib_memo(n)))
    end = time.time()
    print(end - start, "seconds, memoization method\n")

    start = time.time()
    print("F({}) = {}".format(n,fib_bottom_up(n)))
    end = time.time()
    print(end - start, "seconds, bottom-up method")    

if __name__ == "__main__":
    main()




