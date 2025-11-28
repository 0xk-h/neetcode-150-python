from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def back(i):
            res.append(subset.copy())

            prev = 11
            for j in range(i, len(nums)):
                if prev == nums[j]:
                    continue
                
                subset.append(nums[j])
                back(j + 1)
                subset.pop()
                prev = nums[j]

        back(0)
        return res
    
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def back(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            back(i + 1)
            subset.pop()

            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            back(i)

        back(0)
        return res
    
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)