from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        dia1 = set()
        dia2 = set()
        board = [["."] * n for _ in range(n)]

        def back(r):

            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c not in col and (r + c) not in dia1 and (r - c) not in dia2:
                    board[r][c] = "Q"
                    col.add(c)
                    dia1.add(r + c)
                    dia2.add(r - c)
                    back(r+1)
                    dia2.remove(r - c)
                    dia1.remove(r + c)
                    col.remove(c)
                    board[r][c] = "."

        back(0)
        return res
    
# Time Complexity: O(n!)
# Space Complexity: O(n^2)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = [False] * n
        dia1 = [False] * (n * 2)
        dia2 = [False] * (n * 2)
        board = [["."] * n for _ in range(n)]

        def back(r):

            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if not col[c] and not dia1[r + c] and not dia2[r - c + n]:
                    board[r][c] = "Q"
                    col[c] = True
                    dia1[r + c] = True
                    dia2[r - c + n] = True
                    back(r+1)
                    dia2[r - c + n] = False
                    dia1[r + c] = False
                    col[c] = False
                    board[r][c] = "."

        back(0)
        return res
    
# Time Complexity: O(n!)
# Space Complexity: O(n^2)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def back(r, col, dia1, dia2):

            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if not col & 1 << c and not dia1 & 1 << (r + c) and not dia2 & 1 << (r - c + n):
                    board[r][c] = "Q"
                    col |= 1 << c
                    dia1 |= 1 << (r + c)
                    dia2 |= 1 << (r - c + n)
                    back(r+1, col, dia1, dia2)
                    dia2 ^= 1 << (r - c + n)
                    dia1 ^= 1 << (r + c)
                    col ^= 1 << c
                    board[r][c] = "."

        back(0, 0, 0, 0)
        return res
    
# Time Complexity: O(n!)
# Space Complexity: O(n^2)