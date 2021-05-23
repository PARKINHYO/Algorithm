import sys

# 문제 이해가 어렵군..

N, C = map(int, sys.stdin.readline().split())
loc = [int(sys.stdin.readline()) for _ in range(N)]
loc.sort()
start, end = 1, loc[-1] - loc[0]


def func(d):
    count = 1
    cur = loc[0]
    for i in range(1, N):
        if cur + d <= loc[i]:
            count += 1
            cur = loc[i]
    return count


while start <= end:
    mid = (start+end) // 2
    if func(mid) >= C:
        answer = mid
        start = mid+1
    else:
        end = mid - 1
print(answer)
