from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        res = n - 1

        for i in range(n-2, -1, -1):
            if i + nums[i] >= res:
                res = i

        return res == 0
    
# Time Complexity: O(n)
# Space Complexity: O(1)