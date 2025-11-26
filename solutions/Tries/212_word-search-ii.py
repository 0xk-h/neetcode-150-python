from typing import List

class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.deleted = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = []
        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.child:
                    curr.child[c] = TrieNode()
                curr = curr.child[c]

            curr.end = True

        def back(curr, i, j, word):
            if curr.end and not curr.deleted:
                res.append(word)
                remove(root, 0, word)

            if (i, j) in seen or curr.deleted or i < 0 or i >= m or j < 0 or j >= n:
                return

            seen.add((i, j))
            c = board[i][j]
            if c in curr.child:
                node = curr.child[c]
                back(node, i - 1, j, word+c)
                back(node, i + 1, j, word+c)
                back(node, i, j + 1, word+c)
                back(node, i, j - 1, word+c)

            seen.remove((i, j))

        def remove(curr, i, word):
            if len(word) == i:
                if curr.child:
                    curr.end = False
                else:
                    curr.deleted = True
                
                return curr.end

            c = word[i]
            delete = remove(curr.child[c], i + 1, word)
            if delete and not curr.end and len(curr.child) == 1:
                curr.deleted = True
                
            return curr.deleted

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.child:
                    seen = set()
                    back(root, i, j, "")

        return res
    
# Time Complexity: O(m * n * t)
# Space complexity: O(m * n + t)