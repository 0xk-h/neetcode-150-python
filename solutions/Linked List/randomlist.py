class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x) if x else 0
        self.next = next
        self.random = random

    @staticmethod
    def from_list(lst):
        if not lst:
            return None
        
        nodes = [Node(val) for val, _ in lst]
        n = len(nodes)
        
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
        
        for i, (_, r_idx) in enumerate(lst):
            if r_idx is not None:
                nodes[i].random = nodes[r_idx]
        
        return nodes[0]
    
    def __hash__(self):
        return hash(id(self))
    
    def __repr__(self):
        node_to_idx = {}
        idx = 0
        node = self
        while node:
            node_to_idx[node] = idx
            node = node.next
            idx += 1
        
        parts = []
        node = self
        while node:
            r_idx = node_to_idx.get(node.random, None)
            parts.append(f"{node.val}({r_idx})")
            node = node.next
        
        return " -> ".join(parts)
    
    # Only yeild the next pointer in the iteration.
    def __iter__(self):
        node = self
        while node:
            yield node.val
            node = node.next

    def __eq__(self, other):
        def build_index_map(head):
            idx_map = {}
            node_list = []
            node = head
            idx = 0
            while node:
                idx_map[node] = idx
                node_list.append(node)
                node = node.next
                idx += 1
            return idx_map, node_list

        if not other:
            return False

        self_map, self_nodes = build_index_map(self)
        other_map, other_nodes = build_index_map(other)

        if len(self_nodes) != len(other_nodes):
            return False

        for n1, n2 in zip(self_nodes, other_nodes):
            if n1.val != n2.val:
                return False

            r1 = self_map.get(n1.random, None) if n1.random else None
            r2 = other_map.get(n2.random, None) if n2.random else None
            if r1 != r2:
                return False

        return True
