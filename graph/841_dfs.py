class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = [False]*len(rooms)
        
        def dfs(start,rooms):
            if not self.visited[start]:
                self.visited[start] = True
                
            for room in rooms[start]:
                if not self.visited[room]:
                    dfs(room,rooms)
                    
        dfs(0,rooms)
        
        for res in self.visited:
            if not res:
                return False
            
        return True
