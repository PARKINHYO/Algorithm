N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(0, N):
    if A[i]<X:
        print(A[i], end=' ')