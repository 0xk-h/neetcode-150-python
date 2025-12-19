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