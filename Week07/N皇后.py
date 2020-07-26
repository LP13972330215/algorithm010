#!/usr/bin/python3
#Author:pliu

def solveNQueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]  # 建立N×N的棋盘
    res = []

    def helper(left_diagonal, right_diagonal, column):
        j = len(column)
        if len(column) == n:
            tmp = []
            for k in board:  # 分行收集
                tmp.append(''.join(k))
            res.append(tmp)
        for i in range(n):
            if (i in column) or (i - j in left_diagonal) or (i + j in right_diagonal):
                continue
            board[j][i] = 'Q'
            helper(left_diagonal + [i - j], right_diagonal + [i + j], column + [i])
            board[j][i] = '.'

    helper(left_diagonal=[], right_diagonal=[], column=[])
    return res

if __name__ == '__main__':
    data = 4
    print(len(solveNQueens(data)))