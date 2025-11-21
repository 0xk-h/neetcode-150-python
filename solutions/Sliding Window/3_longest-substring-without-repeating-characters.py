from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l, r = 0, 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)

            res = max(res, r - l + 1)
            mp[s[r]] = r
 
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            res = max(res, r - l + 1)
            seen.add(s[r])

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        seen = deque()

        for r in range(len(s)):
            while s[r] in seen:
                seen.popleft()
                l += 1

            res = max(res, r - l + 1)
            seen.append(s[r])

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)