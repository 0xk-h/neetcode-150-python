from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(n + 1):
            res[i] = res[i >> 1] + (i & 1)

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(num).count("1") for num in range(n + 1)]

# Time Complexity: O(n log n)
# Space Complexity: O(1)