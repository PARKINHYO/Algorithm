import sys
input = sys.stdin.readline


class Solution:
    def sum_of_numbers(self, S: int):
        count = 1
        while True:
            if S - count - (count + 1) < 0:
                return count
            S -= count
            count += 1
            


print(Solution().sum_of_numbers(int(input())))