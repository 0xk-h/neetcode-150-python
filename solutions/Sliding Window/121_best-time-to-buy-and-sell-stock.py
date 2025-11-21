from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float("inf")
        res = 0

        for i in prices:
            if i < minn:
                minn = i
            else:
                res = max(res, i - minn)

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)