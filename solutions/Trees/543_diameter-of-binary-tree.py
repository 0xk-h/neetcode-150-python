from typing import Optional
from tree import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def back(root):
            if not root:
                return 0

            left, right = back(root.left), back(root.right)
            res[0] = max(res[0], left + right)

            return 1 + max(left, right)

        back(root)
        return res[0]
    
# Time Complexity: O(n)
# Space Complexity: O(1)
