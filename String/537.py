class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        print(num1,num2)
        a,b = num1[0],num1[1]
        c,d = num2[0],num2[1]
        real1 = int(a)*int(c)
        real2 = int(b[:-1])*int(d[:-1])
        complex1 = int(a)*int(d[:-1]) + int(c)*int(b[:-1])
        return str(real1-real2) + "+" + str(complex1) + "i"
        
