from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [i.lower() for i in s if i.isalnum()]
        return x == x[::-1]
    
# Time Complexity: O(n)
# Space Complexity: O(n)

