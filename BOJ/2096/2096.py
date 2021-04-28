from sys import stdin

locations = [list(map(int, stdin.readline().split()))
             for _ in range(int(stdin.readline()))]
mybasket = [locations[0], locations[0]]

for i in range(1, len(locations)):
    mybasket[0] = [min(locations[i][0] + mybasket[0][0], locations[i][1] + mybasket[0][0]),
                   min(locations[i][0] + mybasket[0][1], locations[i]
                       [1] + mybasket[0][1], locations[i][2] + mybasket[0][1]),
                   min(locations[i][1] + mybasket[0][2], locations[i][2] + mybasket[0][2])]
    mybasket[1] = [max(locations[i][0] + mybasket[1][0], locations[i][1] + mybasket[1][0]),
                   max(locations[i][0] + mybasket[1][1], locations[i]
                       [1] + mybasket[1][1], locations[i][2] + mybasket[1][1]),
                   max(locations[i][1] + mybasket[1][2], locations[i][2] + mybasket[1][2])]
print(max(mybasket[1]), min(mybasket[0]))
