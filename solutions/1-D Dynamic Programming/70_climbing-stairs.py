class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1

        for _ in range(n):
            a, b = b, a + b

        return b
    
# Time Complexity: O(n)
# Space Complexity: O(1)