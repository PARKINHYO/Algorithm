"""
fixme. https://leetcode.com/problems/hamming-distance/
fixme. Q71. 해밍 거리
fixme. 두 정수를 입력받아 몇 비트가 다른지 계산하라.
fixme. 입력 : x = 1, y = 4
fixme. 출력 : 2
fixme. 1 (0 0 0 1)
fixme. 4 (0 1 0 0)
fixme. 1, 1 두 군데 비트가 다르므로 정답은 2다.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')