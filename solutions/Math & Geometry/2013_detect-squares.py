from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        self.pos = defaultdict(set)
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.freq[(x, y)] += 1
        self.pos[x].add((x, y))

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for x2, y2 in self.pos[x1]:
            if (x2, y2) == (x1, y1):
                continue

            d = y2 - y1
            res += self.freq[(x2, y2)] * self.freq[(x2 + d, y2)] * self.freq[(x1 + d, y1)]
            res += self.freq[(x2, y2)] * self.freq[(x2 - d, y2)] * self.freq[(x1 - d, y1)]

        return res

"""
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
"""

#---------------------------------------------------------
#           Time Complexity:
#           add:             O(1)
#           count:           O(m) -> m is the total number of points with the same x coordinate
#           
#           Space Complexity:
#           O(n) -> n is the total number of unique points
#---------------------------------------------------------