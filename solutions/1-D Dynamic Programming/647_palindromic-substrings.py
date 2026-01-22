class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                x = s[i: j + 1]
                if x == x[::-1]:
                    res += 1

        return res
    
# Time Complexity: O(n^3)
# Space Complexity: O(1)


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for mid in range(len(s)):
            i, j = mid, mid
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1

            i, j = mid, mid+ 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
                
        return res
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)