class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]

        curr.end = True


    def search(self, word: str) -> bool:

        def dfs(curr, i):
            if i == len(word):
                return curr.end

            if word[i] == ".":
                for node in curr.child.values():
                    if dfs(node, i + 1):
                        return True

            elif word[i] in curr.child:
                return dfs(curr.child[word[i]], i + 1)

            return False

        return dfs(self.root, 0)

"""
Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(word)
"""

# Time Complexity: O(n)
# Space complexity: O(t)