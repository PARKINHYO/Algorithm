from sys import stdin
from typing import List
from collections import defaultdict


class Solution:
    def spinningSushi(self, N: int, belt: List[int], k: int, coupon: int):
        
        # 스시의 종류
        mydict = defaultdict(int)
        
        """
        투포인터, cnt로 k개 이하로만 동작하게 만듬. 
        k개 안에서 종류가 각각 다름을 알아내기 위한 kind. 
        kind와 answer를 비교해서 kind가 크면 answer에 넣어줌.
        """
        left, right, cnt, kind, answer = 0, 0, 0, 0, 0

        while left != N-1:
            if cnt >= k:
                mydict[belt[left]] -= 1
                if mydict[belt[left]] == 0:
                    kind -= 1

                left = (left+1) % N
                cnt -= 1
            else:
                if mydict[belt[right]] == 0:
                    kind += 1
                mydict[belt[right]] += 1
                right = (right + 1) % N
                cnt += 1
            if kind >= answer:
                answer = kind
                if mydict[coupon] == 0:
                    answer += 1

        return answer


N, d, k, coupon = map(int, stdin.readline().split())
belt = []
for _ in range(N):
    belt.append(int(stdin.readline()))
print(Solution().spinningSushi(N, belt, k, coupon))
