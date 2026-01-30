from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append((v, w))

        seen = [False] * (n + 1)
        notFound = n
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if not seen[node]:
                notFound -= 1
                if notFound == 0:
                    return time
                seen[node] = True

                for nei, w in adj[node]:
                    heapq.heappush(heap, (time + w, nei))

        return -1
    
# Time Complexity: O(E log V)
# Space Complexity: O(V + E)