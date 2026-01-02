from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        grid = [[0] * n for _ in range(m)]

        def back(i, j):
            if grid[i][j]:
                return grid[i][j]

            size = 0
            for dir1, dir2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = i + dir1, j + dir2
                if x >= 0 and x < m and y >= 0 and y < n and matrix[i][j] < matrix[x][y]:
                    size = max(size, back(x, y))

            size += 1
            grid[i][j] = size
            return size

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, back(i, j))

        return res
    
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)