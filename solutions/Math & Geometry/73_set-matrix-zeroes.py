from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows = []
        cols = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        for i in range(m):
            for j in cols:
                matrix[i][j] = 0

# Time Complexity: O(m * n)
# Space Complexity: O(m + n)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroRow = any(matrix[i][0] == 0 for i in range(m))
        zeroCol = any(matrix[0][j] == 0 for j in range(n))

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zeroRow:
            for i in range(m):
                matrix[i][0] = 0

        if zeroCol:
            for j in range(n):
                matrix[0][j] = 0

# Time Complexity: O(m * n)
# Space Complexity: O(1)