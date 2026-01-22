from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(32):
            bit = 1 << i
            x, y = 0, 0

            for num in range(n + 1):
                if num & bit:
                    x += 1

            for num in nums:
                if num & bit:
                    y += 1

            if x != y:
                res |= bit
            
        return res
    
# Time Complexity: O(32 * n)
# Space Complexity: O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        for num in range(len(nums) + 1):
            res ^= num

        for num in nums:
            res ^= num

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)

        for num in range(len(nums) + 1):
            if num not in nums:
                return num
            
# Time Complexity: O(n)
# Space Complexity: O(n)