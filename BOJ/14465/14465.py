import sys
input = sys.stdin.readline
N, K, B = map(int, input().split())
traffic_light = [0 for _ in range(N)]
for _ in range(B):
    traffic_light[int(input())-1] = 1
left, right = 0,0
answer = []
check = True
while left <= N-K and right <= N-1:
    if right - left < K-1:
        right += 1
        continue
    if check:
        answer.append(sum(traffic_light[left:right+1]))
    else:
        cur = answer[-1]
        if not traffic_light[left-1]:
            cur -= 1
        if not traffic_light[right]:
            cur += 1
        answer.append(cur)
    left += 1
    right += 1
print(min(answer))