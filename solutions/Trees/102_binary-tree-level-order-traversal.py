from typing import Optional, List
from tree import TreeNode
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)

            if level:
                res.append(level)

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stk = [(root, 0)]

        while stk:
            node, depth = stk.pop()

            if node:
                if len(res) == depth:
                    res.append([])

                res[depth].append(node.val)
                stk.append((node.right, depth + 1))
                stk.append((node.left, depth + 1))

        return res
            
# Time Complexity: O(n)
# Space Complexity: O(n)