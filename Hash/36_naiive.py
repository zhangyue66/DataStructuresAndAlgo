from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.is_row_valid(board) and self.is_col_valid(board) and self.is_sub_valid(board)
    
    def is_row_valid(self,board):
        for i in range(9):
            maps = Counter(board[i])
            if not self.check_dup(maps):
                return False          
        return True
    
    def is_col_valid(self,board):
        for j in range(9):
            numb_map = {}
            for i in range(9):
                if board[i][j] not in numb_map:
                    numb_map[board[i][j]] = 1
                else:
                    numb_map[board[i][j]] += 1
            if not self.check_dup(numb_map):
                return False
        return True
    
    def is_sub_valid(self,board):
        # find all the 9 - sub squar
        for i in (0,3,6):
            for j in (0,3,6):
                #print(i,j)
                sub = [[board[x][y] for y in range(j,j+3)] for x in range(i,i+3)]
                #print(sub)
                sub_dic = {}
                for a in range(3):
                    for b in range(3):
                        if sub[a][b] not in sub_dic:
                            sub_dic[sub[a][b]] = 1
                        else:
                            sub_dic[sub[a][b]] += 1
                            
                if not self.check_dup(sub_dic):
                    return False
        return True
    
    def check_dup(self,mapping):
        for k,v in mapping.items():
            if k == ".":
                continue
            if v > 1:
                return False
        return True
        
