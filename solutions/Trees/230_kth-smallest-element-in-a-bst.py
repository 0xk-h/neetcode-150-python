from typing import Optional
from tree import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = -1

        def inorder(root):
            if not root or self.res != -1:
                return

            inorder(root.left)

            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return

            inorder(root.right)

        inorder(root)
        return self.res
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)

        return arr[k - 1]
    
# Time Complexity: O(n)
# Space Complexity: O(n)