N = int(input())
for i in range(1, N):
    print("*"*i + " "*(N-i) + " "*(N-i) + "*"*i)
print("*"*(2*N))
for i in range(1, N):
    print("*"*(N-i) + " "*(2*i) + "*"*(N-i))