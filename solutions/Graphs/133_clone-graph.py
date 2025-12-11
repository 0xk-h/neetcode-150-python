from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        seen = [0] * 101
        def dfs(node):
            if seen[node.val]:
                return seen[node.val]

            root = Node(node.val)
            seen[node.val] = root
            for neighbour in node.neighbors:
                root.neighbors.append(dfs(neighbour))

            return root

        return dfs(node)
    
# Time Complexity: O(v + e)
# Space Complexity: O(1)