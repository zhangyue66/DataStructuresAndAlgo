class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)

            while stack and stack[-1] == popped[j]:
                j+=1
                stack.pop()

        if len(stack) != 0:
            return False
        return True


yz = Solution()
pushed = [1,2,3,4,5]
#popped = [4,5,3,2,1]
popped =        [4,3,5,1,2]
print(yz.validateStackSequences(pushed,popped))
