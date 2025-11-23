from typing import Optional
from randomlist import Node

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None}
        copy = Node(0)

        old = head
        new = copy

        while old:
            new.next = Node(old.val)
            mp[old] = new.next
            old = old.next
            new = new.next

        old = head
        new = copy.next

        while old:
            new.random = mp[old.random]
            new = new.next
            old = old.next

        return copy.next
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None}
        copy = Node(0)

        old = head
        new = copy

        while old:
            if old in mp:
                new.next = mp[old]
            else:
                new.next = Node(old.val)
                mp[old] = new.next

            if old.random in mp:
                new.next.random = mp[old.random]
            else:
                new.next.random = Node(old.random.val)
                mp[old.random] = new.next.random

            old = old.next
            new = new.next

        return copy.next
    
# Time Complexity: O(n)
# Space Complexity: O(n)