from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stk = []

        for ind, val in enumerate(heights):
            i = ind
            while stk and stk[-1][1] > val:
                i, x = stk.pop()
                res = max(res, x * (ind - i))

            stk.append((i, val))

        while stk:
            i, x = stk.pop()
            res = max(res, x * (len(heights) - i))

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)