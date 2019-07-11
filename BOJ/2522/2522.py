N = int(input())
for i in range(1, N):
    print(" "*(N-i) + "*"*i)
print("*"*N)
for i in range(N-1, 0, -1):
    print(" " * (N - i) + "*" * i)