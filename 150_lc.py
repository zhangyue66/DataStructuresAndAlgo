class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        operands = ["+","-","*","/"]
        if len(tokens) == 0:
            return 0

        for token in tokens:
            print(stack)
            if token not in operands:
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if token == "+":
                    stack.append(num1+num2)
                elif token == "-":
                    stack.append(num1-num2)
                elif token == "/":
                    stack.append(int(num1/num2))
                else:
                    stack.append(num1*num2)

        return stack[0]

yz = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(yz.evalRPN(tokens))
