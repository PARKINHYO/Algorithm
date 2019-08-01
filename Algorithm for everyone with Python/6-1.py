def search_list(a, x):
    n = len(a)
    result = []
    for i in range(0, n):
        if x == a[i]:
            result.append(i)

    return result

v = [17, 7, 18, 33, 58, 7, 33, 7]
print(search_list(v, 59))