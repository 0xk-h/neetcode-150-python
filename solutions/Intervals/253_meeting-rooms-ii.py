from typing import List
from interval import Interval
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        n = len(intervals)
        intervals.sort(key = lambda x: x.start)

        res = [intervals[0].end]

        for i in intervals[1:]:
            isAdded = False
            for j in range(len(res)):
                if res[j] <= i.start:
                    isAdded = True
                    res[j] = i.end
                    break

            if not isAdded:
                res.append(i.end)
            
        return len(res)
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        n = len(intervals)
        intervals.sort(key = lambda x: x.start)

        heap = [intervals[0].end]

        for i in intervals[1:]:
            if heap[0] <= i.start:
                heapq.heappop(heap)
                
            heapq.heappush(heap, i.end)
            
        return len(heap)

# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        st = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        j = 0
        curr = 0
        res = 0

        for i in range(n):
            while j < n and end[j] <= st[i]:
                curr -= 1
                j += 1

            i += 1
            curr += 1
            res = max(res, curr)

        return res
    
# Time Complexity: O(n log n)
# Space Complexity: O(n)

