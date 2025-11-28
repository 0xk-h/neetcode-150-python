from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def back(left, s):
            if s == target:
                res.append(subset.copy())
                return

            for i in range(left, len(candidates)):
                if s + candidates[i] > target:
                    continue
                    
                subset.append(candidates[i])
                back(i, s + candidates[i])
                subset.pop()
        
        back(0,0)
        return res
    
# Time Complexity: O(n^t)
# Space Complexity: O(t/m)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def back(i, s):
            if s == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or s > target:
                return

            subset.append(candidates[i])
            back(i, s + candidates[i])

            subset.pop()
            back(i + 1, s)

        
        back(0,0)
        return res
    
# Time Complexity: O(2^t)
# Space Complexity: O(t/m)