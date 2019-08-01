import sys
sys.setrecursionlimit(10000)

def Fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n > 32:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(1000))
