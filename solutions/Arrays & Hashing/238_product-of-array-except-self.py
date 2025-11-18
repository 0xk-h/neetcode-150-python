from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        acc = 1

        for i in range(len(nums)):
            res[i] *= acc
            acc *= nums[i]

        acc = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= acc
            acc *= nums[i]

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1) (output array does not count as extra space)
