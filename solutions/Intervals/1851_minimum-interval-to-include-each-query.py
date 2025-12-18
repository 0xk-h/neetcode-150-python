from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        intervals.sort()

        res = {}
        i = 0
        heap = []
        for q in sorted(queries):
            while i < n and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            res[q] = heap[0][0] if heap else -1

        return [res[q] for q in queries]
    
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(n)