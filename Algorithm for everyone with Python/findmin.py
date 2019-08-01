def find_min(a):
    n = len(a)
    min_v = a[0]
    for i in range(1, n):
        if a[i] < min_v:
            min_v = a[i]
    return min_v

v= [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))

