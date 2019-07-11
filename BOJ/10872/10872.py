N = int(input())
if N==0:
    print(1)
else:
    N2 = N
    for i in range(N, 1, -1):
        N2 *= (i-1)
    print(N2)