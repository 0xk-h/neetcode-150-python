class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left = 0
        max_left = 0

        for c in s:
            if c == "(":
                min_left += 1
                max_left += 1

            elif c == ")":
                if max_left < 1:
                    return False

                max_left -= 1
                if min_left:
                    min_left -= 1
            
            else:
                max_left += 1
                if min_left:
                    min_left -= 1

        return min_left == 0
    
# Time Complexity: O(n)
# Space Complexity: O(1)