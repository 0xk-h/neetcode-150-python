class Fenwick:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.tree[i] += arr[i - 1]
            parent = i + (i & -i)
            if parent <= self.n:
                self.tree[parent] += self.tree[i]

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)



"""
        #For testing purposes
"""

def run_test_case(arr, operations):
    ft = Fenwick(arr)

    results = []

    for op in operations:
        if op[0] == "range_sum":
            results.append(ft.range_sum(op[1], op[2]))
        elif op[0] == "update":
            ft.update(op[1], op[2])

    return results


def judge(arr, operations, expected):
    print("Input Array:", arr)
    print("Expected:", expected)

    output = run_test_case(arr, operations)

    print("Your Output:", output)

    if output == expected:
        print("Status: ACCEPTED ✅\n")
    else:
        print("Status: WRONG ANSWER ❌\n")


if __name__ == "__main__":

    arr1 = [1, 3, 5, 7, 9, 11]
    operations1 = [
        ("range_sum", 2, 5),
        ("update", 3, 4),
        ("range_sum", 2, 5)
    ]
    expected1 = [24, 28]
    judge(arr1, operations1, expected1)


    arr2 = [5, -2, 7, -3, 4]
    operations2 = [
        ("range_sum", 1, 5),
        ("range_sum", 2, 4),
        ("update", 4, 3),
        ("range_sum", 2, 4)
    ]
    expected2 = [11, 2, 5]
    judge(arr2, operations2, expected2)


    arr3 = [0, 0, 0, 0, 0]
    operations3 = [
        ("range_sum", 1, 5),
        ("update", 4, 10),
        ("range_sum", 3, 5)
    ]
    expected3 = [0, 10]
    judge(arr3, operations3, expected3)
