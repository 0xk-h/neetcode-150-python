from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        memo = [[None, None] for _ in range(n)]
        def back(i, isCooldown, isBuyed):
            if i >= n:
                return 0

            if isCooldown:
                return back(i + 1, False, isBuyed)

            if memo[i][isBuyed]:
                return memo[i][isBuyed]
                
            res = 0
            if isBuyed:
                # Sell
                res = back(i + 1, True, 0) + prices[i]
            else:
                # Buy
                res = back(i + 1, False, 1) - prices[i]

            res = max(res, back(i + 1, False, isBuyed))
            memo[i][isBuyed] = max(0, res)
            return memo[i][isBuyed]

        return back(0, False, 0)
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            # have no stock (buy, hold)
            dp[i][0] = max(dp[i + 1][1] - prices[i], dp[i + 1][0])

            # have a stock (sell, hold)
            dp[i][1] = max(dp[i + 2][0] + prices[i], dp[i + 1][1])

        return dp[0][0]
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        noStock = 0
        haveStock = 0
        afterCooldown = 0
        temp = 0

        for i in range(len(prices) - 1, -1, -1):
            afterCooldown = temp
            temp = noStock
            noStock = max(haveStock - prices[i], noStock)
            haveStock = max(afterCooldown + prices[i], haveStock)

        return noStock
    
# Time Complexity: O(n)
# Space Complexity: O(1)