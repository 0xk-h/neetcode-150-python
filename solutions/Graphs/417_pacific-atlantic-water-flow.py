from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(grid, i, j, prev):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] or heights[i][j] < prev:
                return

            grid[i][j] = True
            for x, y in directions:
                dfs(grid, i + x, j + y, heights[i][j])
            

        atlantic = [[False]* n for _ in range(m)]
        for i in range(m):
            dfs(atlantic, i, n - 1, 0)
        for j in range(1, n):
            dfs(atlantic, m - 1, j, 0)

        pacific = [[False]* n for _ in range(m)]
        for i in range(m):
            dfs(pacific, i, 0, 0)
        for j in range(1, n):
            dfs(pacific, 0, j, 0)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res
    
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)