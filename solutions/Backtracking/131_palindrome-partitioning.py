from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def back(i):
            if i >= len(s):
                res.append(subset.copy())
                return

            for j in range(i,len(s)):
                word = s[i: j+1]
                if word == word[::-1]:
                    subset.append(s[i: j+1])
                    back(j+1)
                    subset.pop()

        back(0)
        return res
    
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1

            return True

        def back(i):
            if i >= len(s):
                res.append(subset.copy())
                return

            for j in range(i,len(s)):
                if isPali(s, i, j):
                    subset.append(s[i: j+1])
                    back(j+1)
                    subset.pop()

        back(0)
        return res
    
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)