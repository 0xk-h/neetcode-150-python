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
        self.word = word

        def dfs(curr, i):
            if i == len(self.word):
                return curr.end

            if self.word[i] == ".":
                for node in curr.child.values():
                    if dfs(node, i + 1):
                        return True

            else:
                if self.word[i] in curr.child:
                    return dfs(curr.child[self.word[i]], i + 1)

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