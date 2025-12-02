from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        h = {}

        for curr in nums:
            max_value = 1

            for prev in h:
                if prev < curr:
                    max_value = max(max_value, h[prev] + 1)

            h[curr] = max_value

        return max(h.values())
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)