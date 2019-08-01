from sys import stdin

N = int(input())
list = [0]*10001

for i in range(N):
    n = int(stdin.readline())
    list[n] += 1

for i in range(len(list)):
    if(list[i] >= 1):
        if(list[i] == 1):
            print(i)
        else:
            tmp = list[i]
            for j in  range(tmp):
                print(i)
