class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            x = 0
            while n:
                x += (n % 10) ** 2
                n //= 10

            n = x

        return True
    
# Time Complexity: O(log n) well accurately O(k log n) where k is number of iterations but k is small
# Space Complexity: O(log n)


class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(n):
            x = 0
            while n:
                x += (n % 10) ** 2
                n //= 10

            return x

        slow = n
        fast = calc(calc(n))

        while slow != fast:
            slow = calc(slow)
            fast = calc(calc(fast))

        return slow == 1
    
# Time Complexity: O(log n)
# Space Complexity: O(1)