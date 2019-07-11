a, b = map(int, input().split())
if a<b:
    for i in range(a, 0, -1):
        an = a%i
        bn = b%i
        am = a//i
        bm = b//i
        if an == bn == 0:
            print(i)
            print(i*am*bm)
            break
else:
    for i in range(b, 0, -1):
        an = a%i
        bn = b%i
        am = a//i
        bm = b//i
        if an == bn == 0:
            print(i)
            print(i*am*bm)
            break