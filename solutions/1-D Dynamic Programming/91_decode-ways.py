class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}

        def back(i):
            if i in memo:
                return memo[i]

            if s[i] == "0":
                return 0

            res = back(i + 1)

            if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i+1] in {"0","1","2","3","4","5","6"})):
                res += back(i + 2)

            memo[i] = res
            return res

        return back(0)
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] if s[i - 1] != "0" else 0
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] in "0123456"):
                dp[i] += dp[i - 2]

        return dp[-1]
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        a, b = 1, 1

        for i in range(2, n + 1):
            temp = b
            b = b if s[i - 1] != "0" else 0
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] in "0123456"):
                b += a
            
            a = temp

        return b
    
# Time Complexity: O(n)
# Space Complexity: O(1)