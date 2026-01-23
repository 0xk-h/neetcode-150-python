from typing import List
from functools import cache

#---------------------------------------------------------------#
#               Time Limit Exceeded (TLE) Solution
#---------------------------------------------------------------#
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def back(arr):
            if not arr:
                return 0

            res = 0
            for i in range(1, len(arr) - 1):
                curr = arr[i - 1] * arr[i] * arr[i + 1]
                curr += back(arr[:i] + arr[i + 1:])
                res = max(res, curr)

            return res

        return back(tuple([1] + nums + [1]))
    
# Time Complexity: O(2^n * n!)
# Space Complexity: O(2^n * n!)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        memo = [[0] * (n - 1) for _ in range(n - 1)]
        def back(l, r):
            if l > r:
                return 0

            if memo[l][r]:
                return memo[l][r]

            res = 0
            for i in range(l, r + 1):
                curr = nums[l - 1] * nums[i] * nums[r + 1]
                curr += back(l, i - 1) + back(i + 1, r)
                res = max(res, curr)
            
            memo[l][r] = res
            return res

        return back(1, len(nums) - 2)
    
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)