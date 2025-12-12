from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        child = defaultdict(list)

        for x, y in prerequisites:
            child[x].append(y)

        path = set()
        def dfs(node):
            if node in path:
                return False

            path.add(node)
            for n1 in child[node]:
                if not dfs(n1):
                    return False

            path.remove(node)
            child[node] = []
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
    
# Time Complexity: O(v + e)
# Space Complexity: O(v + e)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses

        child = {i : [] for i in range(numCourses)}
        for u, v in prerequisites:
            indeg[u] += 1
            child[v].append(u)

        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)

        res = 0
        while q:
            res += 1

            node = q.popleft()
            for c in child[node]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    q.append(c)

        return res == numCourses
    
# Time Complexity: O(v + e)
# Space Complexity: O(v + e)