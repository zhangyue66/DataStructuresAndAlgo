# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.ans = []
        
        self.path = ""
        
        
        def dfs(node,path,ans):
            if node is None:
                return []
            else:
                
                if node.left is None and node.right is None: #reaching leaf
                    path+=str(node.val)
                    ans.append(path)
                    
                if node.left:
                    dfs(node.left,path+str(node.val),ans)
                if node.right:
                    dfs(node.right,path+str(node.val),ans)        
        
        dfs(root,self.path,self.ans)
        
        #output is ['233', '231', '211']
        
        def is_palin(number):
            if len(number) == 1:
                return True
            dict = {}
            for _ in number:
                if _ not in dict:
                    dict[_] = 1
                else:
                    dict[_] += 1
                    
            cnt = 0
            
            for key,value in dict.items():
                if value % 2 != 0:
                    cnt += 1
                    
            if cnt <= 1:
                return True
            else:
                return False
                    
                    
        
        if len(self.ans) ==0 :
            return 0
        cnt = 0
        for _ in self.ans:
            if is_palin(_) == True:
                cnt += 1
                
        return cnt
        
        
        
        
        
        
        
        
        
