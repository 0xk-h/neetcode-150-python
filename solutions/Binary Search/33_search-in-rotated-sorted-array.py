from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[0]:
                if nums[mid] > target and nums[0] <= target:
                    r = mid - 1
                else:
                    l = mid + 1

            else: 
                if nums[mid] < target and nums[-1] >= target:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
    
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        
        # To find the pivot element(min)
        while l < r:
            mid = l + (r-l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        # Determining which subarr to search
        if target <= nums[-1]:
            l, r = l, len(nums) -1
        else:
            l, r = 0, l

        # Standard binary search
        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
    
# Time Complexity: O(log n)
# Space Complexity: O(1)