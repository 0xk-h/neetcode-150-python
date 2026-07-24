from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                break

            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1

        l, r = 0, len(matrix[0]) - 1
        i = mid

        while l <= r:
            mid = (l + r) // 2
            if matrix[i][mid] == target:
                return True

            elif target > matrix[i][mid]:
                l = mid + 1
            else:
                r = mid - 1

        return False

# Time Complexity: O(log m + log n)
# Space Complexity: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1

        return False
            
# Time Complexity: O(m + n)
# Space Complexity: O(1)