class TrieNode:
    def __init__(self, end = False):
        self.child = {}
        self.end = end

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.child:
                curr.child[i] = TrieNode()
            curr = curr.child[i]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.child:
                return False
            curr = curr.child[i]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i not in curr.child:
                return False
            curr = curr.child[i]

        return True

# Time Complexity: O(n)
# Space complexity: O(t)


class TrieNode:
    def __init__(self, end = False):
        self.child = [0]*26
        self.end = end

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - 97
            if not curr.child[idx]:
                curr.child[idx] = TrieNode()
            curr = curr.child[idx]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = ord(c) - 97
            if not curr.child[idx]:
                return False
            curr = curr.child[idx]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            idx = ord(c) - 97
            if not curr.child[idx]:
                return False
            curr = curr.child[idx]

        return True
    
"""     
Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
"""
        
# Time Complexity: O(n)
# Space complexity: O(t)