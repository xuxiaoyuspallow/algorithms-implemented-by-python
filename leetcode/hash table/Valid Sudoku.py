"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.board = board
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.' and not self.isSafe(row,col,board[row][col]):
                    return False
        return True

    def isSafe(self, row, col, ch):
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkrow(row, col,ch) and self.checkcol(col, row,ch) and self.checksquare(boxrow, boxcol,row,col, ch):
            return True
        return False

    def checkrow(self, row, unneedcol,ch):
        for col in range(9):
            if col == unneedcol:
                continue
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, unneedrow,ch):
        for row in range(9):
            if row == unneedrow:
                continue
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col,unneedrow, unneedcol,ch):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if r == unneedrow and c == unneedcol:
                    continue
                if self.board[r][c] == ch:
                    return False
        return True

Solution().isValidSudoku([["5","3",".",".","5",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])