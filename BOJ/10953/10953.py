T = int(input())
AB = [[int(x) for x in input().split(",")] for y in range(T)]
for i in range(T):
    print(AB[i][0]+AB[i][1])