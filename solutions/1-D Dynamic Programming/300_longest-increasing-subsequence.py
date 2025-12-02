from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        h = {}

        for curr in nums:
            max_value = 1

            for prev in h:
                if prev < curr:
                    max_value = max(max_value, h[prev] + 1)

            h[curr] = max_value

        return max(h.values())
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for num in nums[1:]:
            if dp[-1] < num:
                dp.append(num)

            else:
                l, r = 0, len(dp) -1
                while l < r:
                    mid = l + (r-l) // 2

                    if dp[mid] < num:
                        l = mid + 1
                    else:
                        r = mid

                dp[l] = num

        return len(dp)
    
# Time Complexity: O(n logn)
# Space Complexity: O(n)