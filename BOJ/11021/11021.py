T = int(input())
AB = [[int(x) for x in input().split()] for y in range(T)]
for i in range(T):
    C = AB[i][0] + AB[i][1]
    print("Case #%d: %d" % (i+1, C))