import sys
input = sys.stdin.readline


class Solution:
    def game(self, x: int, y: int):
        
        # 처음 x, y 퍼센트
        percent = int(y*100/x)
        
        # 범위 전체로 해서 이분 탐색
        start, end = 1, 1000000000
        while start < end:
            mid = (start + end) // 2
            
            # x, y에 mid를 각각 더해서 퍼센트를 구하고,
            # 처음 x, y의 퍼센트와 비교한다. 
            cur = int((y+mid)*100/(x+mid))
            if cur <= percent:
                start = mid+1
            else:
                end = mid
        return end if int((y+end)/(x+end)*100) > percent else -1


X, Y = map(int, input().split())
print(Solution().game(X, Y))
