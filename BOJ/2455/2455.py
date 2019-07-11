train = [[int(x) for x in input().split()] for y in range(4)]
p1 = 0
p2 = 0
p3 = []
for i in range(4):
    p1 = -train[i][0] + train[i][1]
    p2 += p1
    p3.append(p2)
p3.sort()
print(p3[3])