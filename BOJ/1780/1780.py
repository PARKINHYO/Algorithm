import sys
sys.setrecursionlimit(10**6)


class Solution:
    def check(self, x: int, y: int, n: int):
        global matrix
        temp = matrix[x][y]
        for i in range(n):
            for j in range(n):
                if temp != matrix[x + i][y + j]:
                    return False
        return True

    def divide(self, x: int, y: int, n: int):
        global matrix
        global result
        if self.check(x, y, n):
            result[matrix[x][y] + 1] += 1
        else:
            for i in range(3):
                for j in range(3):
                    self.divide(x+i*n//3, y+j*n//3, n//3)
        return


N = int(sys.stdin.readline())
matrix = []
result = [0] * 3

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

Solution().divide(0, 0, N)

for i in range(3):
    print(result[i])
