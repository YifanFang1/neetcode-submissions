class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            box = set()
            for j in range(9):
                # check row i
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                # check column i
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
                # check box i
                rb = (i // 3) * 3
                cb = (i % 3) * 3
                r = rb + j // 3
                c = cb + j % 3
                if board[r][c] != '.':
                    if board[r][c] in box:
                        return False
                    box.add(board[r][c])
        return True