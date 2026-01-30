from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        total = len(tickets)
        tickets.sort(reverse = True)
        adj = defaultdict(list)

        for u, v in tickets:
            adj[u].append(v)

        res = []
        def back(node):

            while adj[node]:
                back(adj[node].pop())

            res.append(node)

        back("JFK")
        return res[::-1]
    
# Time Complexity: O(E log E)
# Space Complexity: O(E)


#-----------------------------------------------------
#              TLE Solutions
#-----------------------------------------------------
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        total = len(tickets)
        tickets.sort()
        adj = defaultdict(list)

        for u, v in tickets:
            adj[u].append(v)

        seen = set()
        res = ["JFK"]
        def back(node):
            if len(res) == total + 1:
                return True

            for v in adj[node]:
                if (node, v) in seen:
                    continue

                seen.add((node, v))
                res.append(v)
                if back(v):
                    return True
                res.pop()
                seen.remove((node, v))

        back("JFK")
        return res
    
# Time Complexity: O(E!)
# Space Complexity: O(E)