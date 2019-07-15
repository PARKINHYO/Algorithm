def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


def count_zero(a):
    d = 10
    count = 0
    while (1):
        if a % d == 0:
            count += 1
            d *= 10
        else:
            break
    return count


N = int(input())
print(count_zero(fact(N)))