from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        self.res = n

        def find(n1):
            if par[n1] != n1:
                par[n1] = find(par[n1])

            return par[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 != p2:
                self.res -= 1
                par[p1] = p2
                return True

            else:
                return False

        for i, j in edges:
            if not union(i, j):

                return False

        return self.res == 1
    
# Time Complexity: O(E * α(V))
# Space Complexity: O(V)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [1] * n
        self.res = n

        def find(n1):
            if par[n1] != n1:
                par[n1] = find(par[n1])

            return par[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 != p2:
                self.res -= 1

                if rank[p1] < rank[p2]:
                    par[p1] = p2
                    rank[p2] += rank[p1]

                else:
                    par[p2] = p1
                    rank[p1] += rank[p2]

                return True

            else:
                return False

        for i, j in edges:
            if not union(i, j):

                return False

        return self.res == 1
    
# Time Complexity: O(E * α(V))
# Space Complexity: O(V)