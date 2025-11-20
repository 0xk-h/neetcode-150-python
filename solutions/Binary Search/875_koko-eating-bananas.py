from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l < r:
            k = l + (r-l) // 2
            res = 0
            for i in piles:
                res += math.ceil(i / k)

            if res > h:
                l = k + 1
            else:
                r = k

        return l
    
# Time Complexity: O(n log m)
# Space Complexity: O(1)