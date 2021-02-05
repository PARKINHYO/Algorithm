"""
fixme. https://leetcode.com/problems/queue-reconstruction-by-height/
fixme. Q79. 키에 따른 대기열 재구성
fixme. 여러 명의 사람들이 줄을 서 있다. 각각의 사람은 (h, k)의 두 정수 쌍을 갖는데, h는 그 사람의 키,
fixme. k는 앞에 줄 서 잇는 사람들 중 자신의 키 이상인 사람들의 수르 뜻한다. 이 값이 올바르도록 줄을
fixme. 재정렬하는 알고리즘을 작성하라.
fixme. 입력 : [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
fixme. 출력 : [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
fixme. 설명
fixme. 키가 5인 사람이 가장 먼저 섰고, 앞에는 아무도 없다. 7인 사람이 뒤따르고, 그보다 키가 더 큰 사람은 아무도 없다.
fixme. 5인 사람이 섰으며, 앞에 5, 7 두 명이 자신보다 크거나 같다. 6인 사람의 앞에느 자신보다 큰 키 7인 사람 한명이 있다.
fixme. 4인 사람 앞에는 5, 7, 5, 6 네 명이 있다. 마지막으로 7인 사람 앞에 자신보다 크거나 같은 이는 키가 7인 사람 한 명이다.
"""

from typing import List
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result

