"""
fixme. https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
fixme. 여러 번의 거래로 낼 수 있는 최대 이익을 산출하라.
fixme. 입력 : [7, 1, 5, 3, 6, 4]
fixme. 출력 : 7
fixme. 설명 : 1일 때 사서 5일 때 팔아 4의 이익을 얻고, 3일 때 사서 6일 때 팔아 3의 이익을 얻는다.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 값이 오르는 경우 매번 그리디 계산
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        return result

    def maxProfitPython(self, prices: List[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))
