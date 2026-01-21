from typing import List
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False

        return True