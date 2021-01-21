class Solution:
    def validSquare(self, p1,p2,p3,p4):
        #values as square, values record how many edges, a=2**0.5 * b

        values = []
        p = [p1,p2,p3,p4]
        for i in range(3):
            for j in range(i+1,4):
                edge = ((p[i][0] - p[j][0])**2 +(p[i][1]-p[j][1])**2)
                if edge not in values:
                    values.append(edge)

        if len(values) != 2:
            return False
        if (values[0]) *2 == values[1] or (values[1]) *2 == values[0]:
            return True
        return False

p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
yz = Solution()
print(yz.validSquare(p1,p2,p3,p4))
