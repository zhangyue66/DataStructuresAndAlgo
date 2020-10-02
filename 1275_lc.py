class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        ttt = [["yz" for i in range(3)] for j in range(3)]
        if len(moves) <= 3:
            return "Pending"
        
        for i in range(len(moves)):
            #odd is A , even is B
            if i % 2 == 0:
                ttt[moves[i][0]][moves[i][1]] = "X"
            else:
                ttt[moves[i][0]][moves[i][1]] = "O"
                
        def check_win(ttt,letter):
            if ttt[0].count(letter) ==3 or ttt[1].count(letter) ==3 or ttt[2].count(letter) ==3:
                return True
            if ttt[0][0] == ttt[1][0] == ttt[2][0] == letter or ttt[0][1] == ttt[1][1] == ttt[2][1] == letter or ttt[0][2] == ttt[1][2] == ttt[2][2] == letter:
                return True
            if ttt[0][0] == ttt[1][1] == ttt[2][2] == letter:
                return True
            if ttt[0][2] == ttt[1][1] == ttt[2][0] == letter:
                return True
            
            
            return False
        
        if check_win(ttt,"X"):
            return "A"
        elif check_win(ttt,"O"):
            return "B"
        
        if len(moves) == 9:
            return "Draw"
        #print(ttt)
        return "Pending"
