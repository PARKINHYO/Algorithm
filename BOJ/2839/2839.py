n = int(input())
F = n//5
n%=5
T = 0
while F>=0:
    if n%3 == 0:
        T = n//3
        n = n%3
        break
    F-=1
    n+=5
print((n==0) and (F+T) or -1)