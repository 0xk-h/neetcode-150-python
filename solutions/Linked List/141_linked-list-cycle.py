from typing import Optional
from linkedlist import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr  = head

        while curr:
            if curr in seen:
                return True

            seen.add(curr)
            curr = curr.next

        return False
    
# Time Complexity: O(n)
# Space Complexity: O(n)