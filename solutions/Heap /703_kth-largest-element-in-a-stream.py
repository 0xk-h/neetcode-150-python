from typing import List
from bisect import insort
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0] 
   
#---------------------------------------------------------
#           Time Complexity:
#           init:    O(n)
#           add:     O(logn)
#           
#           Space Complexity:
#           O(n)
#---------------------------------------------------------


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.nums.sort()

    def add(self, val: int) -> int:
        insort(self.nums, val)
        return self.nums[max(0, len(self.nums) - self.k)]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#---------------------------------------------------------
#           Time Complexity:
#           init:    O(n logn)
#           add:     O(n)
#           
#           Space Complexity:
#           O(n)
#---------------------------------------------------------