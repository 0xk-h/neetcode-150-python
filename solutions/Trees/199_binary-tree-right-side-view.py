from typing import List, Optional
from tree import TreeNode
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)

            if level:
                res.append(level[-1])

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = [(root, 0)]

        while stk:
            node, depth = stk.pop()

            if node:
                if len(res) == depth: res.append(0)

                res[depth] = node.val
                stk.append((node.right, depth + 1))
                stk.append((node.left, depth + 1))

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)