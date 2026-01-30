class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m -1, -1, -1):
            for j in range(n -1, -1, -1):
                x = res[i + j + 1] + int(num1[i]) * int(num2[j])
                res[i + j + 1] = x % 10
                res[i + j] += x // 10

        for i in range(m + n):
            if res[i] != 0:
                return "".join(str(x) for x in res[i:])

        return "0"
    
# Time Complexity: O(m * n)
# Space Complexity: O(m + n)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
    
# Time Complexity: O(m + n)
# Space Complexity: O(1)