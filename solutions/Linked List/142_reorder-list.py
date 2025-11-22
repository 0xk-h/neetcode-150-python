from typing import Optional
from collections import deque
from linkedlist import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        prev, curr = None, slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge
        list1 = head
        list2 = prev
        while list2:
            list1.next, list1 = list2, list1.next
            list2.next, list2 = list1, list2.next

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        prev, curr = None, slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge
        list1 = head
        list2 = prev
        turn = False
        while list2:
            if turn:
                list2.next, list2 = list1, list2.next
            else:
                list1.next, list1 = list2, list1.next

            turn = not turn

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst = deque()
        curr = head

        while curr:
            lst.append(curr.val)
            curr = curr.next

        curr = head
        back = 0

        while curr:
            if back:
                curr.val = lst.pop()
            else:
                curr.val = lst.popleft()

            curr = curr.next
            back = ~back

# Time Complexity: O(n)
# Space Complexity: O(n)