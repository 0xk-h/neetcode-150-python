from typing import List
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        heap = list(count)
        heapq.heapify(heap)

        while heap:
            val = heap[0]
            for i in range(groupSize):
                if val + i not in count or count[val + i] == 0:
                    return False

                count[val + i] -= 1
                
            while heap and count[heap[0]] == 0:
                heapq.heappop(heap)

        return True

# Time Complexity: O(n logn)
# Space Complexity: O(n)