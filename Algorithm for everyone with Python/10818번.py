def sum_max(l, a):
    max_v = a[0]
    for i in range(1, l):
        if a[i] >= max_v:
            max_v = a[i]
    return max_v


def sum_min(l, a):
    min_v = a[0]
    for i in range(1, l):
        if a[i] <= min_v:
            min_v = a[i]
    return min_v


N = int(input())
L = [int(x) for x in input().split()]
print("%d %d" % (sum_min(N, L), sum_max(N, L)))
