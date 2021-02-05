"""
fixme. https://leetcode.com/problems/gas-station/
fixme. Q81. 주유소
fixme. 원형으로 경로가 연결된 주유소 목록이 있다. 각 주유소는 gas[i] 만큼의 기름을 갖고 있으며,
fixme. 다음 주유소로 이동하는데 cost[i]가 필요하다. 기름이 부족하면 이동할 수 없다고 할 때
fixme. 모든 주유소를 방문할 수 있는 출발점의 인덱스를 출력하라.
fixme. 출발점이 존재하지 않을 경우 -1을 리턴하며, 출발점은 유일하다.
fixme. 입력 : gas = [1,2,3,4,5], cost = [3,4,5,1,2]
fixme. 출력 : 3
fixme. 설명
fixme. 3번 인덱스(기름을 4만큼 충전할 수 있는)에서 출발할 경우는 다음과 같다.
fixme. 3번 → 4번 -1 fuel 3
fixme. 4번 → 0번 -1 fuel 6
fixme. 0번 → 1번 -1 fuel 4
fixme. 1번 → 2번 -1 fuel 2
fixme. 2번 → 3번 -1 fuel 0
fixme. 정확하게 기름이 0까지 소모되며, 모든 주유소를 방문할 수 있다.
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)

                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]
            if can_travel:
                continue
            return start
        return -1

    # 앞쪽이 -면 어차피 종료이기 때문에 적어도 +0 아니면 오히려 남은 기름을 줘서 앞쪽 부터 O(n)으로
    def canCompleteCircuitOn(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안 되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start
