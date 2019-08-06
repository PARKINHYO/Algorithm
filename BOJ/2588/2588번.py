def myfunc(a, b, b2):
    if b2 == 0:
        print(a*b)
        return
    print(a * (b2 % 10))
    myfunc(a, b, b2//10)


if __name__ == '__main__':
    n1 = int(input())
    n2 = int(input())
    myfunc(n1, n2, n2)

