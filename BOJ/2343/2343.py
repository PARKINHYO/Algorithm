import sys, math
from typing import List
input = sys.stdin.readline


class Solution:
    def guitar_lesson(self, N: int, M: int, lesson: List[int]):
        
        # 블루레이의 크기로 이분 탐색
        # 레슨을 블루레이에 한개씩만 담는다고 했을 때 최소 값을 알  수 있음
        # 레슨의 길이중 가장 큰 값이 블루레이의 최소 값이 된다. 
        # 레슨을 싹다 담았을 때가 최대 값
        start, end = max(lesson), sum(lesson)
        answer = sys.maxsize
        while start <= end:
            mid = (start + end) // 2 # mid가 정답의 후보가 됨
            
            count = 0# 블루레이 갯수
            
            total = 0 # 블루레이 크기
            
            for i in range(len(lesson)):
                if total + lesson[i] > mid:
                    count += 1
                    total = 0
                total += lesson[i]
                
            if total:
                # for문이 끝난 뒤에 마지막 블루레이 count
                count += 1
                
            if count > M: 
                # 블루레이의 갯수가 최소 갯수 M보다 크다는 것은 
                # 블루레이의 크기가 작다는 말. 
                # start를 mid +1위치로 해준다. 
                start = mid + 1
            else:
                # 블루레이의 갯수가 최소 갯수 M이랑 같거나 더 작은 게 오고, 
                # 블루레이 크기(mid)가 더 커지는 것이므로  이중엫서 가장 작은 값이 정답
                answer = min(answer, mid)
                end = mid-1
        return answer


N, M = map(int, input().split())
lesson = list(map(int, input().split()))
print(Solution().guitar_lesson(N, M, lesson))
