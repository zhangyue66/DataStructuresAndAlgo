class Solution:
    def asteroidCollision(self, asteroids):

        stack = []

        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
            else:
                if stack[-1]>0 and asteroid < 0:
                    val = stack.pop()
                    if abs(val) > abs(asteroid):
                        stack.append(val)
                    elif abs(val) < abs(asteroid):
                        stack.append(asteroid)
                else:
                    stack.append(asteroid)

                while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    if abs(val1) > abs(val2):
                        stack.append(val1)
                    elif abs(val1) < abs(val2):
                        stack.append(val2)


        return stack




yz = Solution()
asteroids = [5,10,-5]
print(yz.asteroidCollision(asteroids))
