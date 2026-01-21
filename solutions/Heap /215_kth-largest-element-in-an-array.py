from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)

            elif num > heap[0]:
                heapq.heappushpop(heap, num)

        return heap[0]
    
# Time Complexity: O(n log k)
# Space Complexity: O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
    
# Time Complexity: O(n log k)
# Space Complexity: O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
    
# Time Complexity: O(n log n)
# Space Complexity: O(1)