from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        q = deque([beginWord])
        seen = set()
        res = 1
        while q:
            res += 1

            for _ in range(len(q)):
                currWord = q.popleft()
                for word in wordList:
                    if word not in seen and sum(1 for i, j in zip(word, currWord) if i != j) == 1:
                        if word == endWord:
                            return res

                        q.append(word)
                        seen.add(word)

        return 0
    
# Time Complexity: O(n^2 * m)
# Space Complexity: O(n)


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        for word in wordList:
            x = list(word)
            for i in range(len(word)):
                temp = x[i]
                x[i] = "*"
                adj["".join(x)].append(word)
                x[i] = temp

        q = deque([beginWord])
        seen = set()
        res = 1
        while q:
            res += 1

            for _ in range(len(q)):
                currWord = q.popleft()
                x = list(currWord)
                for i in range(len(x)):
                    temp = x[i]
                    x[i] = "*"

                    for word in adj["".join(x)]:
                        if word not in seen:
                            if word == endWord:
                                return res

                            q.append(word)
                            seen.add(word)
                            
                    x[i] = temp

        return 0
    
# Time Complexity: O(n * m^2)
# Space Complexity: O(n * m^2)