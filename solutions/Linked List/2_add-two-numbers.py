from typing import Optional
from linkedlist import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode(0)
        curr = res
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry

            curr.next = ListNode(total % 10)
            carry = total // 10

            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return res.next
    
# Time Complexity: O(max(m, n))
# Space Complexity: O(max(m, n))


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        res = head
        carry = 0

        while l1 and l2:
            x = l1.val + l2.val + carry
            carry = x // 10

            res.next = ListNode(x % 10)
            res = res.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            x = l1.val + carry
            carry = x // 10

            res.next = ListNode(x % 10)
            res = res.next
            l1 = l1.next

        while l2:
            x = l2.val + carry
            carry = x // 10

            res.next = ListNode(x % 10)
            res = res.next
            l2 = l2.next

        if carry:
            res.next = ListNode(carry)

        return head.next

# Time Complexity: O(max(m, n))
# Space Complexity: O(max(m, n))

