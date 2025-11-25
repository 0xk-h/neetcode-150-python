from tree import TreeNode
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

            else:
                res.append("#")

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        if data[0] == "#":
            return None
        
        root = TreeNode(int(data[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()

            if data[i] != "#":
                node.left = TreeNode(int(data[i]))
                q.append(node.left)

            i += 1

            if data[i] != "#":
                node.right = TreeNode(int(data[i]))
                q.append(node.right)

            i += 1

        return root

""""
Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
"""


# Time Complexity: O(n)
# Space complexity: O(n)
