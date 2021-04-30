import sys

N, K = map(int, sys.stdin.readline().split())
cage = [0] * 1000001 # 동물이 갈 수 있는 공간
left , right = sys.maxsize, 0 

for i in range(N):
    g, x = map(int, sys.stdin.readline().split())
    # 입력 받으면서 최소, 최댓값 구해서 left, right 계산
    right = max(x, right)
    left = min(x, left)
    cage[x] = g

end = left
now, ans = 0, 0


# left에서 right까지 start가 움직임. 
for start in range(left, right+1):
    # 동물이 팔을 양쪽으로 K만큼 뻗을 수 있으니깐 걍 왼쪽팔부터 2K만큼 뻗음. 
    while end < right + 1 and end - start <= K * 2:
        # cage에 값이 존재하는것만 now에 더해줌. 
        if not cage[end]:
            end += 1
            continue
        now += cage[end]
        end += 1
    
    ans = max(ans, now)
    
    # start가 계속 옆으로 가니깐 cage[start]에 값이 있으면 now에 빼줌
    now -= cage[start]
    if end >= right : break
print(ans)