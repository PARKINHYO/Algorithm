N = int(input())
time = [int(x) for x in input().split()]
time.sort()
timesum = 0
timesum2 = []
timesum3 = 0
for i in range(N):
    timesum += time[i]
    timesum2.append(timesum)
    timesum3 += timesum2[i]
print(timesum3)