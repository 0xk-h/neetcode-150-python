from typing import Optional
from tree import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 1

            left, right = dfs(root.left), dfs(root.right)

            if not left or not right or abs(left - right) > 1:
                return False

            return 1 + max(left, right)

        return True if dfs(root) else False
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            balanced = True
            if not left[0] or not right[0] or abs(left[1] - right[1]) > 1:
                balanced = False

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
    
# Time Complexity: O(n)
# Space Complexity: O(1)