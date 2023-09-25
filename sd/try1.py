board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

rs=[]
s0={'1','2','3','4','5','6','7','8','9'}
rows=[]
for i in range(9):
    rows.append(s0-set(board[i]))
cols=[]
for i in range(9):
    col=[row[i] for row in board]
    cols.append(s0-set(col))

ns = [{}, {}, {}, {}, {}, {},{}, {}, {}]

ns[0] = s0-set(board[0][0:3]+board[1][0:3]+board[2][0:3])
ns[3] = s0-set(board[3][0:3]+board[4][0:3]+board[5][0:3])
ns[6] = s0-set(board[6][0:3]+board[7][0:3]+board[8][0:3])

ns[1] = s0-set(board[0][3:6]+board[1][3:6]+board[2][3:6])
ns[4] = s0-set(board[3][3:6]+board[4][3:6]+board[5][3:6])
ns[7] = s0-set(board[6][3:6]+board[7][3:6]+board[8][3:6])

ns[2] = s0-set(board[0][6:8]+board[1][6:8]+board[2][6:8])
ns[5] = s0-set(board[3][6:8]+board[4][6:8]+board[5][6:8])
ns[8] = s0-set(board[6][6:8]+board[7][6:8]+board[8][6:8])

dot_cnt=1
while dot_cnt!=0:
    dot_cnt=0
    for i in range(9):
        for j in range(9):
            if board[i][j]=='.':
                a=rows[i] & cols[j] & ns[3*(i//3)+j//3]
                if len(a)==1:
                    b=a.pop()
                    board[i][j]=b
                    rows[i].remove(b)
                    cols[j].remove(b)
                    ns[3*(i//3)+j//3].remove(b)
                else:
                    dot_cnt+=1

for i in range(9):
    print(board[i])
