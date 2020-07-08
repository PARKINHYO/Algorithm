
from sys import stdin

data = list(map(int, stdin.readline().split()))

for i in range(len(data)):
    for j in range(i,0, -1):
        if data[j-1] > data[j]:
            temp = data[j-1]
            data[j-1] = data[j]
            data[j] = temp
        else:
            break
    for j in data:
        print(j, end=" ")
    print()

