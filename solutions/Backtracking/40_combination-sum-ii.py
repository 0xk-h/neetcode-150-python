from typing import List

class Solution:
    def combinationSum2(self, candi: List[int], target: int) -> List[List[int]]:
        candi.sort()
        res = []
        subset = []

        def back(i, s):
            if s == target:
                res.append(subset.copy())
                return

            if i >= len(candi) or s > target:
                return

            subset.append(candi[i])
            back(i + 1, s + candi[i])
            subset.pop()

            i += 1
            while i < len(candi) and candi[i] == candi[i - 1]:
                i += 1
            back(i, s)

        back(0,0)
        return res
    
# Time Complexity: O(2^t)
# Space Complexity: O(2^t)


class Solution:
    def combinationSum2(self, candi: List[int], target: int) -> List[List[int]]:
        candi.sort()
        res = []
        subset = []

        def back(left, s):
            if s == target:
                res.append(subset.copy())
                return

            prev = -1
            for i in range(left, len(candi)):
                if s + candi[i] > target:
                    return
                
                if prev == candi[i]:
                    continue

                subset.append(candi[i])
                back(i + 1, s + candi[i])
                subset.pop()
                prev = candi[i]

        back(0,0)
        return res
    
# Time Complexity: O(2^t)
# Space Complexity: O(2^t)