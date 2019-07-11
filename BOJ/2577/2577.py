a=int(input())
b=int(input())
c=int(input())
abc = a*b*c
abc2 = [int (i) for i in str(abc)]
for i in range(10):
    print(abc2.count(i))