"""
fixme. https://leetcode.com/problems/search-a-2d-matrix-ii/
fixme. Q69. 2D 행렬 검색Ⅱ
fixme. m x n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라. 행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어 있다.
fixme. [
fixme.     [1, 4, 7, 11, 15],
fixme.     [2, 5, 8, 12, 19],
fixme.     [3, 6, 9, 16, 22],
fixme.     [10, 13, 14, 17, 24],
fixme.     [18, 21, 23, 26, 30]
fixme. ]
fixme. target=5일 경우, 값이 존재하므로 true를 리턴한다. target=20일 경우, 값이 존재하지 않으므로 false를 리턴한다.
"""

class Solution:
    def searchMatrix_firstend(self, matrix, target):
        # 예외 처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타켓이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타켓이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1
        return False

    def searchMatrix_python(self, matrix, target):
        return any(target in row for row in matrix)

