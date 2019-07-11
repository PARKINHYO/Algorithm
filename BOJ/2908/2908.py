a, b = map(list, input().split())
a.reverse()
b.reverse()
A = int(a[0])*100 + int(a[1])*10 +int(a[2])
B = int(b[0])*100 + int(b[1])*10 +int(b[2])
if A<B:
    print(B)
else:
    print(A)