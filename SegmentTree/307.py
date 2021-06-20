class SegmentTreeNode:
    def __init__(self,start,end,summ=0,left=None,right=None):
        self.start = start
        self.end = end
        self.sum = summ
        self.left = left
        self.right = right
        
class NumArray:

    def __init__(self, nums: List[int]):
        def buildTree(start,end,nums):
            if start == end:
                return SegmentTreeNode(start,end,nums[start])
            mid = start+(end-start)//2
            left = buildTree(start,mid,nums)
            right = buildTree(mid+1,end,nums)
            return SegmentTreeNode(start,end,left.sum+right.sum,left,right)
        
        self.root = buildTree(0,len(nums)-1,nums)
        

    def update(self, index: int, val: int) -> None:
        def updateTree(root,index,val):
            if root.start == root.end == index:
                root.sum = val
                return
            mid = (root.start + root.end) // 2
            if index <= mid:
                updateTree(root.left,index,val)
            else:
                updateTree(root.right,index,val)
            root.sum = root.left.sum + root.right.sum
        updateTree(self.root,index,val)
        

    def sumRange(self, left: int, right: int) -> int:
        def querySum(root,left,right):
            if root.start == left and root.end == right:
                return root.sum
            mid = (root.start + root.end) // 2
            if right <= mid:
                return querySum(root.left,left,right)
            elif left > mid:
                return querySum(root.right,left,right)
            else:
                # overlap scenario 
                return querySum(root.left,left,mid) + querySum(root.right,mid+1,right)
        return querySum(self.root,left,right)
