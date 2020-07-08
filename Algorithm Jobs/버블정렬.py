from sys import stdin

arr = list(map(int, stdin.readline().split()))

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

    for i in arr:
        print(i, end=" ")
    print()


