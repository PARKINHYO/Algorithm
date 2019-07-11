N, K = map(int, input().split())
N2 = N
K2 = K
for i in range(1, K):
    N2 = N2*(N-i)
    K2 = K2*(K-i)
if K2==0:
    print(1)
else:
    print(int(N2/K2))