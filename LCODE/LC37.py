board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

class Solution:
    def solveSudoku(self, board: [[]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col = [[False] * 9 for i in range(9)]
        row = [[False] * 9 for i in range(9)]
        place = [[False] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    col[j][num] = True
                    row[i][num] = True
                    place[i // 3 * 3 + j // 3][num] =True
                    
        def dfs(i:int,j:int)->bool:
            if j == 9:
                return dfs(i+1,0)
            if i == 9:
                return True
            if board[i][j] != ".":
                return dfs(i,j+1)
            for k in range(9):
                if (col[j][k] == True
                    or row[i][k] == True
                    or place[i // 3 *3 +j //3][k] == True):
                    continue
                board[i][j] =str(k+1)
                col[j][k] = True
                row[i][k] = True
                place[i // 3 *3 +j //3][k] == True
                if dfs(i,j+1) == True:
                    return True
                board[i][j] = "."
                col[j][k] = False
                row[i][k] = False
                place[i // 3 *3 +j //3][k] == False
                return False

        dfs(0,0)
        print(board)

        a=Solution(board)
        a.solveSudoku(board)
        