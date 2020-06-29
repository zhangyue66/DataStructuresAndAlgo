class Solution:
    def isValidSerialization(self, preorder):
        preorder = preorder.split(",")
        #['9', '3', '4', '#', '#', '1', '#', '#', '2', '#', '6', '#', '#']
        stack  = []
        if preorder.count("#") == len(preorder) and len(preorder) !=1:
            return False
        if len(preorder) >3:
            if preorder[1:].count("#") == len(preorder[1:]) :
                return False

        for _ in preorder:
            stack.append(_)

            # if _ == "#": #check if stack ending with two #s
            #     if len(stack) >2 and stack[-2:] == ["#","#"]:
            #         stack.pop()
            #         stack.pop()
            #         stack.pop()
            #         stack.append("#")

            while len(stack) >2 and stack[-2:] == ["#","#"]:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")

        #print(stack)
        if len(stack) ==1:
            if stack[0] == "#":
                return True

        return False
