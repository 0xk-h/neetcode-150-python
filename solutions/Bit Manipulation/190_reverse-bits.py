class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:][::-1] + "0" * (34 - len(bin(n))), 2)
    
# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def reverseBits(self, n: int) -> int:
        p = 31
        res = 0
        bit = bin(n)[::-1]

        for b in bit[:-2]:
            if b == "1":
                res += 2 ** p

            p -= 1

        return res

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def reverseBits(self, n: int) -> int:
        p = 31
        res = 0

        while n:
            if n & 1:
                res += 2 ** p

            n >>= 1
            p -= 1

        return res

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def reverseBits(self, n: int) -> int:
        p = 31
        res = 0

        while n:
            res |= (n & 1) << p
            n >>= 1
            p -= 1

        return res

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1

        return res

# Time Complexity: O(1)
# Space Complexity: O(1)