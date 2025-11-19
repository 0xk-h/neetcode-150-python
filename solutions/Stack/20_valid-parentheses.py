from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stk = []

        for i in s:
            if i not in h:
                stk.append(i)

            elif not stk or stk.pop() != h[i]:
                return False

        return not stk

# Time Complexity: O(n)
# Space Complexity: O(n)


# Older implementation
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        h = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in h:
                if not stk:
                    return False
                if stk and stk.pop() != h[i]:
                    return False
            else:
                stk.append(i)
        return not stk

# Time Complexity: O(n)
# Space Complexity: O(n)