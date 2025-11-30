from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a1, b1 = 0, 0
        for num in nums[1:]:
            a1, b1 = b1, max(a1 + num, b1)

        a2, b2 = 0, 0
        for num in nums[:-1]:
            a2, b2 = b2, max(a2 + num, b2)

        return max(b1, b2)
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            prev, curr = 0, 0
            for x in arr:
                prev, curr = curr, max(prev + x, curr)

            return curr

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
    
# Time Complexity: O(n)
# Space Complexity: O(1)