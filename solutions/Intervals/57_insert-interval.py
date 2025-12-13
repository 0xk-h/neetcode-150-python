from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        res = []
        added = False
        for i in range(len(intervals)):
            if not added:
                if newInterval[1] < intervals[i][0]:
                    res.append(newInterval)
                    res.append(intervals[i])
                    added = True

                elif newInterval[0] <= intervals[i][1]:
                    res.append([min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])])
                    added = True

                else:
                    res.append(intervals[i])

            elif res[-1][1] >= intervals[i][0]:
                a, b = res.pop()
                res.append([a, max(b, intervals[i][1])])

            else:
                res.append(intervals[i])

        if not added:
            res.append(newInterval)

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)
