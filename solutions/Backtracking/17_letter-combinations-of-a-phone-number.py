from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        subset = []
        digit_to_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def back(i):

            if i == len(digits):
                res.append("".join(subset))
                return

            for c in digit_to_letter[digits[i]]:
                subset.append(c)
                back(i+1)
                subset.pop()

        back(0)
        return res
    
# Time Complexity: O(n * 4^n)
# Space Complexity: O(n * 4^n)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = [""]
        for digit in digits:
            temp = []
            for curr in res:
                for c in digit_to_letter[digit]:
                    temp.append(curr + c)

            res = temp

        return res
    
# Time Complexity: O(n * 4^n)
# Space Complexity: O(n * 4^n)