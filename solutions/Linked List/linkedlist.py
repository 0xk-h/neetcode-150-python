class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode( { " -> ".join(str(v) for v in self) } )"

    @staticmethod
    def from_list(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        curr = head
        for val in lst[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def __iter__(self):
        node = self
        while node:
            yield node.val
            node = node.next

    def __eq__(self, other):
        if not other:
            return False
        return list(self) == list(other)

    def __getitem__(self, index):
        for i, val in enumerate(self):
            if i == index:
                return val
        raise IndexError("Index out of range")
