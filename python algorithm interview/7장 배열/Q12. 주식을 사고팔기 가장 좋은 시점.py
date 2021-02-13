"""
fixme. https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
fixme. Q12. 주식을 사고팔기 가장 좋은 시점
fixme. 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
fixme. Input: [7,1,5,3,6,4]
fixme. Output: 7
fixme. Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
 Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

fixme. Input: [1,2,3,4,5]
 Output: 4
 Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

fixme. Input: [7,6,4,3,1]
 Output: 0
 Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List
import sys


class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
