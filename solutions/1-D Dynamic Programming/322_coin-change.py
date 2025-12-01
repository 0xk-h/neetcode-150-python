from typing import List
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1
    
# Time Complexity: O(n * t)      t -> amount
# Space Complexity: O(t)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def back(s):
            if s == 0:
                return 0

            if s in memo:
                return memo[s]

            min_num = float("inf")
            for coin in coins:
                if s - coin >= 0:
                    min_num = min(min_num, 1 + back(s - coin))
                
            memo[s] = min_num
            return min_num

        res = back(amount)
        return res if res != float("inf") else -1
    
# Time Complexity: O(n * t)      t -> amount
# Space Complexity: O(t)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        q = deque([amount])
        seen = [False] * amount
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                curr = q.popleft()

                for coin in coins:
                    x = curr - coin
                    if x == 0:
                        return res

                    if x > 0 and not seen[x]:
                        seen[x] = True
                        q.append(x)

        return -1
    
# Time Complexity: O(n * t)      t -> amount
# Space Complexity: O(t)