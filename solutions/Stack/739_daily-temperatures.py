from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        stk = []
        res = [0] * n

        for i in range(n):
            while stk and temp[stk[-1]] < temp[i]:
                j = stk.pop()
                res[j] = i - j

            stk.append(i)

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)