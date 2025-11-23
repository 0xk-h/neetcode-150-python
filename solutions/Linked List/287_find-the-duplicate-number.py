from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = nums[0]
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow2

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = 0
        for num in nums:
            if 1 << num & seen:
                return num
            seen |= 1 << num
        return -1
        
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        res = 0
        for b in range(17):
            cnt_nums, cnt_range = 0, 0
            bit = 1 << b

            for num in nums:
                if bit & num:
                    cnt_nums += 1

            for i in range(1, len(nums)):
                if bit & i:
                    cnt_range += 1

            if cnt_nums > cnt_range:
                res |= bit

        return res
    
# Time Complexity: O(17 * n) = O(n)
# Space Complexity: O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for i in nums:
            if i in seen:
                return i
            seen.add(i)
        return -1
    
# Time Complexity: O(n)
# Space Complexity: O(n)

