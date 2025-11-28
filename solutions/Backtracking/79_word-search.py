from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def back(i, j, idx):
            if idx == len(word):
                return True

            if i >= m or i < 0 or j < 0 or j >= n:
                return False

            if board[i][j] == word[idx]:
                board[i][j] = "#"
                idx += 1
                if back(i+1, j, idx) or back(i, j+1, idx) or back(i-1, j, idx) or back(i, j-1, idx):
                    return True

                board[i][j] = word[idx - 1]

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and back(i, j, 0):
                    return True

        return False

# Time Complexity: O(m * 4^n)               m -> no. of cells in the board
# Space Complexity: O(n)                    n -> length of the word