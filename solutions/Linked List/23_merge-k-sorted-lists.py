from typing import List, Optional
from linkedlist import ListNode
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) >= 2:

            merged_lists = []
            for i in range(0, len(lists), 2):
                if (i + 1) >= len(lists):
                    merged_lists.append(lists[i])
                else:
                    head = self.merge(lists[i], lists[i + 1])
                    merged_lists.append(head)

            lists = merged_lists

        if not lists or not lists[0]:
            return None
        else:
            return lists[0]

    def merge(self, list1, list2):
        head = ListNode()
        curr = head
                        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next

            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return head.next

# Time Complexity: O(n log k)
# Space Complexity: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

    def __gt__(self, other):
        return self.node.val > other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        Heap = [Node(node) for node in lists if node]
        heapq.heapify(Heap)

        res = ListNode()
        curr = res

        while Heap:
            wrapper = heapq.heappop(Heap)
            curr.next = wrapper.node
            curr = curr.next
            
            if wrapper.node.next:
                heapq.heappush(Heap, Node(wrapper.node.next))

        return res.next
    
# Time Complexity: O(n log k)
# Space Complexity: O(k)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        while len(lists) >= 2:
            list1 = lists.pop()
            list2 = lists.pop()

            head = ListNode()
            curr = head

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    curr = curr.next
                    list1 = list1.next

                else:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next

            if list1:
                curr.next = list1

            if list2:
                curr.next = list2

            lists.append(head.next)

        if not lists or not lists[0]:
            return None
        else:
            return lists[0]
        
# Time Complexity: O(n * k)
# Space Complexity: O(1)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        
        head = ListNode(0)
        curr = head
        data = []
        for node in lists:
            while node:
                data.append(node.val)
                node = node.next

        data.sort()

        for val in data:
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next

        return head.next

# Time Complexity: O(n log n)
# Space Complexity: O(n)