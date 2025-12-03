from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        acc = 0
        for num in nums:
            acc += num
            res = max(res, acc)

            if acc < 0: acc = 0
            
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)