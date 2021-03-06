# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # use dfs
        dict = defaultdict(list)
        
        self.cnt = 0
        def dfs(node,level):
            if not node:
                return
            dict[level].append(node.val)
            self.cnt += 1
            dfs(node.left,level+1)
            dfs(node.right,level+1)
            
        dfs(root,0)
        ans = []
        for i in range(self.cnt):
            if dict[i]:
                avg = sum(dict[i]) / len(dict[i])
                ans.append(avg)

        #print(dict)   
        return ans
