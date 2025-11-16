from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bucket1 = [0] * 26
        bucket2 = [0] * 26
        for i in s:
            bucket1[ord(i) - ord("a")] += 1

        for i in t:
            bucket2[ord(i) - ord("a")] += 1

        return bucket1 == bucket2
    
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
# Time Complexity: O(n)
# Space Complexity: O(n)