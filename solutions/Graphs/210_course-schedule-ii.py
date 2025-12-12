from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses

        child = {i : [] for i in range(numCourses)}
        for u, v in prerequisites:
            child[v].append(u)
            indeg[u] += 1

        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for c in child[node]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    q.append(c)

        return res if len(res) == numCourses else []
    
# Time Complexity: O(v + e)
# Space Complexity: O(v + e)