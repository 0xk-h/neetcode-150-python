class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n & 1:
                res += 1
            n >>= 1

        return res
    
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            if n % 2 != 0:
                res += 1

            n //= 2

        return res
    
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

# Time Complexity: O(log n)
# Space Complexity: O(1)