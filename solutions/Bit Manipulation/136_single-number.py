from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [num for num in nums if nums.count(num) == 1][0]
        
# Time Complexity: O(n^2)
# Space Complexity: O(1)