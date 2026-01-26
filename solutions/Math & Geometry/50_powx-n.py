class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n
    
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNeg = n < 0
        n = abs(n)

        memo = {}
        def back(p):
            if p == 0:
                return 1

            if p in memo:
                return memo[p]

            if p % 2 == 0:
                memo[p] = back(p // 2) * back(p // 2)
                return memo[p]

            else:
                memo[p] = x * back(p - 1)
                return memo[p]

        res = back(n)
        return res if not isNeg else 1 / res
    
# Time Complexity: O(log n)
# Space Complexity: O(log n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNeg = n < 0
        n = abs(n)
        res = 1

        while n:
            if n & 1:
                res *= x

            x *= x
            n >>= 1

        return res if not isNeg else 1 / res

# Time Complexity: O(log n)
# Space Complexity: O(1)