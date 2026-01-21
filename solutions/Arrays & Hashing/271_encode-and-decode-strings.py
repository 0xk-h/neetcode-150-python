from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "-" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            curr = ""
            d = ""
            while s[i] != "-":
                d += s[i]
                i += 1
            d = int(d)

            for _ in range(d):
                i += 1
                curr += s[i]

            i += 1
            res.append(curr)

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)