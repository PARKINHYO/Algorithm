import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))


left, right = 0, max(trees)
complete = False
while left <= right:
    mid = (left + right) // 2
    sum = 0
    for tree in trees:
        if tree > mid:
            sum += (tree - mid)

    if sum > M:
        left = mid + 1
    elif sum < M:
        right = mid - 1
    else:
        print(mid)
        complete = True
        break
if not complete:
    print(right)