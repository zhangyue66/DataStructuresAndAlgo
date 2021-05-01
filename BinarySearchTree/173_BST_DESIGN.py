# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nums=[]
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            
            self.nums.append(root.val)
            
            dfs(root.right)
            
        dfs(root)
        
        self.pointer = None

    def next(self) -> int:
        if not self.pointer:
            self.pointer=0
        ans = self.nums[self.pointer]  
        self.pointer += 1
        return ans
      

    def hasNext(self) -> bool:
        if self.pointer is None:
            return True
        if self.pointer >= len(self.nums):
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
