from sys import stdin

n = int(stdin.readline())
i = 2
while True:
    if n % i == 0:
        print(i, end=" ")
        n /= i
    else: i+=1

    if n ==1:
        break
