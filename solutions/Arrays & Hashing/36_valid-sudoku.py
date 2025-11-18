from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in col:
                        return False
                    col.add(board[i][j])

        start = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]

        for x, y in start:
            box = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] != ".":
                        if board[i][j] in box:
                            return False
                        box.add(board[i][j])
        return True
    
# Time Complexity: O(1) - board size is fixed
# Space Complexity: O(1) - board size is fixed


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != ".":
                    if x in rows[i] or x in cols[j] or x in box[(i//3)*3 + j//3]:
                        return False

                    rows[i].add(x)
                    cols[j].add(x)
                    box[(i//3) *3 + j//3].add(x)

        return True
# [One Pass Solution]
# Time Complexity: O(1) - board size is fixed
# Space Complexity: O(1) - board size is fixed

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [0] * 9
        cols = [0] * 9
        box = [0] * 9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = 1 << (int(board[i][j]) - 1)
                    if val & rows[i] or val & cols[j] or val & box[(i//3)*3 + j//3]:
                        return False

                    rows[i] |= val
                    cols[j] |= val
                    box[(i//3) *3 + j//3] |= val

        return True

# [BitMask Solution]
# Time Complexity: O(1) - board size is fixed
# Space Complexity: O(1) - board size is fixed