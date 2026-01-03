class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        memo = [[None] * n for _ in range(m)]
        def back(i, j):
            if i == m:
                return n - j

            if j == n:
                return m - i

            if memo[i][j] != None:
                return memo[i][j]

            if word1[i] == word2[j]:
                return back(i + 1, j + 1)
            
            memo[i][j] = min(back(i + 1, j), back(i, j + 1), back(i + 1, j + 1)) + 1
            return memo[i][j]

        return back(0, 0)

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            dp[i][n] = m - i

        for j in range(n):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1

        return dp[0][0]
    
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [n - j for j in range(n + 1)]

        for i in range(m - 1, -1, -1):
            prev = dp[n]
            dp[n] = m - i
            for j in range(n - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j + 1], prev) + 1

                prev = temp

        return dp[0]
    
# Time Complexity: O(m * n)
# Space Complexity: O(n)