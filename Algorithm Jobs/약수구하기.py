from sys import stdin

n = int(stdin.readline())
for i in range(1, n+1):
    if n % i ==0:
        print(i, end=" ")

