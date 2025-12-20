from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[-1][-1]
    
# Time Complexity: O(n * t)
# Space Complexity: O(n * t)


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]

        return dp[-1]
    
# Time Complexity: O(n * t)
# Space Complexity: O(t)