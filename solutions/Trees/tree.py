uni_h, uni_tl, uni_tr, uni_invt, nl = "\u2500\u256d\u256e\u2534\n"
stripped = uni_h + uni_tl + uni_tr + ' '

def padded_lines(s, pad_l, pad_r):
    r_col, l_col = 0, float("inf")
    lines = s.splitlines()
    for line in lines:
        if line.isspace(): continue
        r_col = max(r_col, len(line.rstrip()))
        l_col = min(l_col, len(line) - len(line.lstrip()))
    extra_l = max(pad_l - l_col, 0)
    trim_l = max(l_col - pad_l, 0)
    prefix = ' ' * extra_l
    return [prefix + line[trim_l:].rstrip().ljust(r_col + pad_r) for line in s.splitlines()]

def find_span(s):
    n = len(s)
    r = len(s.rstrip(stripped))
    l = n - len(s.lstrip(stripped))
    return l, (l + r) // 2, r

def join_horizontal(a, b, prefix=None, lwidth=0, gap=1):
    res = prefix or []
    gap_str = ' ' * gap

    max_lines = max(len(a), len(b))

    for i in range(max_lines):
        a_line = a[i] if i < len(a) else ""
        b_line = b[i] if i < len(b) else ""
        res.append(a_line.ljust(lwidth) + gap_str + b_line)

    return '\n'.join(res)

def binary_edge(p, a, b):
    p = str(p)

    a = padded_lines(str(a), 0, 1)
    b = padded_lines(str(b), 1, 0)

    a_first = a[0] if a else ""
    b_first = b[0] if b else ""

    w_a = len(a_first)
    w_b = len(b_first)

    a_l, a_m, a_r = find_span(a_first) if a_first else (0, 0, 0)
    b_l, b_m, b_r = find_span(b_first) if b_first else (0, 0, 0)
    w_p = max(len(l) for l in p.splitlines())

    right_center_combined = w_a + 1 + b_m
    mid = (a_m + right_center_combined) // 2
    x_p = mid - (w_p // 2)
    p_lines = padded_lines(p, x_p, 0)

    connector_added = False
    if a_first or b_first:
        connector_added = True
        inner_len = (w_a + b_m - a_m)
        left_pad = ' ' * a_m
        connector = left_pad + uni_tl + uni_invt.center(inner_len, uni_h) + uni_tr

        p_lines.append(connector)
    return join_horizontal(a, b, prefix=p_lines, lwidth=w_a, gap=1 if connector_added else 0)


class TreeNode:
    def __init__(self, val, depth=1):
        self.val = val
        self.depth = depth
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, child):
        self._left = child
        if child:
            child.depth = self.depth + 1

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, child):
        self._right = child
        if child:
            child.depth = self.depth + 1

    def from_list(lst):
        if not lst:
            return None

        root = TreeNode(lst[0])
        queue = [root]
        i = 1

        while queue and i < len(lst):
            node = queue.pop(0)

            if i < len(lst) and lst[i]:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1

            if i < len(lst) and lst[i]:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1

        return root

    def __repr__(self):
        return draw_tree(self)

    def __hash__(self):
        return hash(id(self))
    
    def __iter__(self):
        stk = [(self)]
        while stk:
            node = stk.pop()

            if node:
                stk.append((node.right))
                stk.append((node.left))
                yield node.val


    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False

        return (
            self.val == other.val and
            self.left == other.left and
            self.right == other.right
        )
    
    def __lt__(self, other):
        if not isinstance(other, TreeNode):
            return NotImplemented
        return self.val < other.val

def draw_tree(node):
    if node is None:
        return ''
    left = draw_tree(node.left)
    right = draw_tree(node.right)
    return binary_edge(str(node.val), left, right)
