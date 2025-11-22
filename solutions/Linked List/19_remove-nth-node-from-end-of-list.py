from typing import Optional
from linkedlist import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = head, head

        for _ in range(n):
            curr = curr.next
        if not curr:
            return head.next

        while curr.next:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next

        return head
        
# Time Complexity: O(n)
# Space Complexity: O(1)