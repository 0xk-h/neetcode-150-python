from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}

        for ind, val in enumerate(numbers):
            if val in h:
                return [h[val], ind +1]
            else:
                h[target - val] = ind + 1

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums) -1
        
        while l < r:
            x = nums[l] + nums[r]
            if x == target:
                return [l +1, r +1]

            if x > target:
                r -= 1
            else:
                l += 1

# Time Complexity: O(n)
# Space Complexity: O(1)