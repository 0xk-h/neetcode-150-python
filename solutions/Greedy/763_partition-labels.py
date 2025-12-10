from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        l, end = 0, 0
        res = []
        for r in range(len(s)):
            end = max(end, last[s[r]])

            if r == end:
                res.append(r - l + 1)
                l = r + 1

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)