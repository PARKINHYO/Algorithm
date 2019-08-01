def ex_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum

print(ex_sum(10))
