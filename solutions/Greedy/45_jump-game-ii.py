from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 1
        res = 0

        while r < n:
            res += 1

            max_reach = 0
            for curr in range(l, r):
                max_reach = max(max_reach, curr + nums[curr])

            l, r = r, max_reach + 1

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)