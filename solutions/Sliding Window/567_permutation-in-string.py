from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n: return False
        c1 = [0] * 26
        c2 = [0] * 26

        for i, j in zip(s1, s2):
            c1[ord(i) - 97] += 1
            c2[ord(j) - 97] += 1

        matches = sum(c1[i] == c2[i] for i in range(26))

        for i in range(n, len(s2)):
            if matches == 26:
                return True

            rindex = ord(s2[i]) - 97
            lindex = ord(s2[i - n]) - 97

            c2[rindex] += 1
            if c1[rindex] == c2[rindex]:
                matches += 1
            elif c1[rindex] + 1 == c2[rindex]:
                matches -= 1

            c2[lindex] -= 1
            if c1[lindex] == c2[lindex]:
                matches += 1
            elif c1[lindex] - 1 == c2[lindex]:
                matches -= 1

        return matches == 26
            
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = Counter(s1)
        res = Counter(s2[:n])

        if s1 == res: return True

        for r in range(n, len(s2)):
            res[s2[r]] += 1
            res[s2[r - n]] -= 1

            if s1 == res:
                return True

        return False
    
# Time Complexity: O(26 * n)
# Space Complexity: O(1)


#----------------------------------------------------------------------------
#      Works if there is no duplicate characters
#----------------------------------------------------------------------------
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        bit1 = 0
        bit2 = 0

        for i, j in zip(s1, s2):
            bit1 |= 1 << (ord(i) - ord("a"))
            bit2 |= 1 << (ord(j) - ord("a"))

        if bit1 == bit2: return True

        for r in range(n, len(s2)):
            if bit1 == bit2:
                return True
            
            bit2 |= 1 << (ord(s2[r]) - ord("a"))
            bit2 ^= 1 << (ord(s2[r - n]) - ord("a"))

        return bit1 == bit2