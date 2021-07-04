import sys, collections, heapq
from typing import List
input = sys.stdin.readline

class Solution:
    def workbook(self, N: int, M: int, 
                 check: List[List[int]], degree: List[int]) -> List[int]:
        heap = []
        
        """차수가 0이면 즉, main에서 입력 받는 a들을 
        다 최소 heap에 넣는다."""
        for i in range(1, N+1):
            if degree[i] == 0:
                heapq.heappush(heap, i)


        answer = []
        while heap:
            
            """현재 힙에 있는 문제들중 
            가장 작은 값을 빼서 정답에 append한다음"""
            data = heapq.heappop(heap)
            answer.append(data)
            
            """check[data]를 확인한다. 
            차수를 1씩 뺴고 차수가 0이 되어야 최소 힙에 들어갈 수 있음
            왜냐하면, check에 3->1, 5->1이 있을 때 1의 차수가 2인데 
            3, 5번 문제를 먼저 풀어야 하기 때문에 차수를 1씩 감소시켜 
            3, 5를 먼저 answer에 집어넣고 차수가 0이 됐을 때 
            1을 힙에 넣어 주고 1이 빠지면서 answer에 들어가게 된다. 
            그래서 차수가 필요함"""
            for i in check[data]:
                degree[i] -= 1
                if degree[i] == 0:
                    heapq.heappush(heap, i)
        return answer


N, M = map(int, input().split())

# 위상 정렬에 사용될 차수
degree = collections.defaultdict(int)

# 어떤 문제를 더 빨리 풀어야되는지를 담을 리스트
check = collections.defaultdict(list)


for _ in range(M):
    a, b = map(int, input().split())
    check[a].append(b)
    
    """4번보다 2번이 더 빨리 들어와야 되면 2번 차수를 1증가 시킨다.
    또 다른 번호보다 2번이 빨리 들어와야 되면 2번 차수를 또 1증가 시킨다.
    나중에 힙에 넣고 빼고 할 때 이 차수를 사용한다. """
    degree[b] += 1
    
print(*Solution().workbook(N, M, check, degree))

