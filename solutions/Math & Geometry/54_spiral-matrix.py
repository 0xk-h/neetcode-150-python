from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total = len(matrix) * len(matrix[0])
        res = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        while top < bottom and left < right:
            # Left
            for j in range(left, right):
                res.append(matrix[top][j])
            top += 1

            # Down
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Boundary check
            if top >= bottom or left >= right:
                break

            # Right
            for j in range(right -1, left -1, -1):
                res.append(matrix[bottom - 1][j])
            bottom -= 1

            # Up
            for i in range(bottom -1, top -1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
    
# Time Complexity: O(m * n)
# Space Complexity: O(1)


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total = len(matrix) * len(matrix[0])
        res = []
        i, j = 0, 0
        while total > 0:
            # Right
            while j < len(matrix[i]) and matrix[i][j] != "x":
                res.append(matrix[i][j])
                matrix[i][j] = "x"
                j += 1
                total -= 1

            j -= 1
            i += 1

            # Down
            while i < len(matrix) and matrix[i][j] != "x":
                res.append(matrix[i][j])
                matrix[i][j] = "x"
                i += 1
                total -= 1

            i -= 1
            j -= 1

            # Left
            while j >= 0 and matrix[i][j] != "x":
                res.append(matrix[i][j])
                matrix[i][j] = "x"
                j -= 1
                total -= 1

            j += 1
            i -= 1

            # Up
            while i >= 0 and matrix[i][j] != "x":
                res.append(matrix[i][j])
                matrix[i][j] = "x"
                i -= 1
                total -= 1

            i += 1
            j += 1

        return res
    
# Time Complexity: O(m * n)
# Space Complexity: O(1)


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix[0]
            del matrix[0]

            for i in range(len(matrix)):
                res.append(matrix[i].pop())

            while matrix and not matrix[i]:
                matrix.pop()
                i -= 1

            if not matrix:
                return res

            for j in range(len(matrix[-1]) -1, -1, -1):
                res.append(matrix[-1][j])
            matrix.pop()

            for i in range(len(matrix) -1, -1, -1):
                res.append(matrix[i][0])
                del matrix[i][0]

            i = len(matrix) - 1
            while matrix and not matrix[i]:
                matrix.pop()
                i -= 1

        return res
    
# Time Complexity: O(m * n)
# Space Complexity: O(1)

