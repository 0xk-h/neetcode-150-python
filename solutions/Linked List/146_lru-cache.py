from collections import OrderedDict

class Node:
    def __init__(self, val = 0,key = 0, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.front = self.back = None

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            if node.key == self.front.key and self.front.next:
                self.front = self.front.next
            if node.key != self.back.key:
                if node.prev:
                    node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = self.back
                self.back.next = node
                self.back = self.back.next
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key].val = value
            _ = self.get(key)
            return

        # Insert the newnode
        newNode = Node(value, key)
        if not self.back:
            self.front = self.back = newNode
        else:
            self.back.next = newNode
            newNode.prev = self.back
            self.back = self.back.next
        self.mp[key] = newNode

        # Remove least recently used
        if self.capacity == 0:
            x = self.front.key
            self.front = self.front.next
            self.front.prev = None
            self.mp[x].next = None
            del self.mp[x]
        else:
            self.capacity -= 1


# Time Complexity: O(1) for both get and put
# Space Complexity: O(1)


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            if self.size == self.capacity:
                self.cache.popitem(last=False)
            else:
                self.size += 1
        
# Time Complexity: O(1) for both get and put
# Space Complexity: O(1)