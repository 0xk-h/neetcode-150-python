from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def back(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            back(i + 1)
            subset.pop()
            back(i + 1)

        back(0)
        return res
    
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            res.extend([subset + [num] for subset in res])

        return res
    
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)