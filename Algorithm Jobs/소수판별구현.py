from sys import stdin

n = int(stdin.readline())
flag = False
for i in range(2, n):
    if n % i == 0:
        flag = True

if flag == False:
    print("Yes")
elif flag == True:
    print("NO")
