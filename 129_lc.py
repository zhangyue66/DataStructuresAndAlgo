class Solution:
    def sumNumbers(self, root) -> int:


        self.res = 0

        def dfs(node,prev):
            if node is None:
                return

            if node.left is None and node.right is None: # reaching leaf node
                self.res += 10* prev + node.val
            prev = 10*prev+node.val
            dfs(node.left,prev)
            dfs(node.right,prev)

        dfs(root,0)

        return self.res

    def sumNumbers2(self, root) -> int:

        num = []
        res = 0


        if root is None:
            return res

        queue = [root]


        while queue:

            cur = queue.pop(0)

            if cur.left is None and cur.right is None:
                res += cur.val


            if cur.left is not None:
                cur.left.val = cur.val*10 + cur.left.val
                queue.append(cur.left)

            if cur.right is not None:
                cur.right.val = cur.val*10+cur.right.val
                queue.append(cur.right)


        return res
