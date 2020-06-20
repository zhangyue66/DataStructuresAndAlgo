# class Solution:
#     def numTimesAllBlue(self, light):
#         # 0 is off,1 is one, 2 is blue
#         cnt = 0
#         bulb = [0]*len(light)
#         step = 0
#         for i in range(len(light)):
#             bulb[light[i]-1] = 1
#             step += 1
#             if bulb[0:step+1] == [1]*step:
#                 bulb[0:step+1] = [2]* step
#                 cnt += 1
#             elif bulb[0:step] == [2]*(step-1) and bulb[step+1] == 1:
#                 bulb[step] = 2
#                 cnt += 1
#             elif step == len(light) and bulb[step] == 1:
#                 bulb[light[i]] =2
#                 cnt += 1
#
#         return cnt
class Solution:
    def numTimesAllBlue(self, light) -> int:
        maximum = -float("inf")
        ref = []
        res = 0
        for i in light:
            ref.append(i)
            if i > maximum:
                maximum = i
            if maximum == len(ref):
                res += 1
        return res


yz = Solution()
light = [2,1,3,5,4]
print(yz.numTimesAllBlue(light))
