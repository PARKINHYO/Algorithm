def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end)//2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0

N = int(input())
A = [int(x) for x in input().split()]
A.sort()
M = int(input())
A2 = [int(x) for x in input().split()]
result = []
for i in A2:
    result.append(binary_search(A, i))
for i in result:
    print(i)