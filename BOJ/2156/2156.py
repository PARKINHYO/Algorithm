from typing import List
import collections
import sys
input = sys.stdin.readline


class solution:
    def wine(self, n: int, wines: List):
        dp = collections.defaultdict(int)

        if n == 1:
            return wines[0]
        if n == 2:
            return sum(wines)
        if n == 3:
            return max(wines[0]+wines[1],
                       wines[0]+wines[2], wines[1]+wines[2])
        if n == 4:
            return max(wines[0]+wines[1]+wines[3],
                       wines[0]+wines[2]+wines[3], wines[1]+wines[2])
        dp[0], dp[1], dp[2], dp[3] = wines[0], wines[0]+wines[1], \
            max(wines[0]+wines[1], wines[0]+wines[2], wines[1]+wines[2]), \
            max(wines[0]+wines[1]+wines[3],
                wines[0]+wines[2]+wines[3], wines[1]+wines[2])
        for i in range(4, n):
            dp[i] = max(dp[i-4]+wines[i-1]+wines[i-2], dp[i-3] + \
                        wines[i]+wines[i-1], dp[i-2]+wines[i])
        return dp[n-1]


if __name__ == '__main__':
    n = int(input())
    wines = []
    for _ in range(n):
        wines.append(int(input()))
    print(solution().wine(n, wines))
