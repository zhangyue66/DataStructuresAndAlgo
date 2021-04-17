class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack:
                element = stack[-1]
                letter,cnt = element[0],element[1]
                if letter != char:
                    stack.append([char,1])
                else:
                    cur = stack.pop()
                    cur[1] += 1
                    if cur[1] < k:
                        stack.append([cur[0],cur[1]])
                            
                
            else:
                stack.append([char,1])
                
        #print(stack)
        if not stack:
            return ""
        
        ans = ""
        for element in stack:
            ans += element[0]*element[1]
            
        return ans 
