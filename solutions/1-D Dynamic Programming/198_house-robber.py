from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])

        return nums[-1]
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0

        for i in range(len(nums)):
            a, b = b, max(a + nums[i], b)

        return b
    
# Time Complexity: O(n)
# Space Complexity: O(1)