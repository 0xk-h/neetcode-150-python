class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        memo = {}
        def back(i, j):
            if i >= m or j >=n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            res = 0
            if text1[i] == text2[j]:
                res = back(i + 1, j + 1) + 1
            else:
                res = max(back(i + 1, j), back(i, j + 1))

            memo[(i, j)] = res
            return res

        return back(0, 0)
    
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        memo = [[-1] * n for _ in range(m)]
        def back(i, j):
            if i >= m or j >=n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            res = 0
            if text1[i] == text2[j]:
                res = back(i + 1, j + 1) + 1
            else:
                res = max(back(i + 1, j), back(i, j + 1))

            memo[i][j] = res
            return res

        return back(0, 0)
    
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]

        if text1[0] == text2[0]:
            dp[0][0] = 1

        for i in range(1, m):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]

        for j in range(1, n):
            if text1[0] == text2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
    
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
    
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)