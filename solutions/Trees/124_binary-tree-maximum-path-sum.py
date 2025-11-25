from typing import Optional
from tree import TreeNode

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(root):
            if not root:
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            self.res = max(self.res, left + root.val + right)
            return root.val + max(left, right)

        dfs(root)
        return self.res
    
# Time Complexity: O(n)
# Space Complexity: O(n)