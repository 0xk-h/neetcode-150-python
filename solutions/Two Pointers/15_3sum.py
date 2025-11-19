from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) -2):
            if i and nums[i -1] == nums[i]:
                continue

            j, k = i +1, len(nums) -1

            while j < k:
                x = nums[i] + nums[j] + nums[k]

                if x == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1
                    
                elif x > 0:
                    k -= 1
                else:
                    j += 1

        return res
    
# Time Complexity: O(n^2)      [n^2 + nlogn]
# Space Complexity: O(1)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) -2):
            if i and nums[i -1] == nums[i]:
                continue

            j, k = i +1, len(nums) -1
            seen = set()

            while j < k:
                x = nums[i] + nums[j] + nums[k]

                if x == 0 and (nums[j], nums[k]) not in seen:
                    res.append([nums[i], nums[j], nums[k]])
                    seen.add((nums[j], nums[k]))
                elif x > 0:
                    k -= 1
                else:
                    j += 1

        return res

# Time Complexity: O(n^2)      [n^2 + nlogn]
# Space Complexity: O(n)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seen = set()

        for i in range(len(nums) -2):
            if nums[i] in seen:
                continue
            else:
                seen.add(nums[i])

            h = {}
            for j in range(i +1, len(nums)):

                if nums[j] in h:
                    a, b = h[nums[j]]
                    c = nums[j]
                    
                    # manual sorting
                    if a > b: a, b = b, a
                    if b > c: b, c = c, b
                    if a > b: a, b = b, a

                    res.add((a, b, c))
                    del h[nums[j]]

                else:
                    h[- nums[i] - nums[j]] = (nums[i], nums[j])

        return [[i, j, k] for i,j,k in res]

# Time Complexity: O(n^2)      [n^2]
# Space Complexity: O(n)                 