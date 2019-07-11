N = int(input())
for i in range(1, N):
    print("*"*i)
print("*"*N)
for i in range(N-1, 0, -1):
    print("*"*i)