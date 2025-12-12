from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]

        def find(n1):
            while par[n1] != n1:
                par[n1] = par[par[n1]]
                n1 = par[n1]

            return n1

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            par[p1] = p2
            return True

        for i, j in edges:
            if not union(i, j):
                return [i, j]
            
# Time Complexity: O(n)
# Space Complexity: O(n)