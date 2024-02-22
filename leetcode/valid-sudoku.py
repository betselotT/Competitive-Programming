class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = 0
        row, col = 0, 0
        for i in range(9):
            mySet = set()
            for j in range(9):
                if board[i][j] in mySet:
                    return False
                else:
                    if board[i][j] != '.':
                        mySet.add(board[i][j])
        for i in range(9):
            mySet = set()
            for j in range(9):
                if board[j][i] in mySet:
                    return False
                else:
                    if board[j][i] != '.':
                        mySet.add(board[j][i])
        
        while row < 9:
            mySet = set()
            for i in range(3):
                for j in range(3):
                    if board[i + row][j + col] in mySet:
                        return False
                    else:
                        if board[i + row][j + col] != '.':
                            mySet.add(board[i + row][j + col])
            col += 3
            if col == 9:
                row += 3
                col = 0
        return True