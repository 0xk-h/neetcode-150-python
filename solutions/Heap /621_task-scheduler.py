from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-val for val in freq.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            if maxHeap:
                curr = heapq.heappop(maxHeap)
                curr += 1
                if curr:
                    q.append((curr, time + n))
            else:
                time = q[0][1]

            while q and q[0][1] == time:
                val, _ = q.popleft()
                heapq.heappush(maxHeap, val)

            time += 1

        return time
            
# Time Complexity: O(n)
# Space Complexity: O(1)