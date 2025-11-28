from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []
        pick = [False] * n

        def back(i):
            if i == n:
                res.append(subset.copy())
                return

            for j in range(n):
                if not pick[j]:
                    pick[j] = True
                    subset.append(nums[j])
                    back(i + 1)
                    pick[j] = False
                    subset.pop()

        back(0)
        return res
    
# Time Complxity: O(n * n!)
# Space Complexity: O(n * n!)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []

        def back(i, pick):
            if i == n:
                res.append(subset.copy())
                return

            for j in range(n):
                if not pick & (1 << j):
                    pick |= 1 << j
                    subset.append(nums[j])
                    back(i + 1, pick)
                    pick ^= 1 << j
                    subset.pop()

        back(0, 0)
        return res

# Time Complxity: O(n * n!)
# Space Complexity: O(n * n!)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in permutations(nums)]