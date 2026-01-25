from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        grid = []

        for j in range(n):
            curr = []
            for i in range(n - 1, -1, -1):
                curr.append(matrix[i][j])

            grid.append(curr)

        matrix[:] = grid

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(n):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse rows
        for i in range(n):
            matrix[i].reverse()

# Time Complexity: O(n^2)
# Space Complexity: O(1)