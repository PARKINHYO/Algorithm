K, N, M = map(int, input().split(" ", 2))
PM = K*N-M
if PM<0:
    print(0)
else:
    print(PM)