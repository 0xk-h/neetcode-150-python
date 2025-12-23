class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def back(i, j, k, s):
            if len(s) == len(s3):
                return s == s3

            if (i, j) in memo:
                return memo[(i, j)] == 1

            curr = False
            if i < len(s1) and s1[i] == s3[k]:
                curr = back(i + 1, j, k + 1, s + s1[i])

            if not curr and j < len(s2) and s2[j] == s3[k]:
                curr = back(i, j + 1, k + 1, s + s2[j])

            memo[(i, j)] = 1 if curr else 2
            return curr

        return back(0, 0, 0, "")
    
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])

        return dp[-1][-1]
    
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)