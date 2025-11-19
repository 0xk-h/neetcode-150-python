from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            curr_l = height[l]
            curr_r = height[r]

            if curr_l < curr_r:
                res = max(res, (r - l) * curr_l)
                while l < r and height[l] <= curr_l:
                    l += 1

            else:
                res = max(res, (r - l) * height[r])
                while l < r and height[r] <= curr_r:
                    r -= 1

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)

#----------------------------------------------------------
#           Simplified Two Pointer Approach
#----------------------------------------------------------
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                res = max(res, (r - l) * height[l])
                l += 1

            else:
                res = max(res, (r - l) * height[r])
                r -= 1

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)


#----------------------------------------------------------
#           Brute Force Approach [TLE]
#----------------------------------------------------------
class Solution:            
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                curr = (j - i) * min(height[i], height[j])
                res = max(res, curr)

        return res