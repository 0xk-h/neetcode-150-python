from typing import Optional
from linkedlist import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode(0)
        curr = res
        
        while list1 and list2:

            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next

            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            
            curr = curr.next

        while list1:
            curr.next = ListNode(list1.val)
            curr = curr.next
            list1 = list1.next

        while list2:
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next

        return res.next