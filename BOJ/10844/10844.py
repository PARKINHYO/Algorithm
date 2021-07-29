import sys
input = sys.stdin.readline 


class Solution:
    def easy_stair_numbers(self, N: int):
        # dp 초기화. 행이 자리수, 열이 0부터 9까지 가능한 개수
        dp = [[0,0,0,0,0,0,0,0,0,0] for _ in range(101)]
        
        # dp 처음 1 [0,1,1,1,1,1,1,1,1,1]로 초기화
        for i in range(1, 10):
            dp[1][i] = 1
            
        """2번째 부터 0일 수 있는 경우의 수는 
        전 자리수에서 1인 경우이고, 
        9인 경우의 수는 전 자리수에서 8인 경우의수임"""
        for i in range(2, N+1):
            dp[i][0] = dp[i-1][1]
            dp[i][9] = dp[i-1][8]
            
            """1부터 8은 전 자리수에서 
            n-1, n+1인 경우의 합과 같음"""
            for j in range(1, 9):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]            
        return sum(dp[N])%1000000000


print(Solution().easy_stair_numbers(int(input())))
