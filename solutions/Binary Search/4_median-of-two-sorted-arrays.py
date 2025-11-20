from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        pivot = (m + n) // 2
        l, r = 0, m - 1

        while True:
            i = l + (r-l) // 2
            j = pivot - i - 2

            left1 = nums1[i] if i >= 0 else float("-inf")
            left2 = nums2[j] if j >= 0 else float("-inf")
            right1 = nums1[i + 1] if (i + 1) < m else float("inf")
            right2 = nums2[j + 1] if (j + 1) < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2

                else:
                    return min(right1, right2)

            elif right1 < left2:
                l = i + 1
            else:
                r = i - 1

# Time Complexity: O(log min(m, n))
# Space Complexity: O(1)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1

            else:
                res.append(nums2[j])
                j += 1

        if i < len(nums1):
            res.extend(nums1[i:])
        if j < len(nums2):
            res.extend(nums2[j:])

        n = len(res)
        if n % 2 == 0:
            return (res[n//2 - 1] + res[n//2]) / 2
        else:
            return res[n//2]
        
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)


from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        return median(sorted(nums1 + nums2))
    
# Time Complexity: O((m + n) log(m + n))
# Space Complexity: O(m + n)


import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = list(heapq.merge(nums1, nums2))
        n = len(res)
        if n % 2 == 0:
            return (res[n//2 - 1] + res[n//2]) / 2
        else:
            return res[n//2]
        
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)
        n = len(res)
        if n % 2 == 0:
            return (res[n//2 - 1] + res[n//2]) / 2
        else:
            return res[n//2]
        
# Time Complexity: O((m + n) log(m + n))
# Space Complexity: O(m + n)