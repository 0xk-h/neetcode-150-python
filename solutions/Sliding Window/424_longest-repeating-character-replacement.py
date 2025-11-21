from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = {}
        l = 0
        res = 1
        maxf = 0

        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxf = max(maxf, freq[s[r]])

            if (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = Counter()
        l = 0
        res = 1

        for r in range(n):
            freq[s[r]] += 1

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)