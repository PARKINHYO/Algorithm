N = int(input())
YX = []
for i in range(N):
    x, y = map(int, input().split())
    YX.append([y, x])
YX.sort()
for i in range(N):
    print(YX[i][1], end=" ")
    print(YX[i][0])