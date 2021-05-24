import sys


def cur(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1
    return cur(n-1) + cur(n-2)

print(cur(int(sys.stdin.readline())))