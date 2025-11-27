from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            d = - (x*x + y*y)
            heapq.heappush(maxHeap, (d, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [[x, y] for _, x, y in maxHeap]
    
# Time Complexity: O(n logk)
# Space Complexity: O(k)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            d = x*x + y*y
            heapq.heappush(heap, (d, x, y))

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res
    
# Time Complexity: O(n logn)
# Space Complexity: O(n)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key = lambda x: x[0]*x[0] + x[1]*x[1])[:k]
    
# Time Complexity: O(n logn)
# Space Complexity: O(n)