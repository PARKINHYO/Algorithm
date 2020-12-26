import collections, heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # defaultdict를 사용해 그래프를 담을 딕셔너리를 만듬
        graph = collections.defaultdict(list)

        # 그래프 만듬. u는 시작점, v는 도착점, w는 가중치
        for u, v, w in flights:
            graph[u].append((v, w))

        # 우선순위 큐변수. 0은 가격(가중치), src는 node, K는 문제에서 주어진 최소로 경유해야하는 값
        Q = [(0, src, K)]

        while Q:
            # 우선순위 큐에서 가장 가격이 작은것부터 pop한다.
            price, node, k = heapq.heappop(Q)

            # node가 도착지라면 가격을 리턴하고 종료
            if node == dst:
                return price

            # K개의 경유지 이내에 도착해야 하므로 K가 0보다 크거나 같아야지만 실행됨.
            if k >= 0:
                # 인접노드로 접근해서 정점과 가중치(가격)을 가지고옴
                for  v, w in graph[node]:
                    # 기존의 가격에 인접한 노드로 갈시에 드는 가격을 더해서 alter 변수로 저장
                    alt = price + w
                    # 힙으로 push. 인접노드로 갈시 한번 경유를 한 셈이므로 k-1로 push.
                    heapq.heappush(Q, (alt, v, k-1))


        return -1

