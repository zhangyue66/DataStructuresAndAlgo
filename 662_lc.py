# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root) -> int:
        if root is None:
            return 0

        queue = [[root,1,1]]
        yz = []
        while queue:
            cur = queue.pop(0)
            yz.append([cur[1],cur[2]])
            #node,level,id
            level = cur[1]
            id = cur[2]
            node = cur[0]
            if node.left:
                queue.append([node.left,level+1,id*2])
            if node.right:
                queue.append([node.right,level+1,id*2+1])
        
        dict ={}
        for level,id in yz:
            if level not in dict:
                dict[level]=[id]
            else:
                dict[level].append(id)
                
        ans = 0
        
        for key,val in dict.items():
            mini = min(val)
            maxi = max(val)
            width = maxi-mini+1
            ans = max(ans,width)
            
        return ans
