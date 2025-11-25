from tree import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, m):
            if not root:
                return 0

            res = 1 if root.val >= m else 0
            res += dfs(root.left, max(m, root.val))
            res += dfs(root.right, max(m, root.val))

            return res

        return dfs(root, float("-inf"))
    
# Time Complexity: O(n)
# Space Complexity: O(n)