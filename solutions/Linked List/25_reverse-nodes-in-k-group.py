from typing import Optional
from linkedlist import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        dummy = ListNode()
        prev, curr = dummy, head
        prev.next = curr
        step = 1

        while curr and curr.next:
            curr = curr.next
            step += 1

            if step == k:
                next_grp = curr.next
                n1 = None
                n2 = prev.next
                while n1 != curr:
                    temp = n2.next
                    n2.next = n1
                    n1 = n2
                    n2 = temp
                    
                old_head = prev.next
                old_head.next = next_grp
                prev.next = curr
                prev = old_head
                curr = next_grp
                step = 1

        return dummy.next
    
# Time Complexity: O(n)
# Space Complexity: O(1)