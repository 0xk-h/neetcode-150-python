from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = [float("inf")] * n
        res[src] = 0

        for _ in range(k + 1):
            dist = res[:]
            for j, i, w in flights:
                dist[i] = min(dist[i], res[j] + w)
            res = dist

        return -1 if res[dst] == float("inf") else res[dst]
    
# Time complexity: O(k * E)
# Space complexity: O(n)