from typing import List, Optional
from tree import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        node = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return node
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)