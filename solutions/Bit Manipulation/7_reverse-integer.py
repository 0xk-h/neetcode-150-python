class Solution:
    def reverse(self, x: int) -> int:
        isNeg = True if x < 0 else False
        res = 0
        x = abs(x)

        while x > 9:
            res *= 10
            res += x % 10
            x //= 10

        last = x % 10
        if isNeg:
            if res > 214748364 or (res == 214748364 and last == 9):
                return 0

            return -(res * 10 + last)

        else:
            if res > 214748364 or (res == 214748364 and last >= 8):
                return 0

            return res * 10 + last

# Time Complexity: O(log10(n))
# Space Complexity: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        isNeg = True if x < 0 else False
        res = 0
        x = abs(x)

        while x:
            res *= 10
            res += x % 10
            x //= 10

        res = -res if isNeg else res

        if -2**31 <= res <= 2**31 - 1:
            return res
        
        return 0
    
# Time Complexity: O(log10(n))
# Space Complexity: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        isNeg = True if x < 0 else False
        res = int(str(abs(x))[::-1])
        res = -res if isNeg else res

        if -2**31 <= res <= 2**31 - 1:
            return res
        
        return 0
    
# Time Complexity: O(log10(n))
# Space Complexity: O(log10(n))