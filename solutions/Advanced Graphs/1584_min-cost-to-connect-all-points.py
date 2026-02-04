from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        par = [i for i in range(n)]
        rank = [1] * n
        self.components = n

        def find(n1):
            if n1 != par[n1]:
                par[n1] = find(par[n1])

            return par[n1]

        def union(n1, n2, d):
            p1, p2 = find(n1), find(n2)
            if p1 != p2:
                self.res += d
                self.components -= 1
                if rank[p1] > rank[p2]:
                    rank[p1] += rank[p2]
                    par[p2] = p1

                else:
                    rank[p2] += rank[p1]
                    par[p1] = p2

            return self.components == 1

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.append((abs(x1 - x2) + abs(y1 - y2), i, j))

        self.res = 0
        edges.sort(key = lambda x:x[0])
        for d, x, y in edges:
            if union(x, y, d):
                return self.res

        return self.res
    
# Time Complexity: O(n^2 log n)
# Space Complexity: O(n^2)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()

        res = 0
        heap = [(0, 0)]

        while len(seen) != n:
            w, i = heapq.heappop(heap)
            if i in seen:
                continue

            res += w
            seen.add(i)
            for j in range(n):
                if j in seen:
                    continue

                x1, y1 = points[i]
                x2, y2 = points[j]

                heapq.heappush(heap, (abs(x1 - x2) + abs(y1 - y2), j))

        return res
    
# Time Complexity: O(n^2 log n)
# Space Complexity: O(n^2)