from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]

        res = 0
        for currStart, currEnd in intervals[1:]:
            if prevEnd > currStart:
                res += 1
                prevEnd = min(prevEnd, currEnd)

            else:
                prevEnd = currEnd

        return res
    
# Time Complexity: O(n log n)
# Space Complexity: O(1)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prevEnd = intervals[0][1]

        res = 0
        for currStart, currEnd in intervals[1:]:
            if prevEnd > currStart:
                res += 1

            else:
                prevEnd = currEnd

        return res
    
# Time Complexity: O(n log n)
# Space Complexity: O(1)