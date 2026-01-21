from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        d = 1
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for x, y in dir:
                    x1, y1 = i + x, j + y
                    if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and grid[x1][y1] == INF:
                        grid[x1][y1] = d
                        q.append((x1, y1))

            d += 1

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)