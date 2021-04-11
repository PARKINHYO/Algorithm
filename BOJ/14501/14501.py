class Solution:
    def retire(self):
        n = int(input())
        T, P = [0 for i in range(n + 1)], [0 for i in range(n + 1)]
        for i in range(n):
            a, b = map(int, input().split())
            T[i] = a
            P[i] = b

        dp = [0 for i in range(n + 1)]

        for i in range(len(T) - 2, -1, -1):
            if T[i] + i <= n:
                dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
            else:
                dp[i] = dp[i + 1]

        print(dp[0])


Solution().retire()
