N =int(input())
N2=N
i=0
while True:
    T = N2//10
    O = N2%10
    TO = (T + O)%10
    N2 = O*10 + TO
    i+=1
    if N2 == N:
        break
print(i)