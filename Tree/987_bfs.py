# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # use BFS to traverse all the nodes in tree
        row,col = 0,0
        queue = [(root,row,col)]
        dict = defaultdict(list)
        keys = []
        ans = []
        
        while queue:
            cur,row,col = queue.pop(0)
            dict[(row,col)].append(cur.val)
            if col not in keys:
                keys.append(col)
            if cur.left:
                queue.append((cur.left,row+1,col-1))
            if cur.right:
                queue.append((cur.right,row+1,col+1))
             
        keys.sort()
        yz = []
        for k,v in dict.items():
            yz.append(k)
            v.sort()       
        #print(dict)
        ans =[[] for i in range(len(keys))]
        yz = sorted(yz,key=lambda x:x[1])
        for k in yz:
            ans[keys.index(k[-1])] +=(dict[k])
        return ans
        
        
        
