from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i in nums:
            if i-1 not in nums:
                cnt = 1
                while i + 1 in nums:
                    cnt += 1
                    i += 1
                res = max(res, cnt)

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)


class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)

        if p1 != p2:
            if self.size[p1] > self.size[p2]:
                self.par[p2] = p1
                self.size[p1] += self.size[p2]
                return self.size[p1]

            else:
                self.par[p1] = p2
                self.size[p2] += self.size[p1]
                return self.size[p2]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        nums = {val : ind for ind, val in enumerate(nums)}

        dsu = DSU(n)

        res = 1
        for i in nums:
            if i -1 in nums:
                res = max(dsu.union(nums[i], nums[i -1]), res)
        
        return res
    
# Time Complexity: amortized O(n)
# Space Complexity: O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        nums = {val : ind for ind, val in enumerate(nums)}
        par = [i for i in range(n)]
        size = [1] * n

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        def union(x, y):
            p1 = find(x)
            p2 = find(y)

            if p1 != p2:
                if size[p1] > size[p2]:
                    par[p2] = p1
                    size[p1] += size[p2]

                else:
                    par[p1] = p2
                    size[p2] += size[p1]

        for i in nums:
            if i -1 in nums:
                union(nums[i], nums[i -1])
        
        return max(size)
    
# Time Complexity: amortized O(n)
# Space Complexity: O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = defaultdict(int)
        res = 0

        for i in nums:
            if not h[i]:
                h[i] = h[i - 1] + 1 + h[i + 1]
                h[i - h[i - 1]] = h[i]
                h[i + h[i + 1]] = h[i]

                res = max(res, h[i])

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))

        res = 0
        cnt = 1
        for i in range(len(nums)):
            if nums[i -1] + 1 == nums[i]:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1

        return max(res, cnt)
    
# Time Complexity: O(n log n)
# Space Complexity: O(n)