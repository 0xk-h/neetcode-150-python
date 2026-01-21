from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        res = [0, 0, 0]

        for i, j, k in triplets:
            if i <= x and j <= y and k <= z:
                res[0] = max(res[0], i)
                res[1] = max(res[1], j)
                res[2] = max(res[2], k)

        return res == target
    
# Time Complexity: O(n)
# Space Complexity: O(1)