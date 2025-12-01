from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = res = nums[0]

        for num in nums[1:]:
            if num < 0:
                a, b = b, a

            a = min(num, a * num)
            b = max(num, b * num)
            res = max(res, b)

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)


# First implementation
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = 1          # min
        b = 1          # max

        res = nums[0]

        for num in nums:
            if num == 0:
                a, b = 1, 1
                res = max(res, 0)

            else:
                x, y = a*num, b*num 
                a = min(x, y, num)
                b = max(x, y, num)
                res = max(res, b)

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)