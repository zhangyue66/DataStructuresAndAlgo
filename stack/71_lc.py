class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        path = path.split("/")
        
        for str in path:
            if str == "..":
                if stack:
                    stack.pop()
                    
            elif str and str != ".":
                stack.append(str)
                
        return "/"+"/".join(stack)
