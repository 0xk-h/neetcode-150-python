from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i == "+":
                b, a = stk.pop(), stk.pop()
                stk.append(a + b)

            elif i == "-":
                b, a = stk.pop(), stk.pop()
                stk.append(a - b)

            elif i == "*":
                b, a = stk.pop(), stk.pop()
                stk.append(a * b)

            elif i == "/":
                b, a = stk.pop(), stk.pop()
                stk.append(int(a / b))

            else:
                stk.append(int(i))

        return stk[0]
    
# Time Complexity: O(n)
# Space Complexity: O(n)