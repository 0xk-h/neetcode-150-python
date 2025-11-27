from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, x - y)

        return -stones[0] if stones else 0
    
# Time Complexity: O(n logn)
# Space Complexity: O(n)