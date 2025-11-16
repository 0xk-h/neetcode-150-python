from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i +1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            if num in h:
                return [h[num], i]

            h[target - num] = i

# Time Complexity: O(n)
# Space Complexity: O(n)
                    