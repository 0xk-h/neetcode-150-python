class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = (0, 1)
        maxLen = 1

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if maxLen < r - l + 1:
                    maxLen = r - l + 1
                    res = (l, r + 1)

                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if maxLen < r - l + 1:
                    maxLen = r - l + 1
                    res = (l, r + 1)

                l -= 1
                r += 1

        l, r = res
        return s[l: r]
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = (0, 1)
        maxLen = 1

        for i in range(n):
            for j in range(i + maxLen, n):
                isPali = True
                l, r = i, j
                while l < r:
                    if s[l] != s[r]:
                        isPali = False
                        break

                    l += 1
                    r -= 1
                
                if isPali:
                    maxLen = j - i + 1
                    res = (i, j + 1)

        l, r = res
        return s[l: r]
    
# Time Complexity: O(n^3)
# Space Complexity: O(1)