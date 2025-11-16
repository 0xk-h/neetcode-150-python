from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True

            seen.add(i)
        return False
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    
# Time Complexity: O(n)
# Space Complexity: O(n)