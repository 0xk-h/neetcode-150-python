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