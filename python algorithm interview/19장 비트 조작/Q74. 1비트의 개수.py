"""
fixme. https://leetcode.com/problems/number-of-1-bits/
fixme. Q74. 1비트의 개수
fixme. 부호없는 정수형을 입력받아 1브트의 개수를 출력하라.
fixme. 입력 00000000000000000000000000001011
fixme. 출력 3
fixme. 입력 00000000000000000000000010000000
fixme. 출력 1
fixme. 입력 11111111111111111111111111111101
fixme. 출력 31
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    def hammingWeightBin(self, n: int) -> int:
        count = 0
        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            n &= n - 1
            count += 1
        return count