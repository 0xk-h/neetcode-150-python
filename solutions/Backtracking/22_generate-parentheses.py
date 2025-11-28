from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def back(l, r, subset):
            if l + r == n+n:
                res.append(subset)
                return

            if l < n: back(l+1, r, subset+"(")

            if r < l: back(l, r+1, subset+")")

        back(0, 0, "")
        return res
    
# Time Complexity: O(2^2n)
# Space Complexity: O(n)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        
        def back(l, r):
            if l + r == n+n:
                res.append("".join(subset))
                return

            if l < n:
                subset.append("(")
                back(l+1, r)
                subset.pop()

            if r < l:
                subset.append(")")
                back(l, r+1)
                subset.pop()

        back(0, 0)
        return res
    
# Time Complexity: O(2^2n)
# Space Complexity: O(n)