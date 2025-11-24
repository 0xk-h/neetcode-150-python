from typing import Optional
from tree import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stk = [(root, 1)]

        while stk:
            node, depth = stk.pop()

            if node:
                stk.append((node.right, depth + 1))
                stk.append((node.left, depth + 1))
            else:
                res = max(res, depth - 1)

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)