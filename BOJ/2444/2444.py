N = int(input())
for i in range(1, N):
    print(" "*(N-i) + "*"*(i-1) + "*" + "*"*(i-1))
print("*"*(2*N-1))
for i in range(N-1, 0, -1):
    print(" " * (N - i) + "*" * (i - 1) + "*" + "*" * (i - 1))