from sys import stdin


class Solution:
    def printStar(self, N: int):
        def recursive(n):
            if n == 3:
                Map[0][:3] = Map[2][:3] = ['*']*3
                Map[1][:3] = ['*', ' ', '*']
                return
            a = n // 3
            recursive(n//3)
            for i in range(3):
                for j in range(3):
                    if i == 1 and j == 1:
                        continue
                    for k in range(a):
                        Map[a*i + k][a*j:a*(j+1)] = Map[k][:a]

        Map = [[' ' for i in range(N)] for i in range(N)]
        recursive(N)
        
        for m in Map:
            print(*m, sep="")
        return


Solution().printStar(int(stdin.readline()))
