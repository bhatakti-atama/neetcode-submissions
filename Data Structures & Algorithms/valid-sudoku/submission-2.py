class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            check = set()
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] in check:
                        return False
                    else:
                        check.add(board[i][j])
            
        for i in range(n):
            check = set()
            for j in range(n):
                if board[j][i] != ".":
                    if board[j][i] in check:
                        return False
                    else:
                        check.add(board[j][i])
        

        for i in range(3):
            for j in range(3):
                check = set()
                for k in range(3):
                    for l in range(3):
                        if board[k+(i*3)][l+(j*3)] != ".":
                            if board[k+(i*3)][l+(j*3)] in check:
                                return False
                            else:
                                check.add(board[k+(i*3)][l+(j*3)])
        
        return True