class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = { "n":[0,1],"s":[0,-1],"w":[-1,0],"e":[1,0]}   
        block = set(map(tuple,obstacles))
        #print(block)
        start = [0,0]
        face = "n"
        ans = 0
        
        
        def turn(face,num):
            if face == "n":
                if num == -1:
                    return "e"
                elif num == -2:
                    return "w"
            elif face == "s":
                if num == -2:
                    return "e"
                elif num == -1:
                    return "w"
            elif face == "e":
                if num == -2:
                    return "n"
                elif num == -1:
                    return "s"
            else:
                if num == -2:
                    return "s"
                elif num == -1:
                    return "n"
                
            return face
        
        for com in commands:
            #print(start)
            if com == -1:
                face = turn(face,com)
                
            elif com == -2:
                face = turn(face,com)
            else:
                
                step = direction[face]
                #print(step)
                #print(com)
                for i in range(com):
                    #print((start[0]+step[0],start[1]+step[1]))
                    if (start[0]+step[0],start[1]+step[1]) not in block:
                        
                        start[0]+=step[0]
                        start[1]+=step[1]
                        
                    else:
                        break
            #print(start)            
            ans = max(ans,start[0]**2+start[1]**2)
                        
        return ans
                    
                
            
