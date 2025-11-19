from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        ll, rl = height[l], height[r]
        res = 0

        while l < r:
            if ll < rl:
                res += ll - height[l]
                l += 1
                ll = max(ll, height[l])

            else:
                res += rl - height[r]
                r -= 1
                rl = max(rl, height[r])

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left = [0] * (n+1)
        for i in range(n):
            left[i + 1] = max(height[i], left[i])

        right = [0] * (n+1)
        for i in range(n -2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])

        res = 0
        for i in range(n):
            res += max(0, min(left[i], right[i]) - height[i])

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)