from typing import List
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        window = {}
        for i in t:
            countT[i] = countT.get(i, 0) + 1

        res = ""
        m = len(s)
        have, need = 0, len(countT)
        l = 0
        for r in range(m):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if window[c] == countT.get(c, 0):
                have += 1

            while l < m and window.get(s[l], 0) > countT.get(s[l], 0):
                window[s[l]] -= 1
                l += 1

            if have == need:
                if not res or len(res) > (r - l + 1):
                    res = s[l: r + 1]

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        h = Counter()
        m, n = len(s), len(t)
        res = ""
        
        matches = 0
        l = 0
        for r in range(m):

            h[s[r]] += 1
            if h[s[r]] == t[s[r]]:
                matches += 1

            while l < m and h[s[l]] > t[s[l]]:
                h[s[l]] -= 1
                l += 1

            if matches == n and (not res or len(res) > (r - l + 1)):
                res = s[l: r + 1]

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)