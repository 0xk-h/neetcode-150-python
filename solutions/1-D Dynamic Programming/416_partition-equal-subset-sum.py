from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2

        memo = {}
        def back(i, s):
            if s == target:
                return True

            if s in memo and memo[s] <= i:
                return False

            for j in range(i, len(nums)):
                if s + nums[j] <= target and back(j + 1, s + nums[j]):
                    return True

            memo[s] = i
            return False

        return back(0, 0)

# Time Complexity: O(n * target)
# Space Complexity: O(target)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[-1]
    
# Time Complexity: O(n * target)
# Space Complexity: O(target)