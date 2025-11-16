from collections import Counter
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return sorted(set(nums), key=lambda x: -freq[x])[:k]
    
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        n = [(-freq[i], i) for i in set(nums)]
        heapq.heapify(n)

        res = [0] * k
        for i in range(k):
            res[i] = heapq.heappop(n)[1]

        return res

# Time Complexity: O(n + k log n)
# Space Complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        freq = [[] for _ in range(len(nums) +1)]

        for i, j in cnt.items():
            freq[j].append(i)

        res = []
        for i in range(len(freq) -1, -1, -1):
            while freq[i]:
                res.append(freq[i].pop())
                if len(res) == k:
                    return res
        return []
    
# Time Complexity: O(n)
# Space Complexity: O(n)