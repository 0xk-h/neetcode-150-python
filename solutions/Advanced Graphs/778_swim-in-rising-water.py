from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = [[False] * n for _ in range(n)]

        heap = [(grid[0][0], 0, 0)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while heap:
            h, x, y = heapq.heappop(heap)
            if (x, y) == (n -1, n -1):
                return h

            if seen[x][y]:
                continue
            seen[x][y] = True

            for dir1, dir2 in directions:
                i, j = x + dir1, y + dir2
                if i >= 0 and i < n and j >= 0 and j < n and not seen[i][j]:
                    heapq.heappush(heap, (max(h, grid[i][j]), i, j))

        return -1
    
# Time Complexity: O(n^2 log n)
# Space Complexity: O(n^2)


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cells = []
        for i in range(n):
            for j in range(n):
                cells.append((grid[i][j], i, j))

        cells.sort()
        par = [i for i in range(n * n)]
        rank = [0] * (n * n)

        def find(n1):
            if n1 != par[n1]:
                par[n1] = find(par[n1])

            return par[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 != p2:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]

                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        canReach = [[False] * n for _ in range(n)]
        res = n*n - 1
        for t, x, y in cells:
            canReach[x][y] = True

            for dir1, dir2 in directions:
                i, j = x + dir1, y + dir2

                if i >= 0 and i < n and j >= 0 and j < n and canReach[i][j]:
                    union(x*n + y, i*n + j)

            if find(0) == find(res):
                return t

        return -1
    
# Time Complexity: O(n^2 log n)
# Space Complexity: O(n^2)