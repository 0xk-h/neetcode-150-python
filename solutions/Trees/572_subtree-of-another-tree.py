from typing import Optional
from tree import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def check(root, subroot):
            if not root and not subroot:
                return True

            if not root or not subroot or root.val != subroot.val:
                return False

            return check(root.left, subroot.left) and check(root.right, subroot.right)

        return check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
# Time Complexity: O(n * m)
# Space Complexity: O(1)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def tostr(root):
            if not root:
                return "*"
            return "<" + str(root.val) + tostr(root.left) + tostr(root.right) + ">"

        return tostr(subRoot) in tostr(root)