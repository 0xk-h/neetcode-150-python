from typing import List
from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        inorder = {}
        for word in words:
            for l in word:
                inorder[l] = 0

        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]

            isFound = False
            for a, b in zip(prev, curr):
                if a != b:
                    isFound = True
                    if b not in adj[a]:
                        inorder[b] += 1
                        adj[a].add(b)
                        
                    break

            if not isFound and len(prev) > len(curr):
                return ""                    

        res = []
        q = deque()
        for a in inorder:
            if inorder[a] == 0:
                q.append(a)

        while q:
            a = q.popleft()
            res.append(a)

            for node in adj[a]:
                inorder[node] -= 1
                if inorder[node] == 0:
                    q.append(node)

        print(len(res), len(inorder))
        return "".join(res) if len(res) == len(inorder) else ""

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)

#--------------------------------------------------------------
#           Honorable Mentions [Wrong answer]
#--------------------------------------------------------------

class Node:
    def __init__(self, val = "?"):
        self.val = val
        self.next = self.prev = None

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        temp = []
        for j in range(100):
            acc = []
            for i in range(len(words)):
                if j < len(words[i]):
                    acc.append(words[i][j])

            if not acc:
                break
            temp.append("".join(acc))

        letter = {}
        self.lastL = Node()
        head = self.lastL

        def join_before(c, l):
            newNode = Node(c)
            letter[c] = newNode
            curr = letter[l]
            curr.prev.next = newNode
            newNode.prev = curr.prev
            newNode.next = curr
            curr.prev = newNode

        def join_after(c, l):
            newNode = Node(c)
            letter[c] = newNode
            curr = letter[l]
            if curr != self.lastL:
                curr.next.prev = newNode
                newNode.next = curr.next

            else:
                self.lastL = newNode

            newNode.prev = curr
            curr.next = newNode

        for word in temp:
            for i in range(len(word)):
                if word[i] in letter:
                    continue

                if i - 1 > 0:
                    join_after(word[i], word[i - 1])

                elif i + 1 < len(word) and word[i + 1] in letter:
                    join_before(word[i], word[i + 1])

                else:
                    newNode = Node(word[i])
                    self.lastL.next = newNode
                    newNode.prev = self.lastL
                    self.lastL = self.lastL.next
                    letter[word[i]] = newNode

        curr = head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next

        order = {x: i for i, x in enumerate(res)}

        for i in range(1, len(words)):
            curr = words[i]
            prev = words[i - 1]
            m, n = len(curr), len(prev)
            for j in range(min(m, n)):
                if curr[j] != prev[j]:
                    break

            if curr[j] == prev[j] and n > m:
                return ""

            if order[curr[j]] < order[prev[j]]:
                return ""

        return "".join(res)

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)