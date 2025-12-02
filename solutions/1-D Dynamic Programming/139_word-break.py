from typing import List

class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.child:
                    curr.child[c] = TrieNode()
                curr = curr.child[c]
            
            curr.end = True

        memo = {}
        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            curr = root
            for j in range(i, len(s)):
                if s[j] not in curr.child:
                    break
                                     
                curr = curr.child[s[j]]
                if curr.end and dfs(j + 1):
                    return True

            memo[i] = False
            return False

        return dfs(0)
    
# Time Complexity: O(n)
# Space Complexity: O(m)