from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1

                elif grid[i][j] == 2:
                    q.append((i, j))

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        while q and fresh > 0:
            res += 1

            for _ in range(len(q)):
                i, j = q.popleft()

                for a, b in moves:
                    x, y = i + a, j + b

                    if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1:
                        fresh -= 1
                        grid[x][y] = 2
                        q.append((x, y))


        return res if fresh == 0 else -1
    
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)