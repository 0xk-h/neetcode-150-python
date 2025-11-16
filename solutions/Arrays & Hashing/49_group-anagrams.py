from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for i in strs:
            h[tuple(sorted(i))].append(i)

        return list(h.values())
    
# Time Complexity: O(n * k . logk) where n is number of strings and k is max length of a string
# Space Complexity: O(n * k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for i in strs:
            h["".join(sorted(i))].append(i)

        return list(h.values())
    
# Time Complexity: O(n * k . logk) where n is number of strings and k is max length of a string
# Space Complexity: O(n * k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for i in strs:
            bucket = [0] * 26
            for j in i:
                bucket[ord(j) - ord("a")] += 1

            key = tuple(bucket)
            if key in h:
                h[key].append(i)
            else:
                h[key] = [i]

        return list(h.values())
    
# Time Complexity: O(n * k) where n is number of strings and k is max length of a string
# Space Complexity: O(n * k)
