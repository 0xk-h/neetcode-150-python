from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) -1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = 0
        for d in digits:
            num = (num * 10) + d

        num += 1

        return list(map(int, str(num)))
    
# Time Complexity: O(n)
# Space Complexity: O(n)