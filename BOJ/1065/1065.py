def HanNumber(a):
    if a>99:
        b = a//100
        c = a - b*100
        d = c//10
        e = c%10
        if d == (b+e)/2:
            return 1
        else:
            return 0

    else:
        return 1

N = int(input())
sum=0
for i in range(1,N+1):
    if HanNumber(i) == 1:
        sum+=1
print(sum)