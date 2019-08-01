def recursive_sum(a, b):
    if (a <= 1):
        return b[0]
    max_v = b[a - 1]
    if (max_v <= b[a - 2]):
        b.pop()
        return recursive_sum(a - 1, b)
    b[a - 2] = v.pop()
    return recursive_sum(a - 1, b)

v = [17, 92, 18, 33, 58, 7, 33, 42]
n = len(v)
print(recursive_sum(n, v))
