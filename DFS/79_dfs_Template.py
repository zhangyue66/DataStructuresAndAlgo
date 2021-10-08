class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
            return False
        m,n = len(board),len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        
        def dfs(x,y,index):
            #check x,y out of bound or not
            if x < 0 or y < 0 or x >= m or y >= n:
                return False 
            # if index > len(word):
            #     return False
            if board[x][y] != word[index]:
                return False
            if index == len(word)-1 and not visited[x][y] :
                return True


            if not visited[x][y]: 
                #if board[x][y] == word[index]:
                    
                visited[x][y] = True
                found = dfs(x+1,y,index+1) or dfs(x-1,y,index+1) or dfs(x,y+1,index+1) or dfs(x,y-1,index+1)

                visited[x][y] = False
                return found
            
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
