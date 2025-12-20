from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def back(i, val):
            if i == len(nums):
                return 1 if val == target else 0

            if (i, val) in memo:
                return memo[(i, val)]

            memo[(i, val)] = back(i + 1, val + nums[i]) + back(i + 1, val - nums[i])
            return memo[(i, val)]

        return back(0, 0)
    
# Time Complexity: O(n * m) where m is the range of possible sums
# Space Complexity: O(n * m)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if abs(target) > s:
            return 0

        dp = [[0] * (2 * s + 1) for _ in range(n + 1)]
        dp[0][s] = 1

        for i in range(n):
            for j in range(len(dp[0])):
                if dp[i][j]:
                    dp[i + 1][j - nums[i]] += dp[i][j]
                    dp[i + 1][j + nums[i]] += dp[i][j]

        return dp[-1][target + s]

# Time Complexity: O(n * m) where m is 2 * sum(nums)
# Space Complexity: O(n * m)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for j in dp[i]:
                dp[i + 1][j - nums[i]] += dp[i][j]
                dp[i + 1][j + nums[i]] += dp[i][j]

        return dp[-1][target]

# Time Complexity: O(n * m) where m is the range of possible sums
# Space Complexity: O(n * m)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prev = defaultdict(int)
        prev[0] = 1

        for i in range(n):
            curr = defaultdict(int)
            for j in prev:
                curr[j - nums[i]] += prev[j]
                curr[j + nums[i]] += prev[j]

            prev = curr

        return prev[target]

# Time Complexity: O(n * m) where m is the range of possible sums
# Space Complexity: O(m)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)

        """
        sum(P) - sum(N) = target
        sum(P) + sum(N) = sum(nums)
        2 * sum(P) = target + sum(nums)
        """
        
        if (s + target) % 2 != 0 or abs(target) > s:
            return 0

        P = (s + target) // 2
        dp = [0] * (P + 1)
        dp[0] = 1

        for num in nums:
            for i in range(P - num, -1, -1):
                dp[i + num] += dp[i]

        return dp[P]

# Time Complexity: O(n * P) where P = (sum(nums) + target) / 2
# Space Complexity: O(P)